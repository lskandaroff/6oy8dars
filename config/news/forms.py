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


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
