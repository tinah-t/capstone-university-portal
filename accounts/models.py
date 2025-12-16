from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
    role = models.CharField(max_length=20, choices=Role.choices)
    
# ======================
# Managers
# ======================

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__role=User.Role.STUDENT)

class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__role=User.Role.TEACHER)
# ======================
# Utility for ID generation
# ======================
def generate_id(prefix, last_id):
    if not last_id:
        return f"{prefix}0001"
    number = int(last_id.replace(prefix, ""))
    return f"{prefix}{number + 1:04d}"

# ======================
# Student Model
# ======================
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    student_id = models.CharField(max_length=10, unique=True, editable=False)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = StudentManager()

    def save(self, *args, **kwargs):
        if not self.student_id:
            last_student = Student.objects.order_by("-id").first()
            last_id = last_student.student_id if last_student else None
            self.student_id = generate_id("STU", last_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student_id

# ======================
# Teacher Model
# ======================
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")

    teacher_id = models.CharField(max_length=10, unique=True, editable=False)

    objects = TeacherManager()

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            last_teacher = Teacher.objects.order_by("-id").first()
            last_id = last_teacher.teacher_id if last_teacher else None
            self.teacher_id = generate_id("TCH", last_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.teacher_id