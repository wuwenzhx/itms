from django.db import models


class Person(models.Model):
    GENDER_CHOICES = {
        (u'M', u'Male'),
        (u'F', u'Female'),
    }
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_person'


class Project(models.Model):
    name = models.CharField(max_length=50)
    reader_group = models.CharField(max_length=200)
    writer_group = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_project'


class Type(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_requirement_type'


class Requirement(models.Model):
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(Type, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_requirement'


class Component(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_feature_component'
#########################################
class Rw_method(models.Model):
    rw_method = models.CharField(max_length=50)
    project=models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'fio_rw'


class Queue_depth(models.Model):
    queue_depth= models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'fio_queue_depth'

class io_size(models.Model):
    io_size=models.CharField(max_length=50)
    project=models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'io_size'
###############################################
class Feature(models.Model):
    name = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    component = models.ForeignKey(Component, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirement = models.ForeignKey(Requirement, blank=True, null=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_feature'


class App(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_perf_app'


class AppAttr(models.Model):
    name = models.CharField(max_length=50)
    app = models.ForeignKey(App)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_perf_appattr'


class Category(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testplan_category'


class TestPlan(models.Model):
    name = models.CharField(max_length=200)
    rw = models.ForeignKey(Rw_method)
    io_size=models.ForeignKey(io_size)
    queue_depth=models.ForeignKey(Queue_depth)
    owner = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testplan'


class Subsystem(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testsuite_subsystem'


class TestSuite(models.Model):
    name = models.CharField(max_length=200)
    subsystem = models.ForeignKey(Subsystem, blank=True, null=True)
    performance = models.BooleanField(default=False)
    app = models.ForeignKey(App, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    testplan = models.ManyToManyField(TestPlan, blank=True, null=True)
    project = models.ForeignKey(Project)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testsuite'


class TestCaseType(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testcase_type'


class TestCase(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(TestCaseType, blank=True, null=True)
    performance = models.BooleanField(default=False)
    app = models.ForeignKey(App, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    script_path = models.CharField(max_length=200, blank=True, null=True)
    config_path = models.CharField(max_length=200, blank=True, null=True)
    parameters = models.CharField(max_length=200, blank=True, null=True)
    feature = models.ForeignKey(Feature, blank=True, null=True)
    testsuite = models.ManyToManyField(TestSuite, blank=True, null=True)
    project = models.ForeignKey(Project)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testcase'


class OS(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_os'


class Platform(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_platform'


class iTEC(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=20)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_itec'


class EnvironmentType(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_env_type'


class Environment(models.Model):
    name = models.CharField(max_length=200)
    testplan = models.ForeignKey(TestPlan)
    itec = models.ForeignKey(iTEC)
    owner = models.CharField(max_length=100, blank=True, null=True)
    worker = models.CharField(max_length=200, blank=True)
    env_type = models.ForeignKey(EnvironmentType)
    schedule = models.CharField(max_length=200, blank=True, null=True)
    runtime = models.TimeField(blank=True, null=True)
    git_repo = models.CharField(max_length=200, blank=True, null=True)
    patch = models.FileField(upload_to='files',  blank=True, null=True)
    commit_id = models.CharField(max_length=200, blank=True, null=True)
    package = models.CharField(max_length=200, blank=True, null=True)
    is_invalid = models.BooleanField(default=False)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_environment'


class Configuration(models.Model):
    env = models.ForeignKey(Environment)
    os = models.CharField(max_length=200)
    kernel = models.CharField(max_length=200)
    gcc = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    nic = models.CharField(max_length=200)
    test_type = models.CharField(max_length=200)
    driver = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_config'


class TestExecution(models.Model):
    name = models.CharField(max_length=200)
    #os = models.ForeignKey(OS, blank=True, null=True)
    #platform = models.ForeignKey(Platform, blank=True, null=True)
    #performance = models.BooleanField(default=False)
    #app = models.ForeignKey(App, blank=True, null=True)
    rw = models.ForeignKey(Rw_method)
    io_size=models.ForeignKey(io_size)
    queue_depth=models.ForeignKey(Queue_depth)
    time = models.DateTimeField(auto_now_add=True)
    runner = models.CharField(max_length=100)
    testplan = models.ForeignKey(TestPlan)
    project = models.ForeignKey(Project)
    environment = models.ForeignKey(Environment, blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_testexecution'


class TestSuiteResult(models.Model):
    testexecution = models.ForeignKey(TestExecution)
    testsuite = models.ForeignKey(TestSuite)
    passed = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)
    #thoughput = models.FloatField(default=0)
    #lossrate = models.FloatField(default=0)
    block = models.IntegerField(default=0)
    na = models.IntegerField(default=0)
    no_run = models.IntegerField(default=0)
    total = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_testsuite_result'
        #db_table = 'itms_mydpdk_result'


class PerfTestSuiteResult(models.Model):
    testexecution = models.ForeignKey(TestExecution)
    testsuite = models.ForeignKey(TestSuite)
    app = models.ForeignKey(App)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_perf_testsuite_result'


class TestCaseResult(models.Model):
    testcase = models.ForeignKey(TestCase)
    testsuite_result = models.ForeignKey(TestSuiteResult)
    result = models.CharField(max_length=50)
    bug = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_testcase_result'


class PerfTestCaseResult(models.Model):
    testcase = models.ForeignKey(TestCase)
    perf_testsuite_result = models.ForeignKey(PerfTestSuiteResult)
    bug = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    app = models.ForeignKey(App)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_perf_testcase_result'


class PerfTestCaseResultDetail(models.Model):
    perf_testcase_result = models.ForeignKey(PerfTestCaseResult)
    key = models.ForeignKey(AppAttr)
    value = models.FloatField(default=0, blank=True, null=True)
    app = models.ForeignKey(App)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_perf_testcase_result_detail'


class PerfDPDKTestCaseResult(models.Model):
    testcase = models.ForeignKey(TestCase)
    perf_testsuite_result = models.ForeignKey(PerfTestSuiteResult)
    bug = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    app = models.ForeignKey(App)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_perf_dpdk_testcase_result'


class PerfDPDKTestCaseResultDetail(models.Model):
    perf_dpdk_testcase_result = models.ForeignKey(PerfDPDKTestCaseResult)
    key = models.ForeignKey(AppAttr)
    value = models.CharField(max_length=50, blank=True, null=True)
    app = models.ForeignKey(App)
    group = models.IntegerField()
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_perf_dpdk_testcase_result_detail'



class MySuiteResult(models.Model):
    testexecution = models.ForeignKey(TestExecution)
    testsuite = models.ForeignKey(TestSuite)
    zero_loss_throughput= models.FloatField()
    zero_loss_rate= models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'itms_mysuite_result'


class NicName(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'itms_nic_name'

class TimeRecordTable(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,primary_key=True)
    Project = models.ForeignKey(Project)
    def __str__(self):
	return self.id
    class Meta:
	db_table = 'Time_record_table'

class CpuType(models.Model):
    cpu_type = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'cpu_type_table'

class Firmware(models.Model):
    firmware = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'firmware_table'


class DeviceId(models.Model):
    device_id = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'device_id_table'


class CaseType(models.Model):
    case_type = models.CharField(max_length=50)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'case_type_table'
class TestRecordTable(models.Model):
    case_name = models.CharField(max_length=50)
    case_type = models.ForeignKey(CaseType)
    create_time = models.DateTimeField(auto_now_add=True)
    branch_commit_id = models.CharField(max_length=60)
    commit_info = models.TextField(blank=True,null=True)
    test_command = models.TextField(blank=True,null=True)
    board_name = models.CharField(max_length=100)
    cpu_info = models.ForeignKey(CpuType)
    memory_info = models.CharField(max_length=100)
    nic_name = models.ForeignKey(NicName)
    device = models.ForeignKey(DeviceId)
    firmware = models.ForeignKey(Firmware)
    distro_info = models.CharField(max_length=30)
    kernel_info = models.CharField(max_length=30)
    gcc_info = models.CharField(max_length=30)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'test_record_table'

class DpdkTestRecordTable(models.Model):
    case_name = models.CharField(max_length=50)
    case_type = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True,primary_key=True)
    branch_commit_id = models.CharField(max_length=60)
    commit_info = models.TextField(blank=True,null=True)
    test_command = models.TextField(blank=True,null=True)
    board_name = models.CharField(max_length=100)
    cpu_info = models.CharField(max_length=50)
    memory_info = models.CharField(max_length=100)
    nic_name = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    firmware = models.CharField(max_length=50)
    distro_info = models.CharField(max_length=30)
    kernel_info = models.CharField(max_length=30)
    gcc_info = models.CharField(max_length=30)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'dpdk_test_record_table'



class NicPerfTable(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    frame_size =models.IntegerField(default=0,blank=True,null=True)
    thoughput = models.FloatField(default=0,blank=True,null=True)
    send_rate = models.FloatField(default=0,blank=True,null=True)
    expected_thoughput=models.FloatField(default=0,blank=True,null=True)
    project = models.ForeignKey(Project)
	
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'nic_record_table'

  
class SingleCorePerfTable(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,primary_key=True)
    frame_size = models.IntegerField(default=0,blank=True,null=True)
    thoughput = models.FloatField(default=0,blank=True,null=True)
    send_rate = models.FloatField(default=0,blank=True,null=True)
    cpu_freq = models.FloatField(default=0,blank=True,null=True)
    per_packet_cycle = models.IntegerField(default=0,blank=True,null=True)
    expected_thoughput = models.FloatField(default=0,blank=True,null=True)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'singlecore_record_table'

class SpdkAvgTrendTable(models.Model):
    trend_iops = models.FloatField(default=0,blank=True,null=True)
    trend_latency = models.FloatField(default=0,blank=True,null=True)
    testexecution = models.ForeignKey(TestExecution)
    create_time = models.DateTimeField(auto_now_add=True)
    rw_method = models.ForeignKey(Rw_method)
    queue_depth = models.ForeignKey(Queue_depth)
    io_size = models.ForeignKey(io_size)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'spdk_trend_result'


class NvmeDriverTrendTable(models.Model):
    trend_iops = models.FloatField(default=0,blank=True,null=True)
    trend_latency = models.FloatField(default=0,blank=True,null=True)
    MBps = models.FloatField(default=0,blank=True,null=True)
    testexecution = models.ForeignKey(TestExecution)
    create_time = models.DateTimeField(auto_now_add=True)
    rw_method = models.ForeignKey(Rw_method)
    workload_mix = models.FloatField(default=50,blank=True,null=True)
    Core_Mask = models.CharField(max_length=30,blank=True)
    run_time = models.FloatField(default=0,blank=True,null=True)
    Average_lat = models.FloatField(default=0,blank=True,null=True)
    Min_lat = models.FloatField(default=0,blank=True,null=True)
    Max_lat = models.FloatField(default=0,blank=True,null=True)
    queue_depth = models.ForeignKey(Queue_depth)
    io_size = models.ForeignKey(io_size)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'nvme_driver_trend_result'


################### Test ######################
class Spdk_Perf_Result(models.Model):
    iops = models.FloatField(default=0,blank=True,null=True)
    latency = models.FloatField(default=0,blank=True,null=True)
    case_type = models.CharField(max_length=30)
    testexecution = models.ForeignKey(TestExecution)
    create_time = models.DateTimeField(auto_now_add=True)
    rw_method = models.ForeignKey(Rw_method)
    queue_depth = models.ForeignKey(Queue_depth)
    io_size = models.ForeignKey(io_size)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'spdk_perf_result'


#Record the max trend_iops & trend_latency in this table:
class Vhost_Scsi_Trend_Table(models.Model):
    trend_iops = models.FloatField(default=0,blank=True,null=True)
    trend_latency = models.FloatField(default=0,blank=True,null=True)
    testexecution = models.ForeignKey(TestExecution)
    create_time = models.DateTimeField(auto_now_add=True)
    rw_method = models.ForeignKey(Rw_method)
    queue_depth = models.ForeignKey(Queue_depth)
    io_size = models.ForeignKey(io_size)
    project = models.ForeignKey(Project)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'vhost_scsi_trend_result'



'''
class Dpdk_Daily_Result(models.Model):
    create_time = models.DateTimeField()
'''

#Nvme Driver DB:
class NvmeDriverTestPlan(models.Model):
    name = models.CharField(max_length=200)
    rw = models.ForeignKey(Rw_method)
    io_size=models.ForeignKey(io_size)
    queue_depth=models.ForeignKey(Queue_depth)
    owner = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'nvme_driver_testplan'
