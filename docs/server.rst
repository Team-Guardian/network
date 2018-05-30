Server
======

"Server" is a stripped-down implementation of a HTTP server built on top of Python standard HTTP library. The entire server application code is contained in the ``server.py`` file and consists primarily of HTTP requests handling logic. Server settings are specified in ``config.cfg`` file, along with client and general settings (i.e. there is only one file for all the settings).

Server application is **not** meant to be run by invoking the Python interpreter on the ``server.py`` source file. Instead, it's meant to run within a Docker container, which brings us to the prerequisites for running the server.

Prerequisites
-------------

Since the server itself is built using only standard Python libraries (i.e. libraries that come with a Python installation), the only requirement you need to fulfill to run the server is get Docker.

To install Docker, follow the `instructions <https://docs.docker.com/get-started/>`_ on the official Docker website. You can either follow the steps to install Docker manually or you can use the installation script available from ``get.docker.com``. Scroll down to the end of the page for instructions on how to use the automated script.

Build a Container
-----------------

If Docker installation was successful, the next step is to create a container for Docker to run. When typing in the build command, make sure you don't forget the period at the end.

.. code-block:: bash

    sudo docker build -t airserver .

Run the Server
--------------

Run the script called ``run_server.sh`` to start up the server application. That script contains instructions for selecting the right container to run and putting it in the background. The script also sets the port on which the server will be listening and the directory, which will be the root of the server. 

Working with the Server
-----------------------

By default, the root directory of the server is mapped to the ``/var/www`` directory in the local filesystem. In other words, the server will treat ``/var/www`` as its ``/`` directory and serve all the requests relative to that directory. 

To get a better feel for how that works, create a dummy directory and a dummy file within that directory in your ``/var/www`` folder.

.. code-block:: bash

    sudo mkdir /var/www/testdir
    sudo touch /var/www/testdir/test.jpg

Then, open your browser and type in the following in your address bar: ``localhost:1346``. Note that the number after the colon is the port number that by default is set to ``1346``, but can be changed if necessary. Next, load the page in the browser - you should see a line of plain text that says 'testdir'. Now, change the address bar to ``localhost:1346/testdir``. This time, you should again see a line of plain text, but it would say 'test.jpg' - you get the gist.

Clean up the dummy files you've created and you are all set for using the server.

Stopping the Server
-------------------

You can stop a running server container with the following command.

.. code-block:: bash

    sudo docker container stop airserver

Note that you **don't** need to rebuild the container to restart the server. The container is not deleted after it's stopped, so you just need to re-run the shell script to start the server again.