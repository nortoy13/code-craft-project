# Generated by Django 5.1.6 on 2025-03-12 10:10

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codecraftapp', '0020_remove_courseopenlessons_weekdays_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 12, 10, 7, 44, 850463, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openlesson',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
