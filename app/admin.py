from django.contrib import admin
from .models import Author, Assignee, Project, File, Issue

admin.site.register(Author)
admin.site.register(Assignee)
admin.site.register(Project)
admin.site.register(File)
admin.site.register(Issue)