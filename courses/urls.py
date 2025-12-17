from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = router.urls

# Admin creates course
# POST /api/courses/

# {
#   "name": "Database Systems",
#   "course_code": "CS302",
#   "credit_hours": 3
# }
# --------------
# Admin assigns teacher
# PATCH /api/courses/1/

# {
#   "teacher_id": "TCH0002"
# }
# ------------------
# Student views courses
# GET /api/courses/