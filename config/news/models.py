from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='post/photos', blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
