from django.shortcuts import render, get_object_or_404

from .models import Course, Lesson

def home(request):
 courses = Course.objects.all()

 context = {
  "courses": courses,
  'title': "Barcha maqolalar"
 }

 return render(request, 'home.html', context)


def about_lessons(request, course_id):
 lessons = get_object_or_404(Lesson, id=course_id)


 context = {
  'lessons': lessons,
 }

 return render(request, 'details.html', context)
