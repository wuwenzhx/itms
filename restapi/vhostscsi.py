from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, get_project_object,check_name,get_object

class VhostScsiPerfResultDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    @check_auth_reader
    def get(self, request, project,pk):
        vhost_scsi_perf_result_list = Vhost_Scsi_Perf_Result.objects.all()
        serializer = VhostScsiPerfSerializer(vhost_scsi_perf_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
####################### API Post Method:#########################	
    def post(self, request,project,pk):
        serializer=VhostScsiPerfSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            iops=serializer.validated_data['iops']
            latency=serializer.validated_data['latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        case_type=serializer.validated_data.get('case_type',None)
        new_testsuit_result=Vhost_Scsi_Perf_Result.objects.create(
            iops=iops,
            latency=latency,
            case_type=case_type,
	    testexecution=testexecution,
            rw_method = rw_method,
            queue_depth = queue_depth,
            io_size = io_size,
            project=get_project_object(project)
        )
        new_serializer = VhostScsiPerfSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)

    def put(self, request, project, pk):
        serializer = VhostScsiPerfSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            iops=serializer.validated_data['iops']
            latency=serializer.validated_data['latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
	    create_time = serializer.validated_data['create_time']
        except KeyError:
        #    return Response({'detail': unicode("The lack of required parameters.")},
        #                    status=status.HTTP_400_BAD_REQUEST)
            pass
        vhost_scsi_trend_obj = get_object(Vhost_Scsi_Trend_Table,project,pk)
        vhost_scsi_trend_obj.trend_iops=trend_iops
        vhost_scsi_trend_obj.trend_latency = trend_latency
        vhost_scsi_trend_obj.test_case = test_case
        vhost_scsi_trend_obj.testexecution = testexecution
        vhost_scsi_trend_obj.rw_method = rw_method
        vhost_scsi_trend_obj.queue_depth = queue_depth
        vhost_scsi_trend_obj.io_size = io_size
        vhost_scsi_trend_obj.save()
        new_serializer = VhostScsiTrendSerializer(vhost_scsi_trend_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

class VhostScsiTrendResultDetail(APIView):
    
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    #@check_auth_reader
    def get(self, request, project,pk):
    #def get(self, request, project):
        #suite_result_list = MySuiteResult.objects.filter(testexecution=execution_obj)
        vhost_scsi_trend_result_list = Vhost_Scsi_Trend_Table.objects.all()
        serializer = VhostScsiTrendSerializer(vhost_scsi_trend_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

####################### I defined the API #########################	
    def post(self, request,project,pk):
        serializer=VhostScsiTrendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            trend_iops=serializer.validated_data['trend_iops']
            trend_latency=serializer.validated_data['trend_latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
	    create_time = serializer.validated_data['create_time']

        except KeyError:
            pass
            #return Response({'detail': unicode("The lack of required parameters.")},
            #             status=status.HTTP_400_BAD_REQUEST)
        new_testsuit_result=Vhost_Scsi_Trend_Table.objects.create(
            trend_iops=trend_iops,
            trend_latency=trend_latency,
	    testexecution=testexecution,
            rw_method = rw_method,
            queue_depth = queue_depth,
            io_size = io_size,
            project=get_project_object(project)
        )
        new_serializer = VhostScsiTrendSerializer(new_testsuit_result)
        return Response(new_serializer.data,status=status.HTTP_201_CREATED)
    
    def put(self, request, project, pk):
        serializer = VhostScsiTrendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            trend_iops=serializer.validated_data['trend_iops']
            trend_latency=serializer.validated_data['trend_latency']
	    testexecution = serializer.validated_data['testexecution']
            rw_method = serializer.validated_data['rw_method']
            queue_depth = serializer.validated_data['queue_depth']
            io_size = serializer.validated_data['io_size']
	    create_time = serializer.validated_data['create_time']
        except KeyError:
        #    return Response({'detail': unicode("The lack of required parameters.")},
        #                    status=status.HTTP_400_BAD_REQUEST)
            pass
        vhost_scsi_trend_obj = get_object(Vhost_Scsi_Trend_Table,project,pk)
        vhost_scsi_trend_obj.trend_iops=trend_iops
        vhost_scsi_trend_obj.trend_latency=trend_latency
        vhost_scsi_trend_obj.testexecution = testexecution
        vhost_scsi_trend_obj.rw_method = rw_method
        vhost_scsi_trend_obj.queue_depth = queue_depth
        vhost_scsi_trend_obj.io_size = io_size
        vhost_scsi_trend_obj.save()
        new_serializer = VhostScsiTrendSerializer(vhost_scsi_trend_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)





