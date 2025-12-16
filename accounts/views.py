from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    StudentCreateSerializer,
    TeacherCreateSerializer,
    UserListSerializer,
)
from .permissions import IsAdmin
from .models import User


class CreateStudentView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Student created successfully"},
            status=status.HTTP_201_CREATED
        )


class CreateTeacherView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = TeacherCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Teacher created successfully"},
            status=status.HTTP_201_CREATED
        )


class UserListView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
