# Generated by Django 4.0.1 on 2022-03-24 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_user_signup_database_class_course_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_signup_database',
            name='class_course_field',
        ),
    ]
