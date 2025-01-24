# Generated by Django 5.1.4 on 2025-01-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("softskills", "0002_alter_question_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalsoftskilltraining",
            name="max_range",
        ),
        migrations.RemoveField(
            model_name="historicalsoftskilltraining",
            name="min_range",
        ),
        migrations.RemoveField(
            model_name="softskilltraining",
            name="max_range",
        ),
        migrations.RemoveField(
            model_name="softskilltraining",
            name="min_range",
        ),
        migrations.AddField(
            model_name="historicalsoftskilltraining",
            name="max_grade",
            field=models.PositiveIntegerField(default=0, verbose_name="max grade"),
        ),
        migrations.AddField(
            model_name="historicalsoftskilltraining",
            name="min_grade",
            field=models.PositiveIntegerField(default=0, verbose_name="min grade"),
        ),
        migrations.AddField(
            model_name="softskilltraining",
            name="max_grade",
            field=models.PositiveIntegerField(default=0, verbose_name="max grade"),
        ),
        migrations.AddField(
            model_name="softskilltraining",
            name="min_grade",
            field=models.PositiveIntegerField(default=0, verbose_name="min grade"),
        ),
    ]
