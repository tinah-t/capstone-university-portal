from django.urls import path
from .views import CreateStudentView, CreateTeacherView, UserListView


urlpatterns = [
    path('students/create/',CreateStudentView.as_view(), name="create-student"),
    path("teachers/create/", CreateTeacherView.as_view(), name="create-teacher"),
    path("users/", UserListView.as_view(), name="user-list"),
]
