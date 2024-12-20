from django.db import models

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
