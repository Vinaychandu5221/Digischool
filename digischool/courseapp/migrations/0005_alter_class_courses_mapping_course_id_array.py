# Generated by Django 4.0.1 on 2022-03-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0004_alter_available_courses_course_instructor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_courses_mapping',
            name='course_id_array',
            field=models.CharField(max_length=55),
        ),
    ]
