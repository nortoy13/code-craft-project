from .models import *
from modeltranslation.translator import register, TranslationOptions


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(ApplicationCategory)
class ApplicationCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('subject', 'text')


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'course_program',)


@register(CourseResults)
class CourseResultTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


@register(CoursePrice)
class CoursePriceTranslationOptions(TranslationOptions):
    fields = ('type', 'content', 'body')


@register(CourseOpenLessons)
class CourseOpenLessonsTranslationOptions(TranslationOptions):
    fields = ('online_or_offline',)
