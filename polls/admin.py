from django.contrib import admin
from polls.models import Student
from polls.models import Lesson

from .models import Lesson

admin.site.register(Lesson)
admin.site.register(Student)
