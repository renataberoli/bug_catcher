# Generated by Django 3.2.12 on 2022-02-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='creation_date',
            field=models.DateTimeField(null=True),
        ),
    ]
