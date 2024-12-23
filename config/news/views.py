from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import LessonForm, CourseForm

from .models import Course, Lesson

def home(request):
 courses = Course.objects.all()

 context = {
  "courses": courses,
  'title': "Barcha maqolalar"
 }

 return render(request, 'home.html', context)


def about_lessons(request, course_id):
 lessons = Lesson.objects.filter(type_id=course_id)


 context = {
  'lessons': lessons,
 }

 return render(request, 'details.html', context)

def add_lesson(request: WSGIRequest):

 if request.method == 'POST':
     form = LessonForm(data=request.POST, files=request.FILES)
     if form.is_valid():
         lesson = Lesson.objects.create(**form.cleaned_data)
         print(lesson, 'qoshildi!')


 forms = LessonForm()
 context = {
  'forms': forms
 }
 return render(request, 'add_lesson.html', context)

def add_course(request: WSGIRequest):

 if request.method == 'POST':
     form = CourseForm(data=request.POST, files=request.FILES)
     if form.is_valid():
         course = Course.objects.create(**form.cleaned_data)
         print(course, 'qoshildi!')


 forms = CourseForm()
 context = {
  'forms': forms
 }
 return render(request, 'add_course.html', context)

