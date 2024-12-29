from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('lessons/<int:course_id>/', about_lessons, name="about_lessons"),
    path('lessons/<int:lesson_id>/update/', update_lesson, name='update_lesson'),
    path('lessons/<int:lesson_id>/delete/', delete_lesson, name='delete_lesson'),
    path('about_1_lesson/<int:lesson_id>/', about_1_lesson, name='about_1_lesson'),
    path('lesson/add/', add_lesson, name='add_lesson'),
    path('course/add/', add_course, name='add_course'),
    path('auth/register/', register, name='register'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    ]


