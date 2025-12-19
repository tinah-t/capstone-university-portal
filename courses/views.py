from django.shortcuts import render
from accounts.permissions import IsAdmin
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializer import CourseSerializer
from accounts.permissions import IsStudentOrTeacherOrAdmin

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.select_related("teacher", "teacher__user")
    serializer_class = CourseSerializer

    def get_permissions(self):
        # Anyone authenticated can view courses
        if self.action in ["list", "retrieve"]:
            return [IsStudentOrTeacherOrAdmin()]

        # Only admins can create/update/delete
        return [IsAdmin()]
