# Generated by Django 4.2 on 2023-04-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_task_color"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="color",
        ),
        migrations.AddField(
            model_name="task",
            name="notes",
            field=models.TextField(default="none"),
        ),
    ]
