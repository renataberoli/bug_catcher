from django.db import models
from django.conf import settings


STATUS = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('pending', 'Pending'),
)

LABELS = (
    ('operational', 'Operational'),
    ('frontend', 'Front-end'),
    ('backend', 'Back-end'),
    ('design', 'Design'),
)

PRIORITY = (
    ('1', 'Urgent'),
    ('2', 'High'),
    ('3', 'Normal'),
    ('4', 'Low'),
)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to=None, max_length=1000)

    def __str__(self):
        return self.name


class Issue(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='assignee')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    attached_file = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='open', blank=True)
    label = models.CharField(max_length=200, choices=LABELS, blank=True)
    creation_date = models.DateTimeField(blank=True)
    priority = models.CharField(max_length=100, choices=PRIORITY, blank=True)

    def __str__(self):
        return self.title
