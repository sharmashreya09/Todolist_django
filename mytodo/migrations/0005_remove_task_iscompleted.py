# Generated by Django 4.1.2 on 2022-11-02 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0004_task_iscompleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='isCompleted',
        ),
    ]