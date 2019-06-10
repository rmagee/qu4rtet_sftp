# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2019 SerialLab Corp.  All rights reserved.
import base64
import requests
import dotenv
import os
import sys
from paramiko.client import SSHClient
from paramiko.sftp_client import SFTPClient
from paramiko import AutoAddPolicy


class Client:
    """
    The client class will connect to a remote SFTP location, pull all of
    the available files down and post them to an HTTP endpoint.
    """
    def __init__(self,
                 sftp_host,
                 sftp_path,
                 post_url,
                 post_user=None,
                 post_password=None,
                 sftp_user=None,
                 sftp_password=None,
                 sftp_port=22,
                 use_keys=True,
                 post_content_type='application/xml'
                 ) -> None:
        """
        Initializes a new SFTP client class.
        :param sftp_host: The host to connect to.
        :param sftp_path: The remote directory to check for files.
        :param post_url: The remote url to post files found to.
        :param post_user: The remote username to use.
        :param post_password: The remote password to use.
        :param sftp_password: The remote SFTP password.
        :param sftp_user: The remote SFTP user.
        :param sftp_port: The port to connect to. Default is 22.
        :param use_keys: Whether or not to use system SSH keys to
        authenticate.
        :param post_content_type: The HTTP content type to use when posting
        to the remote HTTP endpoint.  The default is 'application/xml'.
        When posting to QU4RTET this is less important since QU4RTET handles
        content negotiation within it's rules.
        """
        self.sftp_host = sftp_host
        self.sftp_password = sftp_password
        self.sftp_user = sftp_user
        self.sftp_path = sftp_path
        self.post_url = post_url
        self.use_keys = use_keys
        self.post_user = post_user
        self.post_password = post_password
        self.sftp_port = sftp_port
        self.post_content_type = post_content_type

    def get(self, sftp_path=None):
        """
        Call this function to get all of the files from the remote directory
        and post them to the remote HTTP endpoint.
        :param sftp_path: If you'd like to change the default remote SFTP
        path you can specify a different one on each call.
        :return: None.
        """
        print('running quartet sftp client')
        sshc = SSHClient()
        sshc.set_missing_host_key_policy(AutoAddPolicy())
        if self.use_keys:
            sshc.load_system_host_keys()
        sshc.connect(
            self.sftp_host,
            self.sftp_port,
            self.sftp_user,
            self.sftp_password
        )
        sftp_client = sshc.open_sftp()
        sftp_client.chdir(sftp_path or self.sftp_path)
        files = sftp_client.listdir()
        print('found %s files' % len(files))
        for file in files:
            file_name = os.path.basename(file)
            print('processing file %s' % file)
            if not file_name.startswith('.'):
                self._handle_file(file, sftp_path, sftp_client)
            else:
                print('ignoring file...')

    def _handle_file(self, file: str, path: str, sftp_client: SFTPClient):
        """
        Takes each file found in the SFTP location and posts to remote
        location.
        :param file:
        :param path:
        :param sftp_client:
        :return:
        """
        filehandle = sftp_client.file(file, 'rw')
        print('opened file handle with path %s...reading...' % file)
        data = filehandle.read()
        print('data has been read.')
        headers = None
        if self.post_user and self.post_password:
            auth_val = '%s:%s' % (self.post_user, self.post_password)
            auth_val = base64.b64encode(auth_val.encode('utf-8')).decode(
                'ascii')
            headers = {'Authorization': 'Basic %s' % auth_val,
                       'content-type': self.post_content_type}
        print('Posting data to quartet...')
        response = requests.post(self.post_url, data=data, headers=headers)
        print('Response %s' % response.raw)
        if response.status_code == 200 or response.status_code == 201:
            with open('/tmp/%s' % file, 'w') as f:
                f.write(data.decode('utf-8'))
            try:
                filehandle.close()
                sftp_client.remove(file)
            except OSError as e:
                sftp_client.chmod(file, 0o776)
                sftp_client.rename(file, '.%s' % file)
                print(sys.exc_info())
            print('file processed and removed.  backups are stored in /tmp.')

def execute():
    dotenv.load_dotenv()
    print('instantiating the client...')
    client = Client(
        os.getenv('sftp_host'),
        os.getenv('sftp_path'),
        os.getenv('http_host'),
        os.getenv('http_user', None),
        os.getenv('http_pass', None),
        os.getenv('sftp_user', None),
        os.getenv('sftp_pass', None),
        int(os.getenv('sftp_port', 22)),
        os.getenv('use_keys', False),
        os.getenv('content_type', 'application/xml')
    )
    client.get()

if __name__ == '__main__':
    execute()
