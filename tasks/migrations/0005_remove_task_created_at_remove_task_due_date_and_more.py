# Generated by Django 5.1.3 on 2025-01-07 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='updated_at',
        ),
    ]
