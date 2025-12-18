from django.urls import path
from enrollment.views import (
    RegisterCourseView,
    StudentCoursesView,
    CourseStudentsView
)

urlpatterns = [
    path("register-course/", RegisterCourseView.as_view()),
    path("student/courses/", StudentCoursesView.as_view()),
    path("course/<str:course_id>/students/", CourseStudentsView.as_view()),
]
