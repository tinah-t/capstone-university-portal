from accounts.serializers import StudentMiniSerializer
from courses.models import Course
from .models import Enrollment
from rest_framework import serializers
from courses.serializer import CourseMiniSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(write_only=True)
    class Meta:
        model = Enrollment
        fields = [
            'id',
            'course_id',
            'registration_date'
            ]
        read_only_fields = ['id', 'registration_date']
    
    def validate_course_id(self, value):
        try:
            return Course.objects.get(course_id=value)
        except Course.DoesNotExist:
            raise serializers.ValidationError("Course does not exist.")
        
    def create(self, validated_data):
        course = validated_data.pop('course_id')
        student = self.context["request"].user.student

        if Enrollment.objects.filter(student=student,course=course).exists():
             raise serializers.ValidationError("Already registered for this course.")
        return Enrollment.objects.create(student=student,course=course)
        

class EnrollmentStudentReadSerializer(serializers.ModelSerializer):
    course = CourseMiniSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "course",
            "registration_date",
        ]

class EnrollmentTeacherReadSerializer(serializers.ModelSerializer):
    student = StudentMiniSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "registration_date",
        ]
