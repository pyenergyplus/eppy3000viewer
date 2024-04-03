==============
eppy3000viewer
==============

viewer for E+ using eppy3000

Installation
============

Use a virtual environment to install and run. If you have not done this before, refer to this  `link on virtual environments <https://docs.python.org/3/library/venv.html>`_

To install the libraries needed to run, do

::
    
    pip install -r requirements.txt


Usage:
======

At the command prompt type::

    python runit.py

You will see::

    Bottle v0.12.19 server starting up (using WSGIRefServer())...
    Listening on http://localhost:8081/
    Hit Ctrl-C to quit.

Go to a browser and load the URL <http://localhost:8081/> or click on this `link<http://localhost:8081/>`_

Once you are on the web page, click on links and explore. It will be self explanatory

:Question: Where is the information on the web page coming from?
:Response: The data in the IDD file (or rather the ``Energy+.schema.epJSON``) is stored in a python native database called ``dbm``. The web page is reading that database
:Question: Can I do this for any version of the IDD ?
:Response: Yes. You can. We are yet to document this. Coming soon.
