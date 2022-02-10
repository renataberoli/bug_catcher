from django.db import models


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


class Author(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email


class Assignee(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email


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
    description = models.TextField(max_length=5000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    attached_file = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default='open')
    label = models.CharField(max_length=200, choices=LABELS, null=True)
    creation_date = models.DateTimeField(null=True)
    priority = models.CharField(max_length=100, choices=PRIORITY, blank=True)

    def __str__(self):
        return self.title
