from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk, role=User.Role.STUDENT)

        serializer = StudentCreateSerializer(
            instance=user,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Student updated successfully"},
            status=status.HTTP_200_OK
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

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk, role=User.Role.TEACHER)

        serializer = TeacherCreateSerializer(
            instance=user,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Teacher updated successfully"},
            status=status.HTTP_200_OK
        )



class UserListView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
