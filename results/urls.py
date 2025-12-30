from django.urls import path
from results.views import (
    UploadResultView,
    UpdateResultView,
    StudentResultsView,
    CourseResultsView,
)

urlpatterns = [
    path("results/", UploadResultView.as_view(), name="upload_result"),
    path("results/<int:id>/", UpdateResultView.as_view(), name="update_result"),
    path("student/results/", StudentResultsView.as_view(), name="student_results"),
    path("course/<str:course_id>/results/", CourseResultsView.as_view(), name="course_results"),
]
