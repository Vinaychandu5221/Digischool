# Generated by Django 4.0.1 on 2022-03-24 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_initial'),
        ('loginapp', '0005_user_signup_database_verfied_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_signup_database',
            name='class_course_field',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='courseapp.class_courses_mapping'),
            preserve_default=False,
        ),
    ]
