from rest_framework.generics import CreateAPIView, ListAPIView
from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer, EnrollmentStudentReadSerializer, EnrollmentTeacherReadSerializer
from accounts.permissions import IsStudentOrAdmin , IsTeacherOrAdmin


# Student registers for a course
class RegisterCourseView(CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudentOrAdmin]

# Student views their registered courses
class StudentCoursesView(ListAPIView):
    serializer_class = EnrollmentStudentReadSerializer
    permission_classes = [IsStudentOrAdmin]
    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user.student).select_related("course")
    

# Teacher views students in their course
class CourseStudentsView(ListAPIView):
    serializer_class = EnrollmentTeacherReadSerializer
    permission_classes = [IsTeacherOrAdmin]
    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Enrollment.objects.filter(
            course__id=course_id,
            course__teacher=self.request.user.teacher
        ).select_related("student", "student__user")    