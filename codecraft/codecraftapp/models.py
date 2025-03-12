from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/news/%Y/%m/%d/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})


class ApplicationCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Application(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(region='UZ')
    category = models.ForeignKey(ApplicationCategory, on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class OpenLesson(models.Model):
    fullname = models.CharField(max_length=100)
    phone = PhoneNumberField(region='UZ')
    question = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class ProjectCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_category', kwargs={'slug': self.slug})


class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='photos/technology_icons/')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=350)
    url = models.URLField()
    image = models.ImageField(upload_to='photos/project_images/')
    technologies = models.ManyToManyField(Technology, related_name='projects')
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/testimonials/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseTag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Teg nomi

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField()
    course_program = models.TextField(default='Kurs dasturi haqida malumot')
    image = models.ImageField(upload_to='photos/courses/')
    video_photo = models.ImageField(upload_to='photos/courses/', default='pageVideo.jpg')
    video_url = models.URLField(default="https://www.youtube.com/watch?v=s3EyW4UIHLo")
    category = models.CharField(max_length=100)
    course_tag = models.ManyToManyField(CourseTag, related_name='courses')
    lessons = models.IntegerField(default=30)
    practice = models.IntegerField(default=30)
    portfolio_projects = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class CourseResults(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='results')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/course-results/')

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class CoursePrice(models.Model):
    type = models.CharField(max_length=200)
    price = models.IntegerField(default=800000)
    content = models.TextField()
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prices')

    def __str__(self):
        return f"{self.course.title} - {self.type}"


class LessonTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class CourseOpenLessons(models.Model):
    WEEKDAYS = [
        ('Dushanba', _('Dushanba')),
        ('Seshanba', _('Seshanba')),
        ('Chorshanba', _('Chorshanba')),
        ('Payshanba', _('Payshanba')),
        ('Juma', _('Juma')),
        ('Shanba', _('Shanba')),
        ('Yakshanba', _('Yakshanba')),
    ]
    weekdays = MultiSelectField(choices=WEEKDAYS, max_length=100)
    online_or_offline = models.CharField(max_length=255)
    date = models.DateTimeField()
    times = models.ManyToManyField(LessonTime, related_name="lessons")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}-{self.course.title}"


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Group(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/groups/')

    def __str__(self):
        return self.name
