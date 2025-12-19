from rest_framework import serializers
from results.models import Result
from courses.serializers import CourseMiniSerializer
from accounts.serializers import StudentMiniSerializer
from accounts.models import Student, Course

class ResultSerializer(serializers.ModelSerializer):
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
    class validate_student_id(self,value):
        Student.objects.