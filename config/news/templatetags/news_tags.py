from django import template


from ..models import Course, Lesson




register = template.Library()

@register.simple_tag
def all_courses():
    return Course.objects.all()

@register.simple_tag
def all_lessons():
    return Lesson.objects.all()