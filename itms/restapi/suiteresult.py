from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, get_project_object,check_name,get_object


class TestexecutionSuiteResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):
        execution_obj = get_object(TestExecution, project, pk)
        suite_result_list = TestSuiteResult.objects.filter(testexecution=execution_obj)
        serializer = TestsuiteResultSerializer(suite_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=TestsuiteResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
           #id = serializer.validated_data['id']
            testexecution=serializer.validated_data['testexecution']
            testsuite=serializer.validated_data['testsuite']
            passed=serializer.validated_data['passed']
            failed=serializer.validated_data['failed']
            block=serializer.validated_data['block']
            na =serializer.validated_data['na']
            total=serializer.validated_data['total']
            #time=serializer.validated_data['time']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=TestSuiteResult.objects.create(
            #id=id,
            testexecution=testexecution,
            testsuite=testsuite,
            passed=passed,
            failed=failed,
            block=block,
            na=na,
            total=total,
            #time=time,
            project=get_project_object(project)
        )
        #new_testsuit_result.save()
        new_serializer = TestsuiteResultSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

#############The Put method #################
    def put(self, request, project, pk):
        serializer = TestsuiteResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            #id = serializer.validated_data['id']
            testexecution=serializer.validated_data['testexecution']
            #id = serializer.validated_data['id']
            testsuite=serializer.validated_data['testsuite']
            passed=serializer.validated_data['passed']
            failed=serializer.validated_data['failed']
            block=serializer.validated_data['block']
            na =serializer.validated_data['na']
            total=serializer.validated_data['total']
            #time=serializer.validated_data['time']
        except KeyError:
            pass
	suiteresult_obj = get_object(TestPlan,project,pk)
        #suiteresult_obj.id=id
	suiteresult_obj.testexecution=testexecution
	suiteresult_obj.testsuite=testsuite
	suiteresult_obj.passed=passed
	suiteresult_obj.failed=failed
	suiteresult_obj.block=block
	suiteresult_obj.na=na
	suiteresult_obj.total=total
	suiteresult_obj.save()

        new_serializer = TestsuiteResultSerializer(suiteresult_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)



class TestexecutionPerfSuiteResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        execution_obj = get_object(TestExecution, project, pk)
        perf_suite_result_list = PerfTestSuiteResult.objects.filter(testexecution=execution_obj)
        serializer = TestsuitePerfResultSerializer(perf_suite_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PerTestsuiteResultTestcaseResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        suiteresult_obj = get_object(PerfTestSuiteResult, project, pk)
        perf_caseresult_list = PerfTestCaseResult.objects.filter(perf_testsuite_result=suiteresult_obj)
        serializer = PerTestcaseResultSerializer(perf_caseresult_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PerTestcaseResultTestcaseDetailResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        caseresult_obj = get_object(PerfTestCaseResult, project, pk)
        casedetail_result_list = PerfTestCaseResultDetail.objects.filter(
            perf_testcase_result=caseresult_obj)
        serializer = PerTestcaseResultDetailSerializer(casedetail_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#class TestsuiteTestcaseDetail(APIView):
#    authentication_classes = (SessionAuthentication, BasicAuthentication)

#    @check_auth_reader
#    def get(self, request, project, pk):
#        suite_obj = get_object(TestSuite, project, pk)
#        case_list = TestCase.objects.filter(testsuite=suite_obj)
#        serializer = TestcaseSerializer(case_list, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)


#class TestSuiteResultTestcaseResultDetail(APIView):
#    authentication_classes = (SessionAuthentication, BasicAuthentication)

#    @check_auth_reader
#    def get(self, request, project, pk):
#        suiteresult_obj = get_object(TestSuiteResult, project, pk)
#        caseresult_list = TestCaseResult.objects.filter(testsuite_result=suiteresult_obj)
#        serializer = TestcaseResultSerializer(caseresult_list, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)



############## I defined ############

class MySuiteResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):
        execution_obj = get_object(TestExecution, project, pk)
        suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        serializer = MySuiteResultSerializer(suite_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=MySuiteResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
           #id = serializer.validated_data['id']
            testexecution=serializer.validated_data['testexecution']
            testsuite=serializer.validated_data['testsuite']
            zero_loss_throughput=serializer.validated_data['zero_loss_throughput']
            zero_loss_rate=serializer.validated_data['zero_loss_rate']
            #time=serializer.validated_data['time']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=MySuiteResult.objects.create(
            #id=id,
            testexecution=testexecution,
            testsuite=testsuite,
            zero_loss_throughput=zero_loss_throughput,
            zero_loss_rate=zero_loss_rate,
            #time=time,
            project=get_project_object(project)
        )
        new_serializer = MySuiteResultSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

    def put(self, request, project, pk):
        serializer = MySuiteResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            testexecution=serializer.validated_data['testexecution']
            testsuite=serializer.validated_data['testsuite']
            zero_loss_throughput=serializer.validated_data['zero_loss_throughput']
            zero_loss_rate=serializer.validated_data['zero_loss_rate']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #                status=status.HTTP_400_BAD_REQUEST)

        #if not check_name_by_id(MySuiteResult,testsuite, project, pk):
        #    return Response({'detail': unicode("Found same name testsuite, "
        #                                       "please check your testsuite id.")},
        #                    status=status.HTTP_409_CONFLICT)

        dpdk_result_obj = get_object(MySuiteResult, project, pk)
        #if plan_obj.performance != perf or plan_obj.app != app:
        #    return Response({'detail': unicode("Not allow change performance and app attribute.")},
        #                    status=status.HTTP_400_BAD_REQUEST)

        #if not check_owner_runner(plan_obj.owner, plan_owner):
        #    return Response({'detail': unicode("The owner can not be changed.")},
        #                    status=status.HTTP_400_BAD_REQUEST)

        dpdk_result_obj.testexecution = testexecution
        dpdk_result_obj.testsuite = testsuite
        dpdk_result_obj.zero_loss_throughput= zero_loss_throughput
        dpdk_result_obj.zero_loss_rate = zero_loss_rate
        dpdk_result_obj.save()

        new_serializer = MySuiteResultSerializer(dpdk_result_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        myresult_obj = get_object(MySuiteResult, project, pk)
        myresult_obj.del_flag = True
        myresult_obj.testsuite_set.clear()
        myresult_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


#class NicPerfResultDetail(APIView):
#    authentication_classes = (SessionAuthentication, BasicAuthentication)

#   @check_auth_reader
#    def get(self, request, project):
    #url(r'^(?P<project>.*)/nicresult/$',
        #create_time_obj = get_object(TimeRecordTable, project)
#        nicperf_result_list = NicPerfTable.objects.all()
#        serializer = NicPerfResultSerializer(nicperf_result_list, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)


class CpuTypeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
        if request.user.is_active:
	    #cpu_type_obj = get_object(CpuType,project,)
            #cpu_type_list = CpuType.objects.filter(cpu_type = cpu_type_obj)
            #cpu_type_list = CpuType.objects.filter(project__name=project)
            cpu_type_list = CpuType.objects.all()
            serializer = CpuTypeSerializer(cpu_type_list, many=True )
            #content, auth_status = serializer.data, status.HTTP_200_OK
        #else:
        #    content = {
        #      'detail': unicode("The password is valid, but the account has been disabled!~"),
        #    }
        #    auth_status = status.HTTP_401_UNAUTHORIZED
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=CpuTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            cpu_type = serializer.validated_data['cpu_type']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=CpuType.objects.create(
            cpu_type = cpu_type,
            #time=time,
            project=get_project_object(project)
        )
        new_serializer = CpuTypeSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

class CpuInfoDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
        if request.user.is_active:
	    #cpu_type_obj = get_object(CpuType,project,)
            #cpu_type_list = CpuType.objects.filter(cpu_type = cpu_type_obj)
            #cpu_type_list = CpuType.objects.filter(project__name=project)
            cpu_info_list = CpuInfo.objects.all()
            serializer = CpuInfoSerializer(cpu_info_list, many=True )
            #content, auth_status = serializer.data, status.HTTP_200_OK
        #else:
        #    content = {
        #      'detail': unicode("The password is valid, but the account has been disabled!~"),
        #    }
        #    auth_status = status.HTTP_401_UNAUTHORIZED
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=CpuInfoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            case_name = serializer.validated_data['case_name']
            case_type=serializer.validated_data['case_type']
            branch_commit_id= serializer.validated_data['branch_commit_id']
            commit_info=serializer.validated_data['commit_info']
            test_command = serializer.validated_data['test_command']
            board_name = serializer.validated_data['board_name']
            cpu_info = serializer.validated_data['cpu_info']
            memory_info = serializer.validated_data['memory_info']
            nic_name = serializer.validated_data['nic_name']
            device = serializer.validated_data['device']
            firmware= serializer.validated_data['firmware']
            distro_info = serializer.validated_data['distro_info']
            kernel_info = serializer.validated_data['kernel_info']
            gcc_info = serializer.validated_data['gcc_info']
            #time=serializer.validated_data['time']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=TestRecordTable.objects.create(
            case_name=case_name,
            case_type=case_type,
            branch_commit_id=branch_commit_id,
            commit_info=commit_info,
            test_command=test_command,
            board_name=board_name,
            cpu_info=cpu_info,
            nic_name=nic_name,
            device=device,
            firmware=firmware,
            distro_info = distro_info,
            kernel_info = kernel_info,
            gcc_info = gcc_info,
            #time=time,
            project=get_project_object(project)
        )
        new_serializer = TestRecordSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)





class TestRecordTableDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):
        suite_result_list = TestRecordTable.objects.filter(project__name=project)
        serializer = TestRecordSerializer(suite_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	

    def post(self, request,project,pk):
        serializer=TestRecordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            case_name = serializer.validated_data['case_name']
            case_type=serializer.validated_data['case_type']
            branch_commit_id= serializer.validated_data['branch_commit_id']
            commit_info=serializer.validated_data['commit_info']
            test_command = serializer.validated_data['test_command']
            board_name = serializer.validated_data['board_name']
            cpu_info = serializer.validated_data['cpu_info']
            memory_info = serializer.validated_data['memory_info']
            nic_name = serializer.validated_data['nic_name']
            device = serializer.validated_data['device']
            firmware= serializer.validated_data['firmware']
            distro_info = serializer.validated_data['distro_info']
            kernel_info = serializer.validated_data['kernel_info']
            gcc_info = serializer.validated_data['gcc_info']
            #time=serializer.validated_data['time']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=TestRecordTable.objects.create(
            case_name=case_name,
            case_type=case_type,
            branch_commit_id=branch_commit_id,
            commit_info=commit_info,
            test_command=test_command,
            board_name=board_name,
            cpu_info=cpu_info,
            nic_name=nic_name,
            device=device,
            firmware=firmware,
            distro_info = distro_info,
            kernel_info = kernel_info,
            gcc_info = gcc_info,
            #time=time,
            project=get_project_object(project)
        )
        new_serializer = TestRecordSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

    def put(self, request, project, pk):
        serializer = MySuiteResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            testexecution=serializer.validated_data['testexecution']
            testsuite=serializer.validated_data['testsuite']
            zero_loss_throughput=serializer.validated_data['zero_loss_throughput']
            zero_loss_rate=serializer.validated_data['zero_loss_rate']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #                status=status.HTTP_400_BAD_REQUEST)

        #if not check_name_by_id(MySuiteResult,testsuite, project, pk):
        #    return Response({'detail': unicode("Found same name testsuite, "
        #                                       "please check your testsuite id.")},
        #                    status=status.HTTP_409_CONFLICT)

        dpdk_result_obj = get_object(MySuiteResult, project, pk)
        #if plan_obj.performance != perf or plan_obj.app != app:
        #    return Response({'detail': unicode("Not allow change performance and app attribute.")},
        #                    status=status.HTTP_400_BAD_REQUEST)

        #if not check_owner_runner(plan_obj.owner, plan_owner):
        #    return Response({'detail': unicode("The owner can not be changed.")},
        #                    status=status.HTTP_400_BAD_REQUEST)

        dpdk_result_obj.testexecution = testexecution
        dpdk_result_obj.testsuite = testsuite
        dpdk_result_obj.zero_loss_throughput= zero_loss_throughput
        dpdk_result_obj.zero_loss_rate = zero_loss_rate
        dpdk_result_obj.save()

        new_serializer = MySuiteResultSerializer(dpdk_result_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, project, pk):
        myresult_obj = get_object(MySuiteResult, project, pk)
        myresult_obj.del_flag = True
        myresult_obj.testsuite_set.clear()
        myresult_obj.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class NicNameDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
        if request.user.is_active:
	    #cpu_type_obj = get_object(CpuType,project,)
            #cpu_type_list = CpuType.objects.filter(cpu_type = cpu_type_obj)
            #cpu_type_list = CpuType.objects.filter(project__name=project)
            nicname_list = NicName.objects.all()
            serializer = NicNameSerializer(nicname_list, many=True )
            #content, auth_status = serializer.data, status.HTTP_200_OK
        #else:
        #    content = {
        #      'detail': unicode("The password is valid, but the account has been disabled!~"),
        #    }
        #    auth_status = status.HTTP_401_UNAUTHORIZED
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=NicNameSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            name = serializer.validated_data['name']
        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=NicName.objects.create(
            name = name,
            #time=time,
            project=get_project_object(project)
        )
        new_serializer = NicNameSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)



class FirmwareDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
        if request.user.is_active:
            firmware_list = Firmware.objects.all()
            serializer = FirmwareSerializer(firmware_list, many=True )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=FirmwareSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            firmware = serializer.validated_data['firmware']
        except KeyError:
            pass
        new_testsuit_result=Firmware.objects.create(
            name = name,
            project=get_project_object(project)
        )
        new_serializer = FirmwareSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)


class CaseTypeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
            case_type_list = CaseType.objects.all()
            serializer = CaseTypeSerializer(firmware_list, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=SerializerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            case_type = CaseTypeSerializer.validated_data['case_type']
        except KeyError:
            pass
        new_testsuit_result=Firmware.objects.create(
            case_type = case_type,
            project=get_project_object(project)
        )
        new_serializer = CaseTypeSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)



class CaseTypeDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
            case_type_list = CaseType.objects.all()
            serializer = CaseTypeSerializer(case_type_list, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=CaseTypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            case_type = CaseTypeserializer.validated_data['case_type']
        except KeyError:
            pass
        new_testsuit_result=Firmware.objects.create(
            case_type = case_type,
            project=get_project_object(project)
        )
        new_serializer = CaseTypeSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)



class NicPerfTableDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
            nic_perf_list = NicPerfTable.objects.filter(project__name=project)
            serializer = NicPerfTableSerializer(nic_perf_list, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=NicPerfTableSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            frame_size = serializer.validated_data['frame_size']
            thoughput = serializer.validated_data['thoughput']
            send_rate = serializer.validated_data['send_rate']
            expected_thoughput = serializer.validated_data['expected_thoughput']
        except KeyError:
            pass
        new_testsuit_result=NicPerfTable.objects.create(
            frame_size = frame_size,
            thoughput = thoughput,
            send_rate = send_rate,
            expected_thoughput = expected_thoughput,
            project=get_project_object(project)
        )
        new_serializer = NicPerfTableSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)




class SingleCorePerfTableDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request,project,pk):
        #if request.user.is_active:
            singlecore_perf_list = SingleCorePerfTable.objects.all()
            serializer = SingleCorePerfTableSerializer(singlecore_perf_list, many=True )
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,project,pk):
        serializer=SingleCorePerfTableSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            frame_size = serializer.validated_data['frame_size']
            thoughput = serializer.validated_data['thoughput']
            send_rate = serializer.validated_data['send_rate']
            cpu_freq = serializer.validated_data['cpu_freq']
            per_packet_cycle = serializer.validated_data['per_packet_cycle']
            expected_thoughput = serializer.validated_data['expected_thoughput']
        except KeyError:
            pass
        new_testsuit_result=SingleCorePerfTable.objects.create(
            frame_size = frame_size,
            thoughput = thoughput,
            send_rate = send_rate,
            cpu_freq = cpu_freq,
            per_packet_cycle = per_packet_cycle,
            expected_thoughput = expected_thoughput,
            project=get_project_object(project),
        )
        new_serializer = SingleCorePerfTableSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)


class SpdkPerfResultDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):

        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        spdk_perf_result_list = Spdk_Perf_Result.objects.all()
        serializer = SpdkPerfResultSerializer(spdk_perf_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=SpdkPerfResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
           #id = serializer.validated_data['id']
            iops=serializer.validated_data['iops']
            latency=serializer.validated_data['latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
            #time=serializer.validated_data['time']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        case_type=serializer.validated_data.get('case_type',None)
        new_testsuit_result=Spdk_Perf_Result.objects.create(
            #id=id,
            iops=iops,
            latency=latency,
            case_type=case_type,
	    testexecution=testexecution,
            #create_time=create_time,
            rw_method = rw_method,
            queue_depth = queue_depth,
            io_size = io_size,
            project=get_project_object(project)
        )
        new_serializer = SpdkPerfResultSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)


class RwMethodDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):

        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        rw_method_list = Rw_method.objects.all()
        serializer = RwMethodSerializer(rw_method_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=RwMethodSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            rw_method=serializer.validated_data['rw_method']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=Rw_method.objects.create(
            rw_method = rw_method,
            project=get_project_object(project)
        )
        new_serializer = RwMethodSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

class Queue_depthDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):

        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        queue_depth_list = Queue_depth.objects.all()
        serializer = Queue_depthSerializer(queue_depth_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=Queue_depthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            queue_depth=serializer.validated_data['queue_depth']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=Queue_depth.objects.create(
            queue_depth = queue_depth,
            project=get_project_object(project)
        )
        new_serializer = Queue_depthSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)


