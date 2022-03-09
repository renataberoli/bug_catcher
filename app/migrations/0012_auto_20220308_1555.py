# Generated by Django 3.2.12 on 2022-03-08 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220225_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='creation_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='issue',
            name='label',
            field=models.CharField(blank=True, choices=[('operational', 'Operational'), ('frontend', 'Front-end'), ('backend', 'Back-end'), ('design', 'Design')], max_length=200),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('closed', 'Closed'), ('pending', 'Pending')], default='open', max_length=100),
        ),
    ]
