
Execution Center
------------------------------

iTMS supports communicate with iTEC, we get test machine information according to iTEC IP address. Then create an execution which include
testplan, machine configuration, test schedule and resource. Execute test by enabling the execution, after
testing, the result will be uploaded to report center.

In execution center, we can manage iTEC and execution.


iTEC Setting
^^^^^^^^^^^^^^^^^^^

iTEC Management displays iTEC in iTEC list, the filter is name.

.. image:: /_static/image/itec_list.png
   :width: 700px
   :alt: iTEC list
   :align: center
   :class: image

Add iTEC in |itec_new| page, enter iTEC name and IP address then save it, in confirm dialog choose YES to create iTEC
and NO to cancel. Click |delete| to discard the added iTEC.

.. image:: /_static/image/itec_add.png
   :width: 700px
   :alt: iTEC add
   :align: center
   :class: image

Edit iTEC by clicking item in iTEC List. In overview tab, update iTEC name and save, click |delete| to delete the iTEC.

In addition, iTEC includes workers, we also can get worker information in this tab.

.. image:: /_static/image/itec_modify.png
   :width: 700px
   :alt: iTEC modify
   :align: center
   :class: image

.. note:: We cannot delete an iTEC in use.


Execution Setting
^^^^^^^^^^^^^^^^^^

Execution Management shows execution information in execution list, its filters are name, environment type, status and
iTEC in |filter| page.

.. image:: /_static/image/exe_list.png
   :width: 700px
   :alt: Execution List
   :align: center
   :class: image

There are three type of environment, execution has different source and schedule according to its environment.

1. Regular. Execution of regular environment supports daily, weekly and other kinds of regression test. We should set
   execution time and git repo. The execution is valid by default.
2. One-time Commit ID. Execution of One-time Commit ID should set git repo, commit id and upload patch. It should be
   executed manually and it is invalid by default.
3. One-time Package. Execution of One-time Package need the package url. It's invalid by default and manually execute.

Add execution in |exe_new| page, select an iTEC will get iTEC information - workers and configuration from iTEC server.
Select the configuration in the drop-down list.

.. image:: /_static/image/exe_add.png
   :width: 700px
   :alt: Execution Add
   :align: center
   :class: image

The owner should be current user. Click search icon of TestPlan will go to TestPlan Filter page, the filters are name,
category and performance.

.. image:: /_static/image/exe_plan_filter.png
   :width: 400px
   :alt: Execution List
   :align: center
   :class: image

Select the environment type and enter corresponding schedule and source, then save it, in confirm dialog choose YES to
create execution and NO to cancel. Click |delete| to discard the added execution.


Edit execution. Regular execution is not editable, enabled execution of One-time Commit ID and One-time Package are
uneditable too, click uneditable item in Execution List will show execution information, click |exe_play| button to
change execution status and click |delete| button to delete the execution.

.. image:: /_static/image/exe_enable.png
   :width: 700px
   :alt: Execution List
   :align: center
   :class: image

For editable execution, iTMS will get iTEC information from iTEC server when go into execution detail, reset
configuration or other information then save, while click |delete| to delete the execution.

.. image:: /_static/image/exe_disable.png
   :width: 700px
   :alt: Execution List
   :align: center
   :class: image

.. note:: Only execution owner can edit or delete the execution.


.. |itec_new| image:: /_static/image/itec_new.png
.. |delete| image:: /_static/image/delete_btn.png
.. |exe_new| image:: /_static/image/exe_new.png
.. |filter| image:: /_static/image/filter.png
.. |exe_play| image:: /_static/image/exe_play.png