Test Center
===============

Test Center manage the test elements - Testcase, Testsuite and Testplan.

TestCase
----------------

Testcase Management page shows Testcase information in Testcase List, its filters are name and requirement, feature,
case type, performance in |filter| page.

.. image:: /_static/image/case.png
   :width: 700px
   :alt: Testcase Management
   :align: center
   :class: image

Add Testcase in |case_new| page, enter Testcase information then save it, in confirm dialog choose YES to create Testcase
and NO to cancel. Click |delete| to discard the added Testcase.

.. image:: /_static/image/case_add.png
   :width: 700px
   :alt: Testcase Management
   :align: center
   :class: image

Edit Testcase by clicking item in Testcase List.
In overview tab, update testcase information and save, while click |delete| to delete the Testcase.

.. image:: /_static/image/case_overview.png
   :width: 700px
   :alt: Modify Testcase
   :align: center
   :class: image

Testcase belongs to one or more Testsuite, they should have the same performance setting. The association
relationship between them can be changed. In Related Testsuite tab, TestSuite column lists all TestSuite with the same
performance setting as this Testcase, Related Testsuite column lists the related ones. Select the Testsuites then click
arrow button to set or cancel their association relationship.

.. image:: /_static/image/case_related.png
   :width: 700px
   :alt: Testcase Related Information
   :align: center
   :class: image

Testcase has an attribute Type, it also can be edited in |case_edit_type|.

.. image:: /_static/image/case_type.png
   :width: 700px
   :alt: Edit Type
   :align: center
   :class: image


1. Add. Click |new_btn| enter type name and save.
2. Modify. Select the type you want to modify, change type name, save it.
3. Delete. Select the type you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

You can edit Testcase and Subsystem by REST api, please refer to REST api - :ref:`api-case`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TestSuite
----------------

Testsuite Management page shows Testsuite information in Testsuite List, its filters are name and subsystem, performance
in |filter| page.

.. image:: /_static/image/suite.png
   :width: 700px
   :alt: Testsuite Management
   :align: center
   :class: image

Add Testsuite in |suite_new| page, enter Testsuite information then save it, in confirm dialog choose YES to create
Testsuite and NO to cancel. Click |delete| to discard the added Testsuite.

.. image:: /_static/image/suite_add.png
   :width: 700px
   :alt: Testsuite Management
   :align: center
   :class: image

Edit Testsuite by clicking item in Testsuite List.
In overview tab, update Testsuite information and save, while click |delete| to delete the Testsuite.

.. image:: /_static/image/suite_overview.png
   :width: 700px
   :alt: Modify Testsuite
   :align: center
   :class: image

Each Testsuite contains Testcase and belongs to one or more Testplan, they should have the same performance setting.
The association relationship between them can be changed.
In Related Testcase tab, Testcase column lists all Testcases with the same performance setting as this Testsuite,
Related Testcase column lists the related ones. Select the Testcases then click arrow button to set or cancel their
association relationship.

.. image:: /_static/image/suite_related_case.png
   :width: 700px
   :alt: Testsuite Related Information
   :align: center
   :class: image

In Related Testplan tab, Testplan column lists all Testplans with the same performance setting as this Testsuite,
Related Testplan column lists the related ones. Select the Testplans then click arrow button to set or cancel their
association relationship.

.. image:: /_static/image/suite_related_plan.png
   :width: 700px
   :alt: Testsuite Related Information
   :align: center
   :class: image

Testsuite has an attribute Subsystem, it also can be edited in |suite_edit_subsystem|

.. image:: /_static/image/suite_subsystem.png
   :width: 700px
   :alt: Edit Subsystem
   :align: center
   :class: image


1. Add. Click |new_btn| enter subsystem name and save.
2. Modify. Select the subsystem you want to modify, change subsystem name, save it.
3. Delete. Select the subsystem you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

You can edit Testsuite and Subsystem by REST api, please refer to REST api - :ref:`api-suite`.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TestPlan
----------------

Testplan List in Testplan Management page displays testplan information, and its filters are name and category,
performance in |filter| page.

.. image:: /_static/image/plan.png
   :width: 700px
   :alt: Testplan Management
   :align: center
   :class: image

Add Testplan in |plan_new| page, enter Testplan information then save it, in confirm dialog choose YES to create feature and
NO to cancel. Click |delete| to discard the added Testplan.

.. image:: /_static/image/plan_add.png
   :width: 700px
   :alt: Testplan Management
   :align: center
   :class: image

Edit Testplan by clicking item in Testplan List.
In overview tab, update Testplan information and save, while click |delete| to delete the Testplan.

.. image:: /_static/image/plan_overview.png
   :width: 700px
   :alt: Modify Testplan
   :align: center
   :class: image

Each Testplan has its related Testsuite, they should have the same performance setting. The association relationship
between Testplan and Testsuite can be changed. In Related Testsuite tab, Testsuite column lists all Testsuites with the
same performance setting as this Testplan, Related Testsuite column lists the related ones. Select the Testsuites then
click arrow button to set or cancel their association relationship.

.. image:: /_static/image/plan_related.png
   :width: 700px
   :alt: Testplan Related Information
   :align: center
   :class: image

Testplan has an attribute Category, it also can be edited in |plan_edit_category| page.

.. image:: /_static/image/category.png
   :width: 700px
   :alt: Edit Category
   :align: center
   :class: image

1. Add. Click |new_btn| enter category name and save.
2. Modify. Select the category you want to modify, change category name, save it.
3. Delete. Select the category you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

You can edit Testplan and Category by REST api, please refer to REST api - :ref:`api-plan`.

.. |case_new| image:: /_static/image/case_new.png
.. |filter| image:: /_static/image/filter.png
.. |case_edit_type| image:: /_static/image/case_edit_type.png
.. |new_btn| image:: /_static/image/new_btn.png
.. |delete| image:: /_static/image/delete_btn.png
.. |suite_edit_subsystem| image:: /_static/image/suite_edit_subsystem.png
.. |suite_new| image:: /_static/image/suite_new.png
.. |plan_edit_category| image:: /_static/image/plan_edit_category.png
.. |plan_new| image:: /_static/image/plan_new.png