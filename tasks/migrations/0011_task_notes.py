# Generated by Django 4.2 on 2023-04-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0010_remove_task_notes_alter_task_due_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="notes",
            field=models.TextField(null=True),
        ),
    ]