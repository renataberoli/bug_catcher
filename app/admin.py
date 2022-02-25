from django.contrib import admin
from .models import Assignee, Project, File, Issue

admin.site.register(Assignee)
admin.site.register(Project)
admin.site.register(File)
admin.site.register(Issue)
