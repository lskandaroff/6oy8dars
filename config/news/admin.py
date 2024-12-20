from django.contrib import admin
from .models import Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    list_display_links = ('name', 'id')
    list_editable = ('price', )
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top = False
    readonly_fields = ('views',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
