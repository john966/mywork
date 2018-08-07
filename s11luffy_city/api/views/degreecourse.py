from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination
# from api import serializers

from api import models
from api.serializers.course import CourseSerializer,CourseModelSerializer
from api.utils.response import BaseResponse
#
from api.serializers.degreecourse import DegreeCourseTeachersModelSerializer


class DegreeCourseTeachersView(APIView):  # 学位课对应的老师
    def get(self, request, *args, **kwargs):
        # respone = {"code":1000,"status":None,"error",None}
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            # 防止出现UnorderedObjectListWarning: Pagination may yield...
            queryset = models.DegreeCourse.objects.order_by('id')
            print(queryset)
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)

            # 分页之后的结果执行序列化
            ser = DegreeCourseTeachersModelSerializer(instance=course_list, many=True)
            print(ser.data)

            ret.data = ser.data

        except Exception as e:

            print(e)

            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

