REST API
===========

.. _api-introduction:

REST api is a powerful and flexible Web apis, REST api can get and upload test data, it means you can 
get test data from iTMS and upload data from other platforms into iTMS. REST api improves iTMS’s 
expansibility much bigger.


REST api provide web pages for test data, you can edit them in their page.
You can create python script to edit data automatically with REST api.

If you want to start your python script, you should imports following staff in your python file.

.. code-block:: python
    :linenos:

    import requests
    import json
    from requests.auth import HTTPBasicAuth

And define the variable SERVER as your server url, for example:

.. code-block:: python
    :linenos:

    SERVER = 'http://127.0.0.1:8000'

This document introduces the URL and python code for test elements in the following sections.


.. role:: method

.. toctree::
   :maxdepth: 1

   api_quickstart.rst
   api_project.rst
   api_req.rst
   api_feature.rst
   api_app.rst
   api_testcase.rst
   api_testsuite.rst
   api_testplan.rst
   api_execution.rst
   api_result.rst



