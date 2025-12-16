from rest_framework import serializers
from .models import User, Student, Teacher


# ======================
# Student Creation
# ======================
class StudentCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    department = serializers.CharField()
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            role=User.Role.STUDENT
        )
        Student.objects.create(
            user=user,
            phone_number=validated_data["phone_number"],
            department=validated_data["department"]
        )
        return user

# ======================
# Teacher Creation
# ======================
class TeacherCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    def create(self, validated_data):
        user = User.objects.create_user(
        username = validated_data["username"],
        password = validated_data["password"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
        email=validated_data["email"],
        role=User.Role.TEACHER
        )
        Teacher.objects.create(user=user)
        return user

# ======================
# User List (Admin)
# ======================
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "role"]