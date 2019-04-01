============
quartet_sftp
============


.. image:: https://gitlab.com/serial-lab/quartet_sftp/badges/master/coverage.svg
   :target: https://gitlab.com/serial-lab/quartet_sftp/pipelines

.. image:: https://img.shields.io/pypi/v/quartet_sftp.svg
        :target: https://pypi.python.org/pypi/quartet_sftp

.. image:: https://gitlab.com/serial-lab/quartet_sftp/badges/master/build.svg
        :target: https://gitlab.com/serial-lab/quartet_sftp/commits/master




QU4RTET SFTP Tools and Utilities.

* Free software: GNU General Public License v3


Features
--------

* The `Client` script will monitor a remote SFTP location for files and,
  when files are found, will attempt to HTTP post them into a remote
  QU4RTET system.  To configure the remote SFTP location, use a .env
  file (see the example .env) to configure users, remote locations
  content-types and other connection specifics.
