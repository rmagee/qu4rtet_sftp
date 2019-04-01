#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `quartet_sftp` package."""

import unittest

import os
from quartet_sftp import client
from paramiko import SFTP, SFTPClient
from paramiko import SSHClient
from paramiko import transport
from paramiko import AutoAddPolicy



class TestQuartet_sftp(unittest.TestCase):
    """Tests for `quartet_sftp` package."""

    def setUp(self):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(
            hostname='testsftphost', username='foo', password='pass', port=22)
        sftp_client = ssh_client.open_sftp()
        path = self.get_test_file_path()
        sftp_client.put(path, '/upload/epcis.xml')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_sftp_client(self):
        test_client = client.Client(
            'testhost','/upload',
            'http://testhost/capture/quartet-capture/?rule=EPCIS',
            #'http://testhost:8000',
            sftp_password='pass',
            sftp_user='foo',
            sftp_port=22,
            use_keys=False,
        )
        test_client.get()


    def get_test_file_path(self, file='data/epcis.xml'):
        curpath = os.path.dirname(__file__)
        return os.path.join(curpath, file)
