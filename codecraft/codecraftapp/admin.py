from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ApplicationCategory)
admin.site.register(ProjectCategory)
admin.site.register(Technology)
admin.site.register(Testimonial)
admin.site.register(CourseTag)
admin.site.register(CourseResults)
admin.site.register(Faq)
admin.site.register(Group)
admin.site.register(CoursePrice)
admin.site.register(CourseOpenLessons)
admin.site.register(LessonTime)


@admin.register(OpenLesson)
class OpenLessonAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'created_time')
    readonly_fields = ('created_time',)
    search_fields = ('fullname', 'phone')
    list_filter = ('created_time',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'created_time')
    readonly_fields = ('created_time',)
    search_fields = ('fullname', 'phone')
    list_filter = ('created_time',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time')
    readonly_fields = ('created_time',)
    search_fields = ('title', 'content')
    list_filter = ('created_time',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'technologies')
    list_filter = ('category', 'technologies')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'course_tag')
    list_filter = ('category', 'created_at')
