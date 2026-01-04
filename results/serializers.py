from rest_framework import serializers
from results.models import Result
from courses.serializer import CourseMiniSerializer
from accounts.serializers import StudentMiniSerializer
from accounts.models import Student
from courses.models import Course
from enrollment.models import Enrollment

class ResultSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(write_only=True)
    course_id = serializers.CharField(write_only=True)

    class Meta:
        model = Result
        fields = [
            "id",
            "student_id",
            "course_id",
            "grade",
            "remark",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    # ✅ FIX 1: RAISE ValidationError
    def validate_student_id(self, value):
        try:
            return Student.objects.get(student_id=value)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student does not exist.")

    # ✅ FIX 2: RAISE ValidationError
    def validate_course_id(self, value):
        try:
            return Course.objects.get(course_id=value)
        except Course.DoesNotExist:
            raise serializers.ValidationError("Course does not exist.")

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user

        # These are now MODEL INSTANCES (because validate_* returned them)
        student = validated_data.pop("student_id")
        course = validated_data.pop("course_id")

        # Teacher must teach this course
        if course.teacher != user.teacher:
            raise serializers.ValidationError(
                "You are not assigned to this course."
            )

        # Student must be enrolled
        if not Enrollment.objects.filter(
            student=student,
            course=course
        ).exists():
            raise serializers.ValidationError(
                "The student is not enrolled in the course."
            )

        # Prevent duplicate result
        if Result.objects.filter(
            student=student,
            course=course
        ).exists():
            raise serializers.ValidationError(
                "Result already exists for this student and course."
            )

        return Result.objects.create(
            student=student,
            course=course,
            **validated_data
        )

    student_id = serializers.CharField(write_only=True, required=False)
    course_id = serializers.CharField(write_only=True)

    class Meta:
        model = Result
        fields = [
            "id",
            "student_id",
            "course_id",
            "grade",
            "remark",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_student_id(self,value):
        try:
            return Student.objects.get(student_id=value)
        except Student.DoesNotExist:
            return serializers.ValidationError("Student does not exist. ")
        
    def validate_course_id(self,value):
        try:
            return Course.objects.get(course_id=value)
        except Course.DoesNotExist:
            return serializers.ValidationError("Course does not exist. ")
        
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        student = validated_data.pop("student_id")
        course = validated_data.pop("course_id")
        # Teacher must teach this course
        if course.teacher != user.teacher:
            return serializers.ValidationError("You are not assigned to this course.")
        # Student must be enrolled in the course
        if not Enrollment.objects.filter(student=student,course=course).exists():
            raise serializers.ValidationError("The student is not enrolled in the course")
        # Prevent duplicate result
        if Result.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("Result already exists for this student and course.")
        return Result.objects.create(
            student=student,
            course=course,
            **validated_data
        )
    
# Read serializer for dashboards
class ResultReadSerializer(serializers.ModelSerializer):
    student = StudentMiniSerializer(read_only=True)
    course = CourseMiniSerializer(read_only=True)

    class Meta:
        model = Result
        fields = [
            "id",
            "student",
            "course",
            "grade",
            "remark",
            "created_at",
        ]