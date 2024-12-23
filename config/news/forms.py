from django import forms
from .models import Course, Lesson

class LessonForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    type = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select())

class CourseForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())
    price = forms.IntegerField(widget=forms.NumberInput())
    photo = forms.ImageField(widget=forms.FileInput())

