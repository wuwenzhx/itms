Report Center
===============

In report management, test result is divided into two kinds according to testplan performance settings.

Function Report presents test result with performance is False, while the Performance Report shows test result with
performance is True.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Function Report
-----------------

Function Report Management lists testplans with performance is False in TestPlan List, and the filters are Category and
plan name. Click plan name in Testplan Lists will go to report page.

.. image:: /_static/image/function_report_new.png
   :width: 700px
   :alt: Function Report Management
   :align: center
   :class: image

Testplan category contains regular, undated, daily and other types, most of testplans are handled as regular testplan
but undated testplan. Here we will introduce function report in two ways - Regular and Undated.

Regular Report
^^^^^^^^^^^^^^^^^^^

The testplan belongs to regular generates an execution each time it is executed. Regular Test Report presents
all executions for the selected testplan by chart and table, the filters are OS and platform.


.. image:: /_static/image/regular_report.png
   :width: 700px
   :alt: Regular Report
   :align: center
   :class: image

Compare test results. In execution list, select executions that want to be compared, |compare| button will be activated
when more than one executions are selected. Click |compare| button to show Contrast Analysis Results list, it shows
cases with failed result or have different results.

.. image:: /_static/image/compare_result.png
   :width: 700px
   :alt: Regular Report
   :align: center
   :class: image

View an execution test result, click the execution name in the table to hide Contrast Analysis Results, and TestSuite
Results will be displayed with chart and table.

.. image:: /_static/image/exe_result.png
   :width: 700px
   :alt: Regular Report
   :align: center
   :class: image

For case result information, click number in the TestSuite Results. For example, click the Total Number for a suite,
TestCase Result shows all case results, if click the Pass Number for a suite, TestCase Result will
only list case result information with pass result.

.. image:: /_static/image/exe_case_result.png
   :width: 700px
   :alt: Regular Report
   :align: center
   :class: image

Undated Report
^^^^^^^^^^^^^^^^^

For the testplan with undated category, it can create only one execution. Undated Test Report page presents its suite
results in chart and table.

.. image:: /_static/image/undate_report.png
   :width: 700px
   :alt: Undated Report
   :align: center
   :class: image

For case result information, click number in the TestSuite Results. For example, click the Total Number for a suite,
TestCase Result shows all case results, if click the Pass Number for a suite, TestCase Result will
only list case result information with pass result.

.. image:: /_static/image/undate_case_result.png
   :width: 700px
   :alt: Undated Report
   :align: center
   :class: image

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Performance Report
--------------------

Performance Report Management lists testplans with performance is True in TestPlan List, and the filters are category,
app and name.

The result of performance test case is different from normal test case. Normal test case result should be one of pass,
fail, block, N/A and no run, but performance test case result is a value set. Performance test case has an app setting,
an app maps to a list of attributes, the value of each attribute compose a test result.

.. image:: /_static/image/perf_report_new.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

In performance testing, testplans of different categories have an uniform manner. Performance Test Report lists all
executions for selected testplan in a table, the filters are OS and platform.

.. image:: /_static/image/perf_test_report.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

Compare test results. Select more than one executions in above table, click |compare| button to show Contrast Analysis
Results.

.. image:: /_static/image/perf_compare.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

Contrast Analysis Results displays all attribute values of compared executions. Click case name will present case
results of compared executions in chart.

.. image:: /_static/image/perf_compare_result.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

View an execution test result, click the execution name in the table to hide Contrast Analysis Results, and show Test
Suite Results by chart and table.

.. image:: /_static/image/perf_suite_result.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

For case result information, click the suite name in TestSuite Results, test case results of selected suite show in
chart and table.

.. image:: /_static/image/perf_case_result.png
   :width: 700px
   :alt: Performance Report Management
   :align: center
   :class: image

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. role:: dpdk

:dpdk:`DPDK` Performance Report
-----------------------------------

DPDK Performance Report Management lists testplans with performance is True in TestPlan List, and the filters are
category, app and name.

The result of DPDK performance test case is different from other test case. DPDK Performance test case has an app
setting, an app maps to a list of attributes, the Packet Size(Bytes) attribute has several values, each Packet
Size(Bytes) value contains a group result, so DPDK test result with several group values.

.. image:: /_static/image/dpdk_testplan.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

DPDK Performance Test Report lists all executions for selected testplan in a table, the filters are OS and platform.

.. image:: /_static/image/dpdk_report.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

Compare test results. Select more than one executions in above table, click |compare| button to show Contrast Analysis
Results.

.. image:: /_static/image/dpdk_compare.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

Contrast Analysis Results displays Packet Size(Bytes) values of compared executions. Click case name will present case
results of compared executions in chart.

.. image:: /_static/image/dpdk_compare_result.png
   :width: 700px
   :alt:  DPDK Performance Report Management
   :align: center
   :class: image

View an execution test result, click the execution name in the table to hide Contrast Analysis Results, and show Test
Suite Results by table.

.. image:: /_static/image/dpdk_suite.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

For case result information, click the suite name in TestSuite Results, test case results of selected suite will be
shown in table.

.. image:: /_static/image/dpdk_case.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

For detail result, click the case name in Testcase Results, detail results of selected case displayed in chart and
table.

.. image:: /_static/image/dpdk_case_detail.png
   :width: 700px
   :alt: DPDK Performance Report Management
   :align: center
   :class: image

.. note:: This section is only for project DPDK.


.. |compare| image:: /_static/image/compare.png