# Generated by Django 4.1.2 on 2022-11-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apitask", "0002_task_updated_at"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="description",),
        migrations.RemoveField(model_name="task", name="title",),
        migrations.AddField(
            model_name="task",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
    ]
