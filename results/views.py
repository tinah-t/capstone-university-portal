from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from results.models import Result
from results.serializers import ResultSerializer, ResultReadSerializer
from accounts.permissions import IsTeacherOrAdmin, IsStudentOrAdmin

#  Teacher uploads a result
class UploadResultView(CreateAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsTeacherOrAdmin]


# Teacher updates a grade
class UpdateResultView(UpdateAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsTeacherOrAdmin]
    lookup_field = "id"

    def get_queryset(self):
        # Teacher can update results only for their courses
        return Result.objects.filter(course__teacher=self.request.user.teacher)

# Student views their results
class StudentResultsView(ListAPIView):
    serializer_class = ResultReadSerializer
    permission_classes = [IsStudentOrAdmin]

    def get_queryset(self):
        return Result.objects.filter(student=self.request.user.student).select_related(
            "student", "student__user", "course", "course__teacher", "course__teacher__user"
        )
    

# Teacher views results for their course
class CourseResultsView(ListAPIView):
    serializer_class = ResultReadSerializer
    permission_classes = [IsTeacherOrAdmin]

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Result.objects.filter(
            course__course_id=course_id,
            course__teacher=self.request.user.teacher
        ).select_related("student", "student__user", "course")