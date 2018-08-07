from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api import serializers

from api import models
from api.utils.response import BaseResponse
#
from api.serializers.degreecourse import DegreeCourseTeachersModelSerializer

class AllCourse(APIView):
    degree_course = serializers.CharField(source='degree_course.name')

    class Meta:
        model = models.Course
        fields = ['id', 'degree_course']