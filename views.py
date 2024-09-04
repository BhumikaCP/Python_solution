from django.shortcuts import render
from .models import Student
def search_courses(request):
    if request.method == 'GET' and 'student_name' in request.GET:
        student_name = request.GET['student_name']
        student = Student.objects.filter(name__icontains=student_name).first()
        courses = student.courses.all()
    else:
        courses = []
        return render(request, 'search_app/course_list.html', {'courses': courses})
    return render(request, 'search_app/search_form.html')