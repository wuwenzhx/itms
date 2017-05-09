Config Center
==============

ConfigCenter section is focus on the operations of requirement, feature and performance 
setting.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirement
----------------

Requirement Management page lists the operation tabs and the basic information of requirements. Its filters are name and
requirement type in |filter| page.

.. image:: /_static/image/req.png
   :width: 700px
   :alt: Add Requirement
   :align: center
   :class: image

Add requirement in |req_add_btn| page, enter requirement information then save it, in confirm dialog choose YES to
create requirement and NO to cancel. Click |delete| to discard the added requirement.

.. image:: /_static/image/req_add.png
   :width: 700px
   :alt: Add Requirement
   :align: center
   :class: image

Edit requirement by clicking item in Requirement List.
In overview tab, update requirement information and save,
while click |delete| to delete the requirement.

.. image:: /_static/image/req_overview.png
   :width: 700px
   :alt: Add Requirement
   :align: center
   :class: image

In Related Feature tab, we can add/remove its related features.

.. image:: /_static/image/req_related.png
   :width: 700px
   :alt: Add Requirement
   :align: center
   :class: image

Requirement has an attribute Type, it also can be edited in |req_edit_type|.

.. image:: /_static/image/req_type.png
   :width: 700px
   :alt: Edit Requirement Type
   :align: center
   :class: image

1. Add. Click |new_btn| enter type name and save.
2. Modify. Select the type you want to modify, change type name, save it.
3. Delete. Select the type you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

You can edit Requirement and Type by REST api, please refer to REST api - :ref:`api-req`.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Feature
----------------

Feature List in Feature Management page displays feature information, and its filters are name and component,
requirement in |filter| page.

.. image:: /_static/image/fea.png
   :width: 700px
   :alt: Delete Requirement
   :align: center
   :class: image

Add feature in |fea_new| page, enter Feature information then save it, in confirm dialog choose YES to create feature and
NO to cancel. Click |delete| to discard the added feature.

.. image:: /_static/image/fea_add.png
   :width: 700px
   :alt: Add Feature
   :align: center
   :class: image

Edit feature by clicking item in Feature List.
In overview tab, update feature information and save, while click
|delete| to delete the feature.

.. image:: /_static/image/fea_overview.png
   :width: 700px
   :alt: Modify Feature
   :align: center
   :class: image

In Related Testcase tab, we can add/remove its related testcases.

.. image:: /_static/image/req_related.png
   :width: 700px
   :alt: Delete Feature
   :align: center
   :class: image


Feature has an attribute Component, it also can be edited in |fea_edit_component|.

.. image:: /_static/image/fea_component.png
   :width: 700px
   :alt: Edit Component
   :align: center
   :class: image

1. Add. Click |new_btn| enter component name and save.
2. Modify. Select the component you want to modify, change component name, save it.
3. Delete. Select the component you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

You can edit Feature and Component by REST api, please refer to REST api - :ref:`api-fea`.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Performance Setting
---------------------

In performance testing, we can set an app for test elements, and each app has its own attributes.
This section describe edit app and its attributes in App Management page.


.. image:: /_static/image/app.png
   :width: 700px
   :alt: APP Management
   :align: center
   :class: image


Add an App in |app_new| page. Enter app name and save it.

.. image:: /_static/image/app_add.png
   :width: 700px
   :alt: APP Information
   :align: center
   :class: image

Edit App by clicking item in App List.
In overview tab, update App information and save, while click |delete| to delete the App.

.. image:: /_static/image/app_overview.png
   :width: 700px
   :alt: APP Information
   :align: center
   :class: image

Each App has its attributes, we can edit the attributes in App Attribute tab.

.. image:: /_static/image/app_attr_edit.png
   :width: 700px
   :alt: APP Information
   :align: center
   :class: image

1. Add. Click |add_btn| enter attribute name.
2. Modify. Select the attribute you want to modify, change attribute name, save it.
3. Delete. Select the attribute you want to delete, click Delete button, in confirm dialog choose YES to
   delete and NO to cancel.

.. note:: We cannot delete an App or attribute in use.

You can edit App and App attribute by REST api, please refer to REST api - :ref:`api-app`.


.. |save| image:: /_static/image/save_btn.png
.. |delete| image:: /_static/image/delete_btn.png
.. |req_add_btn| image:: /_static/image/req_add_btn.png
.. |req_edit_type| image:: /_static/image/req_edit_type.png
.. |new_btn| image:: /_static/image/new_btn.png
.. |filter| image:: /_static/image/filter.png
.. |fea_new| image:: /_static/image/fea_new.png
.. |fea_edit_component| image:: /_static/image/fea_edit_component.png
.. |app_new| image:: /_static/image/app_new.png
.. |add_btn| image:: /_static/image/add_btn.png
