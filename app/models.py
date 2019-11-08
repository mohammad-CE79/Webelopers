from django.db import models
from django.forms import ModelForm


class Course(models.Model):
    department = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=[0, 1, 2, 3, 4])
    second_day = models.IntegerField(choices=[0, 1, 2, 3, 4])


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number',
                  'teacher', 'start_time', 'end_time', 'first_day', 'second_day']
