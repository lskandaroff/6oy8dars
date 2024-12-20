from django.urls import path

from .views import home, about_lessons

urlpatterns = [
    path('', home, name="home"),
    path('lessons/<int:course_id>/', about_lessons, name="about_lessons")
    ]