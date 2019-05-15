=====
Usage
=====

Project Use
-----------

To use quartet_sftp in a project::

    import quartet_sftp

crontab Setup
-------------
First, clone quartet_sftp into your home directory.  If you are using a
QU4RTET server according to our typical path and environment recommendations,
you'd do the following

.. code-block:: text

    cd ~
    git clone https://gitlab.com/serial-lab/qu4rtet_sftp.git

Now create a .env file:

.. code-block:: text

    # assuming you are in the directory where you cloned the quartet sftp
    cp qu4rtet_sftp/quartet_sftp/.env_example qu4rtet_sftp/quartet_sftp/.env
    # vim qu4rtet_sftp/quartet_sftp/.env

In the .env file, configure the settings accordingly.  You will see the following

.. code-block:: text

    sftp_host = 'localhost'
    sftp_port = '1001'
    sftp_user = 'foo'
    sftp_pass = 'pass'
    sftp_path = '/upload'
    http_host = 'http://localhost:8000/capture/quartet-capture/?rule=EPCIS'
    #http_user = ''
    #http_pass = ''
    #http_port = 80
    #use_keys = False
    #content_type = ''

Your options are as follows:

.. list-table:: Options
    :widths: 33 33 33
    :header-rows: 1

    * - Name
      - Description
      - Required
    * - sftp_host
      - The host you will be polling for data.  Can be an ip address or host name.
      - True
    * - sftp_port
      - The port the remote sftp service is exposed on.  Default is 22.
      - False
    * - sftp_user
      - If user auth is enabled remotely, specify the user name here.
      - False
    * - sftp_pass
      - The sftp password
      - False
    * - sftp_path
      - Specify the path relative to the SFTP root that will be inspected.
      - False
    * - http_host
      - This is the host where any files found in the SFTP remote directory will be HTTP POSTed to.
      - True
    * - http_user
      - The user name to post with to the remote http endpoing.
      - False
    * - http_pass
      - The password for the http user.
      - False
    * - http_port
      - The http port to use if not specified in the url.  It is recommended to just spedcify this in the url.
      - False
    * - use_keys
      - If you are using the user ssh keys for authentication, set this to True
      - False
    * - content_type
      - If you are posting anything other than application/xml to the remote http endpoint, specify the content type here.
      - False




To invoke as a job with cron, here is what an example crontab config
could look like.

(The below examples assume that you are using a virutalenv named qu4rtet,
and have installed the quartet_sftp script in the home directory.  If these
values are different on your system adjust the examples below accordingly.)


Check every one minute:

.. code-block:: text

    */1 * * * * /home/ubuntu/.virtualenvs/qu4rtet/bin/python /home/ubuntu/qu4rtet_sftp/quartet_sftp/client.py

Check every day at 1 am:

.. code-block:: text

    0 1 * * * /home/ubuntu/.virtualenvs/qu4rtet/bin/python /home/ubuntu/qu4rtet_sftp/quartet_sftp/client.py

To edit crontab issue the following command:

.. code-block:: text

    crontab -e

Log Monitoring
--------------

If you set up `postfix` you can monitor the logs of your cron
job by tailing the root log as below:

.. code-block:: text

    sudo tail -f /var/mail/root

