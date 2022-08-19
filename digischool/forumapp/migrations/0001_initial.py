# Generated by Django 4.0.1 on 2022-03-24 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseapp', '0003_available_courses_forum_series_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALL_FORUMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_title', models.CharField(max_length=100)),
                ('forum_question', models.JSONField()),
                ('forum_datetime', models.DateTimeField(auto_now_add=True)),
                ('forum_unique_id', models.CharField(max_length=12)),
                ('forum_answers', models.JSONField()),
                ('course_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.available_courses')),
            ],
        ),
    ]
