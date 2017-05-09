from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object, get_object
from utils import check_case_in_suite, check_app_attr


class PerDPDKTestsuiteResultTestcaseResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        suiteresult_obj = get_object(PerfTestSuiteResult, project, pk)
        perf_caseresult_list = PerfDPDKTestCaseResult.objects.filter(perf_testsuite_result=suiteresult_obj)
        serializer = PerDPDKTestCaseResultSerializer(perf_caseresult_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PerDPDKTestcaseResultTestcaseDetailResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        caseresult_obj = get_object(PerfDPDKTestCaseResult, project, pk)
        casedetail_result_list = PerfDPDKTestCaseResultDetail.objects.filter(
            perf_dpdk_testcase_result=caseresult_obj)
        serializer = PerDPDKTestcaseResultDetailSerializer(casedetail_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PerDPDKTestcaseResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        caseresult_obj = get_object(PerfDPDKTestCaseResult, project, pk)
        serializer = PerDPDKTestCaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = PerDPDKTestCaseResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            bug = serializer.validated_data['bug']
            log = serializer.validated_data['log']
            comments = serializer.validated_data['comments']
        except KeyError:
            return Response({'detail': unicode('The lack of required parameters.')},
                            status=status.HTTP_400_BAD_REQUEST)
        caseresult_obj = get_object(PerfDPDKTestCaseResult, project, pk)
        caseresult_obj.bug = bug
        caseresult_obj.log = log
        caseresult_obj.comments = comments
        caseresult_obj.save()

        serializer = PerDPDKTestCaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class PerDPDKTestcaseResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        result_list = PerfDPDKTestCaseResultDetail.objects.filter(project__name=project)
        serializer = PerDPDKTestcaseResultDetailSerializer(result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def post(self, request, project):
        serializer = PerDPDKTestcaseResultDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            perf_dpdk_testcase_result = serializer.validated_data['perf_dpdk_testcase_result']
            key = serializer.validated_data['key']
            value = serializer.validated_data['value']
            app = serializer.validated_data['app']
            group = serializer.validated_data['group']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if perf_dpdk_testcase_result.app != app:
            return Response({'detail': unicode("The attribute app not match testcase result.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_app_attr(key, app, project):
            return Response({'detail': unicode("app ({}) not have attribute ({})"
                                               .format(app.name, key.name))},
                            status=status.HTTP_400_BAD_REQUEST)

        if PerfDPDKTestCaseResultDetail.objects.filter(perf_dpdk_testcase_result=perf_dpdk_testcase_result,
                                                       key=key, app=app, group=group,
                                                       project__name=project).count():
            return Response({'detail': unicode("perf_dpdk_testcase result detail already exist."
                                               "please use PUT method to update result detail.")},
                            status=status.HTTP_409_CONFLICT)
        new_result_detail = PerfDPDKTestCaseResultDetail.objects.create(
            perf_dpdk_testcase_result=perf_dpdk_testcase_result,
            key=key, value=value, app=app, group=group, project=get_project_object(project)
        )
        new_result_detail.save()
        serializer = PerDPDKTestcaseResultDetailSerializer(new_result_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PerDPDKTestcaseResultDetailPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        testcase_result_detail_obj = get_object(PerfDPDKTestCaseResultDetail, project, pk)
        serializer = PerDPDKTestcaseResultDetailSerializer(testcase_result_detail_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = PerDPDKTestcaseResultDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            key = serializer.validated_data['key']
            value = serializer.validated_data['value']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        testcase_result_detail_obj = get_object(PerfDPDKTestCaseResultDetail, project, pk)
        if not check_app_attr(key, testcase_result_detail_obj.app, project):
            return Response({'detail': unicode("app ({0}) not have attribute ({1})"
                                               .format(testcase_result_detail_obj.app.name, key.name))},
                            status=status.HTTP_400_BAD_REQUEST)

        testcase_result_detail_obj.key = key
        testcase_result_detail_obj.value = value
        testcase_result_detail_obj.save()
        new_serializer = PerDPDKTestcaseResultDetailSerializer(testcase_result_detail_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    def delete(self, request, project, pk):
        testcase_result_detail_obj = get_object(PerfDPDKTestCaseResultDetail, project, pk)
        testcase_result_detail_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

