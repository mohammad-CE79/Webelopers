from django.contrib import admin

from app.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
