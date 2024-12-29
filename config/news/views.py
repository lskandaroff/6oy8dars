from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import LessonForm, CourseForm, RegisterForm, LoginForm
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Course, Lesson

def home(request):
 courses = Course.objects.all()

 context = {
  "courses": courses,
  'title': "Barcha maqolalar"
 }

 return render(request, 'home.html', context)

def about_1_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    context = {
        'lesson': lesson
    }

    return render(request, 'about_1_lesson.html', context)


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
         messages.success(request, 'Maqola qoshildi!!!')
         return redirect('about_lessons', course_id=lesson.type.id)


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


def update_lesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == "POST":
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson.name = form.cleaned_data.get('name')
            lesson.description = form.cleaned_data.get('description')
            lesson.type = form.cleaned_data.get('type')
            lesson.save()
            messages.success(request, 'Maqola ozgartirildi')



    forms = LessonForm(initial={
        'name': lesson.name,
        'description': lesson.description,
        'type': lesson.type
    })

    context = {
        'forms': forms,
    }

    return render(request, 'add_lesson.html', context)

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, 'Maqola ochirildi')
        return redirect('home')

    context = {
        'lesson': lesson
    }
    return render(request, 'confirm_delete.html', context)



def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Royxatdan otildi')
                return redirect('login')

    context = {
        'form': RegisterForm()
    }

    return render(request, 'auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, 'Xush kelibsiz')
            login(request, user)
            return redirect('home')
    context = {
        'form': LoginForm()
    }

    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')



































