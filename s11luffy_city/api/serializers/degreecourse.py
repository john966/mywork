from rest_framework import serializers
from api import models

class DegreeCourseTeachersModelSerializer(serializers.ModelSerializer):  # 学位课的老师
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name','teachers']

    def get_teachers(self,row):
        print(row)
        teachers_list = row.teachers.all()
        return [ {'id':item.id,'name':item.name} for item in teachers_list]



