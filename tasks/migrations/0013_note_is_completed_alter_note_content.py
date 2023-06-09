# Generated by Django 4.2 on 2023-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0012_remove_task_notes_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="note",
            name="content",
            field=models.CharField(max_length=200),
        ),
    ]
