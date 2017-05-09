Release Notes
==============

The changes in each release are always covered in this section.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.7.0
--------------

In this release, we changed the page layout and style of iTMS.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.6.0
--------------

This release covered DPDK performance test related feature.

1. Add DPDK performance test report.

    a. Support the result of the comparison by table and chart.
    b. Support the result of each execution.

2. Add DPDK performance test related API:

    * PerfDPDKTestSuiteResultTestCaseResult api
    * PerfDPDKTestcaseResultTestcaseDetailResult api
    * PerfDPDKTestCaseResult api
    * PerfDPDKTestCaseResultDetail api
    * PerfDPDKTestCaseResultDetail api

3. Update readme_api.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.5.3
--------------

This release have added new feature - readme online help.

The help link was in iTMS header, click |help| to load readme online help page.

.. note:: Please clear the browser cache before loading iTMS.


.. |help| image:: /_static/image/help.png

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.5.2
--------------

1. Enable to delete used testcase, testsuite, testplan.
2. Improve the user experience.

    a. Stay on the current page after delete and modify testcase, testsuite, testplan, feature, requirement.
    b. Turn to the first page after add new testcase, testsuite, testplan, feature, requirement.

~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.5.1
----------

This release cover the new features, as well as revision, we have also dropped two features.

1. Modify chart legend.
2. Add feature filter for testcase table in testsuite page.
3. Sort testcase, testsuite, testplan, feature, requirement.
4. Add testcase result chart in performance test report.
5. Enable to resize  table column width.
6. Improve report for show history data compare.
7. Update iTMs menu list.
8. Support multiple executions to compare for function report.
9. Add testcase total number info in execution table for test performanc report.
10. Add run case number/no run case number/case total number in testsuite results table for test performance report.
11. Modify chart bar width for function report.
12. Add log, bug, comments in testcase results table for test performance report.
13. Update api and readme_api:

    * delete TestcaseResult / PerfTestCaseResult's post and delete function.
    * add PerfTestSuiteResultTestCaseResult api.
    * add PerfTestcaseResultTestcaseDetailResult api.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v_1.5.0
-------------

We have added following features in this release.

1. Enable performance test report.

    a. Support the result of the comparison by table and chart.
    b. Support summary info of test execution.

2. Add performance test related API.
3. Add App attribute related configuration.