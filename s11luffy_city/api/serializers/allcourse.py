from rest_framework import serializers
from api import models

class CourseModuleModelSerializer(serializers.ModelSerializer):  # 所有的专题课
    degree_course = serializers.CharField(source='degree_course.name')
    class Meta:
        model = models.Course
        fields = ['id','degree_course']