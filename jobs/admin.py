from django.contrib import admin

from .models import Job  # "." means the "models" file is in the same folder(current dir)  with "admin" file

from blog.models import Blog

# This is making that applications will show in the DB
# e.g. for "jobs" application the following line will do, including the line 3 :
admin.site.register(Job)

admin.site.register(Blog)
