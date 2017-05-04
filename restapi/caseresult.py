from base_models.models import *
from restapi.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from utils import check_auth_reader, check_auth_writer, get_project_object, get_object
from utils import check_case_in_suite, check_app_attr


class TestcaseResult(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        case_result_list = TestCaseResult.objects.filter(project__name=project)
        serializer = TestcaseResultSerializer(case_result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    # post
    def xxx(self, request, project):
        serializer = TestcaseResultSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            testcase = serializer.validated_data['testcase']
            suite_result = serializer.validated_data['testsuite_result']
            result = str(serializer.validated_data['result']).lower()
            bug = serializer.validated_data['bug']
            log = serializer.validated_data['log']
            comments = serializer.validated_data['comments']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        message = check_case_in_suite(testcase, suite_result)
        if message:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        if TestCaseResult.objects.filter(testcase=testcase,
                                         testsuite_result=suite_result,
                                         project__name=project
                                         ).count():
            return Response({'detail': unicode("Testcase result already exist. "
                                               "please use PUT method to update result.")},
                            status=status.HTTP_409_CONFLICT)

        new_result = TestCaseResult.objects.create(testcase=testcase, testsuite_result=suite_result,
                                                   result=result, bug=bug, log=log, comments=comments,
                                                   project=get_project_object(project)
                                                   )
        new_result.save()
        serializer = TestcaseResultSerializer(new_result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TestcaseResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        caseresult_obj = get_object(TestCaseResult, project, pk)
        serializer = TestcaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = TestcaseResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = str(serializer.validated_data['result']).lower()
            bug = serializer.validated_data['bug']
            log = serializer.validated_data['log']
            comments = serializer.validated_data['comments']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        caseresult_obj = get_object(TestCaseResult, project, pk)
        caseresult_obj.result = result
        caseresult_obj.bug = bug
        caseresult_obj.log = log
        caseresult_obj.comments = comments
        caseresult_obj.save()

        serializer = TestcaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    # delete
    def xxx(self, request, project, pk):
        caseresult_obj = get_object(TestCaseResult, project, pk)
        caseresult_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PerTestcaseResult(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        result_list = PerfTestCaseResult.objects.filter(project__name=project)
        serializer = PerTestcaseResultSerializer(result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    # post
    def xxx(self, request, project):
        serializer = PerTestcaseResultSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            testcase = serializer.validated_data['testcase']
            suite_result = serializer.validated_data['perf_testsuite_result']
            bug = serializer.validated_data['bug']
            log = serializer.validated_data['log']
            comments = serializer.validated_data['comments']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        message = check_case_in_suite(testcase, suite_result)
        if message:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        if PerfTestCaseResult.objects.filter(testcase=testcase,
                                             perf_testsuite_result=suite_result,
                                             project__name=project
                                             ).count():
            return Response({'detail': unicode("perf_testcase result already exist. "
                                               "please use PUT method to update result.")},
                            status=status.HTTP_409_CONFLICT)

        new_result = PerfTestCaseResult.objects.create(testcase=testcase,
                                                       perf_testsuite_result=suite_result,
                                                       bug=bug, log=log, comments=comments,
                                                       app=testcase.app,
                                                       project=get_project_object(project)
                                                       )
        new_result.save()
        serializer = PerTestcaseResultSerializer(new_result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PerTestcaseResultPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        caseresult_obj = get_object(PerfTestCaseResult, project, pk)
        serializer = PerTestcaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = PerTestcaseResultSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            bug = serializer.validated_data['bug']
            log = serializer.validated_data['log']
            comments = serializer.validated_data['comments']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        caseresult_obj = get_object(PerfTestCaseResult, project, pk)
        caseresult_obj.bug = bug
        caseresult_obj.log = log
        caseresult_obj.comments = comments
        caseresult_obj.save()

        serializer = PerTestcaseResultSerializer(caseresult_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @check_auth_writer
    # delete
    def xxx(self, request, project, pk):
        caseresult_obj = get_object(PerfTestCaseResult, project, pk)
        caseresult_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PerTestcaseResultDetail(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project):
        result_list = PerfTestCaseResultDetail.objects.filter(project__name=project)
        serializer = PerTestcaseResultDetailSerializer(result_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    # post
    def xxx(self, request, project):
        serializer = PerTestcaseResultDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            perf_testcase_result = serializer.validated_data['perf_testcase_result']
            key = serializer.validated_data['key']
            value = serializer.validated_data['value']
            app = serializer.validated_data['app']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if perf_testcase_result.app != app:
            return Response({'detail': unicode("The attribute app not match testcase_result.")},
                            status=status.HTTP_400_BAD_REQUEST)

        if not check_app_attr(key, app, project):
            return Response({'detail': unicode("app ({0}) not have attribute ({1})"
                                               .format(app.name, key.name))},
                            status=status.HTTP_400_BAD_REQUEST)

        if PerfTestCaseResultDetail.objects.filter(perf_testcase_result=perf_testcase_result,
                                                   key=key, app=app, project__name=project).count():
            return Response({'detail': unicode("perf_testcase result detail already exist. "
                                               "please use PUT method to update result detail.")},
                            status=status.HTTP_409_CONFLICT)

        new_result_detail = PerfTestCaseResultDetail.objects.create(
            perf_testcase_result=perf_testcase_result,
            key=key, value=value, app=app, project=get_project_object(project)
        )
        new_result_detail.save()
        serializer = PerTestcaseResultDetailSerializer(new_result_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PerTestcaseResultDetailPK(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @check_auth_reader
    def get(self, request, project, pk):
        testcase_result_detail_obj = get_object(PerfTestCaseResultDetail, project, pk)
        serializer = PerTestcaseResultDetailSerializer(testcase_result_detail_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @check_auth_writer
    def put(self, request, project, pk):
        serializer = PerTestcaseResultDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            key = serializer.validated_data['key']
            value = serializer.validated_data['value']
        except KeyError:
            return Response({'detail': unicode("The lack of required parameters.")},
                            status=status.HTTP_400_BAD_REQUEST)

        testcase_result_detail_obj = get_object(PerfTestCaseResultDetail, project, pk)

        if not check_app_attr(key, testcase_result_detail_obj.app, project):
            return Response({'detail': unicode("app ({0}) not have attribute ({1})"
                                               .format(testcase_result_detail_obj.app.name, key.name))},
                            status=status.HTTP_400_BAD_REQUEST)

        testcase_result_detail_obj.key = key
        testcase_result_detail_obj.value = value
        testcase_result_detail_obj.save()
        new_serializer = PerTestcaseResultDetailSerializer(testcase_result_detail_obj)
        return Response(new_serializer.data, status=status.HTTP_202_ACCEPTED)


    @check_auth_writer
    # delete
    def xxx(self, request, project, pk):
        testcase_result_detail_obj = get_object(PerfTestCaseResultDetail, project, pk)
        testcase_result_detail_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
