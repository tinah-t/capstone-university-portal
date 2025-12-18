from rest_framework import serializers
from courses.models import Course
from accounts.models import Teacher


class CourseSerializer(serializers.ModelSerializer):
    # Admin sends teacher_id (string)
    teacher_id = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=True
    )

    # Read-only teacher details
    teacher = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "course_id",
            "name",
            "course_code",
            "credit_hours",
            "teacher_id",
            "teacher",
            "created_at",
        ]
        read_only_fields = ["id", "course_id", "created_at"]

    def get_teacher(self, obj):
        if not obj.teacher:
            return None
        return {
            "teacher_id": obj.teacher.teacher_id,
            "first_name": obj.teacher.user.first_name,
            "last_name": obj.teacher.user.last_name,
            "email": obj.teacher.user.email,
        }

    def validate_teacher_id(self, value):
        if value is None:
            return None
        try:
            return Teacher.objects.get(teacher_id=value)
        except Teacher.DoesNotExist:
            raise serializers.ValidationError("Teacher with this ID does not exist.")

    def create(self, validated_data):
        teacher = validated_data.pop("teacher_id", None)
        return Course.objects.create(teacher=teacher, **validated_data)

    def update(self, instance, validated_data):
        teacher = validated_data.pop("teacher_id", None)
        if teacher is not None:
            instance.teacher = teacher

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class CourseMiniSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "course_id",
            "name",
            "course_code",
            "credit_hours",
            "teacher_name",
        ]

    def get_teacher_name(self, obj):
        if obj.teacher:
            return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"
        return None
