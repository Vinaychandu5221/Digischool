# Generated by Django 4.0.1 on 2022-03-29 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0005_alter_class_courses_mapping_course_id_array'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_courses',
            name='news_series_number',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ALL_ANOUNCEMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_description', models.TextField()),
                ('news_datetime', models.DateTimeField(auto_now_add=True)),
                ('news_unique_id', models.CharField(max_length=12)),
                ('course_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseapp.available_courses')),
            ],
        ),
    ]
