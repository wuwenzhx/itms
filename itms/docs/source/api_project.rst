.. _api-project:

Project
=============

This section introduces how to get project list.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project
--------------

We can get project list with GET method.


:Object: Project
:Authorization: Basic Authorization


:method:`GET`

:Function: Get all of project list
:Usage: GET /api/project/
:Permission: All
:Parameters: None
:Response: Project List
:Successful Status: HTTP_200_OK
:Unsuccessful Status: HTTP_401_UNAUTHORIZED
:Sample Output:

::

    [
        {
            "id": 1,
            "name": "Media"
        },
        {
            "id": 4,
            "name": "DPDK"
        }
    ]

:Python code:

.. code-block:: python
    :linenos:

    def get_project_list():
        url = '{server_add}/api/project/'.format(server_add=SERVER)
        r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
        print r.status_code
        print r.json()