class io_sizeDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):

        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        io_size_list = io_size.objects.all()
        serializer = io_sizeSerializer(io_size_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=io_sizeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            size=serializer.validated_data['io_size']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result = io_size.objects.create(
            io_size = size,
            project=get_project_object(project)
        )
        new_serializer = io_sizeSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

class SpdkTrendResultDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):

        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        spdk_trend_result_list = SpdkAvgTrendTable.objects.all()
        serializer = SpdkTrendResultSerializer(spdk_trend_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=SpdkTrendResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
           #id = serializer.validated_data['id']
            trend_iops=serializer.validated_data['trend_iops']
            trend_latency=serializer.validated_data['trend_latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
            #time=serializer.validated_data['time']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=SpdkAvgTrendTable.objects.create(
            #id=id,
            trend_iops=trend_iops,
            trend_latency=trend_latency,
	    testexecution=testexecution,
            #create_time=create_time,
            rw_method = rw_method,
            queue_depth = queue_depth,
            io_size = io_size,
            project=get_project_object(project)
        )
        new_serializer = SpdkTrendResultSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

##########
class NvmeDriverResultDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project,pk):
        nvme_driver_trend_result_list = NvmeDriverTrendTable.objects.all()
        serializer = NvmeDriverTrendResultSerializer(nvme_driver_trend_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=NvmeDriverTrendResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
           #id = serializer.validated_data['id']
            trend_iops=serializer.validated_data['trend_iops']
            trend_latency=serializer.validated_data['trend_latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
            MBps = serializer.validated_data['MBps']
            workload_mix = serializer.validated_data['workload_mix']
            Core_Mask = serializer.validated_data['Core_Mask']
            run_time = serializer.validated_data['run_time']
            Average_lat = serializer.validated_data['Average_lat']
            Min_lat = serializer.validated_data['Min_lat']
            Max_lat = serializer.validated_data['Max_lat']
            #time=serializer.validated_data['time']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=NvmeDriverTrendTable.objects.create(
            #id=id,
            trend_iops=trend_iops,
            trend_latency=trend_latency,
	    testexecution=testexecution,
            MBps = MBps,
            #create_time=create_time,
            rw_method = rw_method,
            queue_depth = queue_depth,
            io_size = io_size,
            workload_mix = workload_mix,
            Core_Mask = Core_Mask,
            run_time = run_time,
            Average_lat = Average_lat,
            Min_lat = Min_lat,
            Max_lat = Max_lat,
            project=get_project_object(project)
        )
        new_serializer = NvmeDriverTrendResultSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)
