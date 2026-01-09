# 🎓 Simplified University Course and Result Portal

A Django REST Framework–based backend system that allows **admins, teachers, and students** to manage courses, enrollments, and results in a university setting.

---

## 🚀 Project Overview

### Roles
- **Admin**
  - Creates students and teachers
  - Manages courses
  - Assigns teachers to courses
- **Teacher**
  - Views assigned courses
  - Views enrolled students
  - Uploads and updates results
- **Student**
  - Views available courses
  - Registers for courses
  - Views registered courses and results

---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- SQLite / PostgreSQL
- JWT / Session Authentication

---

## 📦 Project Structure
```
accounts/
courses/
enrollment/
results/
```

---

## 🔐 Authentication

### Login
```
POST /api/auth/login/
```
ADMIN
Request:
{
  "username": "abee",
  "password": "Ab@123!!!bb"
}
STUDENT
Request:
{
  "username": "burte",
  "password": "Ab@123!!bb"
}
TEACHER
Request:
{
  "username": "john",
  "password": "Ab@123!!bb"
}
---

## 👤 Accounts API

### Get All Users (Admin only)
```
GET /api/accounts/users/
```
### Create a student (Admin only)
POST /api/accounts/students/create/

### Create a teacher (Admin only)
POST /api/accounts/teachers/create/

## 📘 Courses API

### Get All Courses
```
GET /api/courses/
```

### Create Course (Admin only)
```
POST /api/courses/
```

### Update Course (Admin only)
```
PATCH /api/courses/{id}/
```
---

## 📝 Enrollment API

### Register Course (Student)
```
POST /api/register-course/
```


### Course Students (Teacher)
```
GET /api/course/{id}/students/
```

---
## 🧮 Enrollement API

### Enroll in course (Student)
```
POST /api/register-course/
```
{
    "course_id": "CRS0002"
}

### Enrolled Courses (Student)

GET api/student/courses/

### Students Enrolled (Teacher)

GET /api/course/2/students/

## 🧮 Results API

### Upload Result (Teacher)
```
POST /api/results/
```

### Update Result (Teacher)
```
PATCH /api/results/{id}/
```

### Student Results (Student)
```
GET /api/student/results/
```

### Course Results (Teacher)
```
GET /api/course/{id}/results/
```

---

## 🔒 Permissions Summary

| Role     | Access |
|--------|--------|
| Admin   | Full |
| Teacher | Own courses & results |
| Student | Courses & results |

---

## ⚙️ Setup Instructions

```bash
git clone <repo-url>
cd university-portal
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📌 Notes
- Student and Teacher IDs are auto-generated
- Foreign keys are used internally
- Role-based permissions enforced

---

## ✅ Project Status
✔ Accounts  
✔ Courses  
✔ Enrollment  
✔ Results  
✔ Permissions  

---

## 🎯 Future Improvements
- GPA calculation
- Semester system
- Transcript generation
- Frontend integration
