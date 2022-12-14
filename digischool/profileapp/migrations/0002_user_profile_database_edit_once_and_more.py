# Generated by Django 4.0.1 on 2022-03-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_database',
            name='edit_once',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_profile_database',
            name='father_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='user_profile_database',
            name='mother_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='user_profile_database',
            name='user_profile_photo',
            field=models.FileField(default='profile_photo.jpg', null=True, upload_to='image/', verbose_name=''),
        ),
    ]
