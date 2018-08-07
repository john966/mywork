from rest_framework import serializers
from api import models

class DegreeCourseScholarshipModelSerializer(serializers.ModelSerializer):
    # 查看所有学位课并打印学位课名称以及学位课的奖学金
    # DegreeCourse.objects.all()
    scholarship = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name','scholarship','teachers']

    def get_scholarship(self,row):
        scholarship_list = row.scholarship_set.all()
        print(scholarship_list)
        return [{'value': item.value} for item in scholarship_list]

    def get_teachers(self,row):
        teachers_list = row.teachers.all()

        return [{'id':item.id,'name':item.name} for item in teachers_list]

