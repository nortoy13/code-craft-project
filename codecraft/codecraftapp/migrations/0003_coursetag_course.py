# Generated by Django 5.1.6 on 2025-02-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codecraftapp', '0002_news_slug_alter_news_title_alter_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/courses/')),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('is_free', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course_tag', models.ManyToManyField(related_name='courses', to='codecraftapp.coursetag')),
            ],
        ),
    ]
