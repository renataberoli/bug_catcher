from django.contrib import admin
from .models import  Project, File, Issue

admin.site.register(Project)
admin.site.register(File)
admin.site.register(Issue)