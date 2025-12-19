from django.db import models
from accounts.models import Student
from courses.models import Course


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name="results")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="results")
    grade = models.CharField(max_length=5)  # e.g., A, B+, 90
    remark = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.student_id} - {self.course.course_code}: {self.grade}"