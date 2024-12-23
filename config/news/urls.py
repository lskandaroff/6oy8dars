from django.urls import path

from .views import home, about_lessons, add_lesson, add_course

urlpatterns = [
    path('', home, name="home"),
    path('lessons/<int:course_id>/', about_lessons, name="about_lessons"),
    path('lesson/add/', add_lesson, name='add_lesson'),
    path('course/add/', add_course, name='add_course')
    ]