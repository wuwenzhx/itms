from rest_framework import serializers
from base_models.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')

class RwMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rw_method
        fields = ('id','rw_method')

class Queue_depthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue_depth
        fields = ('id','queue_depth')

class io_sizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = io_size
        fields = ('id','io_size')

class RequirementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('id', 'name', 'create_time', 'owner',
                  'type', 'description')


class FeatureComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'name')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'name', 'create_time', 'owner', 'component',
                  'description', 'requirement')


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name')


class AppAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppAttr
        fields = ('id', 'name', 'app')


class TestPlanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TestPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlan
        fields = ('id', 'name', 'rw', 'io_size', 'queue_depth',
                  'owner', 'create_time', 'description', 'del_flag')


class TestsuiteSubsystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsystem
        fields = ('id', 'name')


class TestsuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = ('id', 'name', 'subsystem', 'performance', 'app',
                  'description', 'testplan')


class TestcaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseType
        fields = ('id', 'name')


class TestcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ('id', 'name', 'type', 'description', 'script_path',
                  'config_path', 'parameters', 'feature', 'testsuite',
                  'performance', 'app')


class TestexecutionOsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = ('id', 'name')


class TestexecutionPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'name')


class TestexecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestExecution
        fields = ('id', 'name','rw','io_size','queue_depth', 'time',
                  'runner', 'testplan','environment')


#class TestsuiteResultSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = TestSuiteResult
#        fields = ('id', 'testexecution', 'testsuite', 'passed', 'failed',
#                  'block', 'na', 'total', 'time')
class TestsuiteResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuiteResult
        fields = ('id', 'testexecution', 'testsuite', 'passed', 'failed',
                  'block', 'na', 'total', 'time')


class TestsuitePerfResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfTestSuiteResult
        fields = ('id', 'testexecution', 'testsuite', 'app')


class TestcaseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseResult
        fields = ('id', 'testcase', 'testsuite_result', 'result', 'bug',
                  'log', 'comments')


class PerTestcaseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfTestCaseResult
        fields = ('id', 'testcase', 'perf_testsuite_result', 'bug',
                  'log', 'comments')


class PerTestcaseResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfTestCaseResultDetail
        fields = ('id', 'perf_testcase_result', 'key', 'value','app') 
class PerDPDKTestCaseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfDPDKTestCaseResult
        fields = ('id', 'testcase', 'perf_testsuite_result', 'bug', 'log', 'comments')


class PerDPDKTestcaseResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfDPDKTestCaseResultDetail
        fields = ('id', 'perf_dpdk_testcase_result', 'key', 'value', 'app', 'group')



####### define API database structure############
#class TestsuiteResultSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = TestSuiteResult
#        fields = ('id', 'testexecution', 'testsuite', 'passed', 'failed',
#                  'block', 'na', 'total', 'time')


class MySuiteResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySuiteResult
        fields = ('id', 'testexecution', 'testsuite', 'zero_loss_throughput','zero_loss_rate','time')


class NicPerfResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicPerfTable
        fields = ('id','create_time','frame_size','thoughput','send_rate','expected_thoughput')

class NicPerfTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicPerfTable
        fields = ('id','create_time','frame_size','thoughput','send_rate','expected_thoughput')

class TestRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRecordTable
        fields = ('id','case_name','case_type','create_time','branch_commit_id','commit_info','test_command','board_name','cpu_info','memory_info','nic_name','device','firmware','distro_info','kernel_info','gcc_info')


##################################

class DpdkTestRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DpdkTestRecordTable
        fields = ('case_name','case_type','create_time','branch_commit_id','commit_info','test_command','board_name','cpu_info','memory_info','nic_name','device','firmware','distro_info','kernel_info','gcc_info')

###################################

class SingleCorePerfTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleCorePerfTable
        fields =('create_time','frame_size','thoughput','send_rate','cpu_freq','per_packet_cycle','expected_thoughput')

class NicNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NicName
        fields  =('id','name')

class CpuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuType
        fields = ('id','cpu_type')

class FirmwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields =('id','firmware')

class CaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseType
        fields =('id','case_type')

class DeviceIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields=('id','device_id')

class SpdkPerfResultSerializer(serializers.ModelSerializer):
    class Meta:
	model = Spdk_Perf_Result
	fields=('id','iops','latency','case_type','testexecution','create_time','rw_method','queue_depth','io_size')

class SpdkTrendResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpdkAvgTrendTable
	fields=('id','trend_iops','trend_latency','testexecution','create_time','rw_method','queue_depth','io_size')
        
#class VhostScsiPerfSerializer(serializers.ModelSerializer):
#    class Meta:
#	model = Vhost_Scsi_Perf_Result
#	fields=('id','iops','latency','case_type','testexecution','create_time','rw_method','queue_depth','io_size')

class VhostScsiTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vhost_Scsi_Trend_Table
	fields=('id','trend_iops','trend_latency','testexecution','create_time','rw_method','queue_depth','io_size')
        
class NvmeDriverTrendResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NvmeDriverTrendTable
	fields=('id','trend_iops','trend_latency','MBps','testexecution','create_time','rw_method','queue_depth','workload_mix','Core_Mask','run_time','Average_lat','Min_lat','Max_lat','io_size')




