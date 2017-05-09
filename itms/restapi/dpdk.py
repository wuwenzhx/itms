from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, get_project_object,check_name,get_object


#############################Dpdk_no_key:############################################

#############################Dpdk no key API:########################################
class DpdkTestRecordTableDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    @check_auth_reader
    def get(self, request, project,pk):
        suite_result_list = DpdkTestRecordTable.objects.filter(project__name=project)
        serializer = DpdkTestRecordSerializer(suite_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
####################### I defined the API########################################	

    def post(self, request,project,pk):
        serializer=DpdkTestRecordSerializer(data=request.data)
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
        new_testsuit_result=DpdkTestRecordTable.objects.create(
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
        new_serializer = DpdkTestRecordSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

    def put(self, request, project, pk):
        serializer = DpdkTestRecordSerializer(data=request.data)
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

        dpdk_result_obj = get_object(DpdkTestRecordTable, project, pk)
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

        new_serializer = DpdkTestRecordTable(dpdk_result_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)
































