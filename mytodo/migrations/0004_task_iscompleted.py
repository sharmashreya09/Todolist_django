# Generated by Django 4.1.2 on 2022-11-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0003_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
