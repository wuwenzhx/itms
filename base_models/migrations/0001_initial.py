# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('test_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'base_models', ['Person'])

        # Adding model 'Project'
        db.create_table('itms_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reader_group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('writer_group', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'base_models', ['Project'])

        # Adding model 'Type'
        db.create_table('itms_requirement_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Type'])

        # Adding model 'Requirement'
        db.create_table('itms_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Type'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Requirement'])

        # Adding model 'Component'
        db.create_table('itms_feature_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Component'])

        # Adding model 'Feature'
        db.create_table('itms_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('component', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Component'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('requirement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Requirement'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Feature'])

        # Adding model 'App'
        db.create_table('itms_perf_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['App'])

        # Adding model 'AppAttr'
        db.create_table('itms_perf_appattr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['AppAttr'])

        # Adding model 'Category'
        db.create_table('itms_testplan_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Category'])

        # Adding model 'TestPlan'
        db.create_table('itms_testplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Category'], null=True, blank=True)),
            ('performance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'], null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
            ('del_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'base_models', ['TestPlan'])

        # Adding model 'Subsystem'
        db.create_table('itms_testsuite_subsystem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Subsystem'])

        # Adding model 'TestSuite'
        db.create_table('itms_testsuite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subsystem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Subsystem'], null=True, blank=True)),
            ('performance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
            ('del_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'base_models', ['TestSuite'])

        # Adding M2M table for field testplan on 'TestSuite'
        m2m_table_name = db.shorten_name('itms_testsuite_testplan')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('testsuite', models.ForeignKey(orm[u'base_models.testsuite'], null=False)),
            ('testplan', models.ForeignKey(orm[u'base_models.testplan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['testsuite_id', 'testplan_id'])

        # Adding model 'TestCaseType'
        db.create_table('itms_testcase_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['TestCaseType'])

        # Adding model 'TestCase'
        db.create_table('itms_testcase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestCaseType'], null=True, blank=True)),
            ('performance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('script_path', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('config_path', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('parameters', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Feature'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
            ('del_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'base_models', ['TestCase'])

        # Adding M2M table for field testsuite on 'TestCase'
        m2m_table_name = db.shorten_name('itms_testcase_testsuite')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('testcase', models.ForeignKey(orm[u'base_models.testcase'], null=False)),
            ('testsuite', models.ForeignKey(orm[u'base_models.testsuite'], null=False))
        ))
        db.create_unique(m2m_table_name, ['testcase_id', 'testsuite_id'])

        # Adding model 'OS'
        db.create_table('itms_os', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['OS'])

        # Adding model 'Platform'
        db.create_table('itms_platform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Platform'])

        # Adding model 'iTEC'
        db.create_table('itms_itec', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['iTEC'])

        # Adding model 'EnvironmentType'
        db.create_table('itms_env_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['EnvironmentType'])

        # Adding model 'Environment'
        db.create_table('itms_environment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('testplan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestPlan'])),
            ('itec', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.iTEC'])),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('worker', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('env_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.EnvironmentType'])),
            ('schedule', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('runtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('git_repo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('patch', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('commit_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('package', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('is_invalid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Environment'])

        # Adding model 'Configuration'
        db.create_table('itms_config', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('env', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Environment'])),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('kernel', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('gcc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nic', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('test_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('driver', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['Configuration'])

        # Adding model 'TestExecution'
        db.create_table('itms_testexecution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('os', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.OS'], null=True, blank=True)),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Platform'], null=True, blank=True)),
            ('performance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('runner', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('testplan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestPlan'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Environment'], null=True, blank=True)),
        ))
        db.send_create_signal(u'base_models', ['TestExecution'])

        # Adding model 'TestSuiteResult'
        db.create_table('itms_testsuite_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testexecution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestExecution'])),
            ('testsuite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestSuite'])),
            ('passed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('failed', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('block', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('na', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_run', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['TestSuiteResult'])

        # Adding model 'PerfTestSuiteResult'
        db.create_table('itms_perf_testsuite_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testexecution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestExecution'])),
            ('testsuite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestSuite'])),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['PerfTestSuiteResult'])

        # Adding model 'TestCaseResult'
        db.create_table('itms_testcase_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testcase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestCase'])),
            ('testsuite_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestSuiteResult'])),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bug', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('log', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['TestCaseResult'])

        # Adding model 'PerfTestCaseResult'
        db.create_table('itms_perf_testcase_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testcase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestCase'])),
            ('perf_testsuite_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.PerfTestSuiteResult'])),
            ('bug', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('log', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['PerfTestCaseResult'])

        # Adding model 'PerfTestCaseResultDetail'
        db.create_table('itms_perf_testcase_result_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('perf_testcase_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.PerfTestCaseResult'])),
            ('key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.AppAttr'])),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['PerfTestCaseResultDetail'])

        # Adding model 'PerfDPDKTestCaseResult'
        db.create_table('itms_perf_dpdk_testcase_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testcase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestCase'])),
            ('perf_testsuite_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.PerfTestSuiteResult'])),
            ('bug', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('log', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['PerfDPDKTestCaseResult'])

        # Adding model 'PerfDPDKTestCaseResultDetail'
        db.create_table('itms_perf_dpdk_testcase_result_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('perf_dpdk_testcase_result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.PerfDPDKTestCaseResult'])),
            ('key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.AppAttr'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.App'])),
            ('group', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['PerfDPDKTestCaseResultDetail'])

        # Adding model 'MySuiteResult'
        db.create_table('itms_mysuite_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testexecution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestExecution'])),
            ('testsuite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.TestSuite'])),
            ('zero_loss_throughput', self.gf('django.db.models.fields.FloatField')()),
            ('zero_loss_rate', self.gf('django.db.models.fields.FloatField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base_models.Project'])),
        ))
        db.send_create_signal(u'base_models', ['MySuiteResult'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('test_person')

        # Deleting model 'Project'
        db.delete_table('itms_project')

        # Deleting model 'Type'
        db.delete_table('itms_requirement_type')

        # Deleting model 'Requirement'
        db.delete_table('itms_requirement')

        # Deleting model 'Component'
        db.delete_table('itms_feature_component')

        # Deleting model 'Feature'
        db.delete_table('itms_feature')

        # Deleting model 'App'
        db.delete_table('itms_perf_app')

        # Deleting model 'AppAttr'
        db.delete_table('itms_perf_appattr')

        # Deleting model 'Category'
        db.delete_table('itms_testplan_category')

        # Deleting model 'TestPlan'
        db.delete_table('itms_testplan')

        # Deleting model 'Subsystem'
        db.delete_table('itms_testsuite_subsystem')

        # Deleting model 'TestSuite'
        db.delete_table('itms_testsuite')

        # Removing M2M table for field testplan on 'TestSuite'
        db.delete_table(db.shorten_name('itms_testsuite_testplan'))

        # Deleting model 'TestCaseType'
        db.delete_table('itms_testcase_type')

        # Deleting model 'TestCase'
        db.delete_table('itms_testcase')

        # Removing M2M table for field testsuite on 'TestCase'
        db.delete_table(db.shorten_name('itms_testcase_testsuite'))

        # Deleting model 'OS'
        db.delete_table('itms_os')

        # Deleting model 'Platform'
        db.delete_table('itms_platform')

        # Deleting model 'iTEC'
        db.delete_table('itms_itec')

        # Deleting model 'EnvironmentType'
        db.delete_table('itms_env_type')

        # Deleting model 'Environment'
        db.delete_table('itms_environment')

        # Deleting model 'Configuration'
        db.delete_table('itms_config')

        # Deleting model 'TestExecution'
        db.delete_table('itms_testexecution')

        # Deleting model 'TestSuiteResult'
        db.delete_table('itms_testsuite_result')

        # Deleting model 'PerfTestSuiteResult'
        db.delete_table('itms_perf_testsuite_result')

        # Deleting model 'TestCaseResult'
        db.delete_table('itms_testcase_result')

        # Deleting model 'PerfTestCaseResult'
        db.delete_table('itms_perf_testcase_result')

        # Deleting model 'PerfTestCaseResultDetail'
        db.delete_table('itms_perf_testcase_result_detail')

        # Deleting model 'PerfDPDKTestCaseResult'
        db.delete_table('itms_perf_dpdk_testcase_result')

        # Deleting model 'PerfDPDKTestCaseResultDetail'
        db.delete_table('itms_perf_dpdk_testcase_result_detail')

        # Deleting model 'MySuiteResult'
        db.delete_table('itms_mysuite_result')


    models = {
        u'base_models.app': {
            'Meta': {'object_name': 'App', 'db_table': "'itms_perf_app'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.appattr': {
            'Meta': {'object_name': 'AppAttr', 'db_table': "'itms_perf_appattr'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'itms_testplan_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.component': {
            'Meta': {'object_name': 'Component', 'db_table': "'itms_feature_component'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.configuration': {
            'Meta': {'object_name': 'Configuration', 'db_table': "'itms_config'"},
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'env': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Environment']"}),
            'gcc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kernel': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nic': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'test_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'base_models.environment': {
            'Meta': {'object_name': 'Environment', 'db_table': "'itms_environment'"},
            'commit_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'env_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.EnvironmentType']"}),
            'git_repo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_invalid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itec': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.iTEC']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'patch': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'runtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'testplan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestPlan']"}),
            'worker': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'base_models.environmenttype': {
            'Meta': {'object_name': 'EnvironmentType', 'db_table': "'itms_env_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.feature': {
            'Meta': {'object_name': 'Feature', 'db_table': "'itms_feature'"},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Component']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'requirement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Requirement']", 'null': 'True', 'blank': 'True'})
        },
        u'base_models.itec': {
            'Meta': {'object_name': 'iTEC', 'db_table': "'itms_itec'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.mysuiteresult': {
            'Meta': {'object_name': 'MySuiteResult', 'db_table': "'itms_mysuite_result'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'testexecution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestExecution']"}),
            'testsuite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestSuite']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'zero_loss_rate': ('django.db.models.fields.FloatField', [], {}),
            'zero_loss_throughput': ('django.db.models.fields.FloatField', [], {})
        },
        u'base_models.os': {
            'Meta': {'object_name': 'OS', 'db_table': "'itms_os'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.perfdpdktestcaseresult': {
            'Meta': {'object_name': 'PerfDPDKTestCaseResult', 'db_table': "'itms_perf_dpdk_testcase_result'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            'bug': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'perf_testsuite_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.PerfTestSuiteResult']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'testcase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestCase']"})
        },
        u'base_models.perfdpdktestcaseresultdetail': {
            'Meta': {'object_name': 'PerfDPDKTestCaseResultDetail', 'db_table': "'itms_perf_dpdk_testcase_result_detail'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            'group': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.AppAttr']"}),
            'perf_dpdk_testcase_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.PerfDPDKTestCaseResult']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'base_models.perftestcaseresult': {
            'Meta': {'object_name': 'PerfTestCaseResult', 'db_table': "'itms_perf_testcase_result'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            'bug': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'perf_testsuite_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.PerfTestSuiteResult']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'testcase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestCase']"})
        },
        u'base_models.perftestcaseresultdetail': {
            'Meta': {'object_name': 'PerfTestCaseResultDetail', 'db_table': "'itms_perf_testcase_result_detail'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.AppAttr']"}),
            'perf_testcase_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.PerfTestCaseResult']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'base_models.perftestsuiteresult': {
            'Meta': {'object_name': 'PerfTestSuiteResult', 'db_table': "'itms_perf_testsuite_result'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'testexecution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestExecution']"}),
            'testsuite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestSuite']"})
        },
        u'base_models.person': {
            'Meta': {'object_name': 'Person', 'db_table': "'test_person'"},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'base_models.platform': {
            'Meta': {'object_name': 'Platform', 'db_table': "'itms_platform'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.project': {
            'Meta': {'object_name': 'Project', 'db_table': "'itms_project'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reader_group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'writer_group': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'base_models.requirement': {
            'Meta': {'object_name': 'Requirement', 'db_table': "'itms_requirement'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Type']", 'null': 'True', 'blank': 'True'})
        },
        u'base_models.subsystem': {
            'Meta': {'object_name': 'Subsystem', 'db_table': "'itms_testsuite_subsystem'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.testcase': {
            'Meta': {'object_name': 'TestCase', 'db_table': "'itms_testcase'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']", 'null': 'True', 'blank': 'True'}),
            'config_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'del_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Feature']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parameters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'performance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'script_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'testsuite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base_models.TestSuite']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestCaseType']", 'null': 'True', 'blank': 'True'})
        },
        u'base_models.testcaseresult': {
            'Meta': {'object_name': 'TestCaseResult', 'db_table': "'itms_testcase_result'"},
            'bug': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'testcase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestCase']"}),
            'testsuite_result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestSuiteResult']"})
        },
        u'base_models.testcasetype': {
            'Meta': {'object_name': 'TestCaseType', 'db_table': "'itms_testcase_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        },
        u'base_models.testexecution': {
            'Meta': {'object_name': 'TestExecution', 'db_table': "'itms_testexecution'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']", 'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Environment']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'os': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.OS']", 'null': 'True', 'blank': 'True'}),
            'performance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Platform']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'runner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'testplan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestPlan']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'base_models.testplan': {
            'Meta': {'object_name': 'TestPlan', 'db_table': "'itms_testplan'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Category']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'del_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'performance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'base_models.testsuite': {
            'Meta': {'object_name': 'TestSuite', 'db_table': "'itms_testsuite'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.App']", 'null': 'True', 'blank': 'True'}),
            'del_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'performance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'subsystem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Subsystem']", 'null': 'True', 'blank': 'True'}),
            'testplan': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base_models.TestPlan']", 'null': 'True', 'blank': 'True'})
        },
        u'base_models.testsuiteresult': {
            'Meta': {'object_name': 'TestSuiteResult', 'db_table': "'itms_testsuite_result'"},
            'block': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'failed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'na': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'no_run': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'passed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"}),
            'testexecution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestExecution']"}),
            'testsuite': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.TestSuite']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'base_models.type': {
            'Meta': {'object_name': 'Type', 'db_table': "'itms_requirement_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base_models.Project']"})
        }
    }

    complete_apps = ['base_models']