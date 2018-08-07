from django.conf.urls import url
from api.views import course
from api.views import degreecourse
from api.views import scholarship
from api.views import allcourse
# from api import views
#
#
# urlpatterns = [
#     # url(r'degreecourses/',views.Courses.as_view())
# ]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls


urlpatterns = [
    url(r'courses/$',course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    url(r'degreecourse/teachers/$',degreecourse.DegreeCourseTeachersView.as_view()),
    url(r'degreecourse/scholarship/$',scholarship.DegreeCourseScholarshipView.as_view()),
    url(r'allcourse/$',allcourse.AllCourse.as_view())
]