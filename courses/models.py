from django.db import models
from accounts.models import Teacher

# ======================
# Utility for Course ID
# ======================
def generate_course_id(last_id):
    if not last_id:
        return "CRS0001"
    number = int(last_id.replace("CRS", ""))
    return f"CRS{number + 1:04d}"


class Course(models.Model):
    course_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False
    )
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    credit_hours = models.PositiveIntegerField()

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.course_id:
            last_course = Course.objects.order_by("-id").first()
            last_id = last_course.course_id if last_course else None
            self.course_id = generate_course_id(last_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course_code} - {self.name}"