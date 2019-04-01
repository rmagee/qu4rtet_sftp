=====
Usage
=====

Project Use
-----------

To use quartet_sftp in a project::

    import quartet_sftp

crontab Setup
-------------

To invoke as a job with cron, here is what an example crontab config
could look like.

(The below examples assume that you are using a virutalenv named qu4rtet,
and have installed the quartet_sftp script in the home directory.  If these
values are different on your system adjust the examples below accordingly.)


Check every one minute:

.. code-block:: text

    */1 * * * * /home/ubuntu/.virtualenvs/qu4rtet/bin/python /home/ubuntu/quartet_sftp/quartet_sftp/client.py

Check every day at 1 am:

.. code-block:: text

    0 1 * * * /home/ubuntu/.virtualenvs/qu4rtet/bin/python /home/ubuntu/quartet_sftp/quartet_sftp/client.py

To edit crontab issue the following command:

.. code-block:: text

    crontab -e
