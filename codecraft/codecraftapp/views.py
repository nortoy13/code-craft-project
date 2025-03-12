from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, TemplateView, ListView, FormView
from .forms import ApplicationForm, OpenLessonForm

from .models import *


# Create your views here.
class HomeView(TemplateView):
    template_name = 'codecraftapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.all()
        context["groups"] = Group.objects.all()
        return context


class AboutView(CreateView):
    model = OpenLesson
    template_name = 'codecraftapp/about.html'
    success_url = reverse_lazy('home')
    form_class = OpenLessonForm


class NewsListView(ListView):
    model = News
    template_name = 'codecraftapp/news.html'
    context_object_name = 'news'
    ordering = ['-created_time']



class NewsDetailView(DetailView):
    model = News
    template_name = 'codecraftapp/newsInner.html'
    context_object_name = 'news'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_news'] = News.objects.exclude(slug=self.object.slug).order_by('-created_time')
        return context



class ContactView(CreateView):
    model = Application
    template_name = 'codecraftapp/contact.html'
    success_url = reverse_lazy('home')
    form_class = ApplicationForm


class ProjectListView(ListView):
    model = Project
    template_name = 'codecraftapp/projects.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        return context



class ProjectCategoryListView(ListView):
    model = Project
    template_name = 'codecraftapp/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.project_category = get_object_or_404(ProjectCategory, slug=slug)
        return Project.objects.filter(category=self.project_category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['project_category'] = self.project_category
        return context


class CourseDetailView(DetailView, FormView):
    model = Course
    template_name = 'codecraftapp/courses.html'
    context_object_name = 'course'
    form_class = OpenLessonForm

    def get_object(self, queryset=None):
        return get_object_or_404(Course, slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context["results"] = CourseResults.objects.filter(course=course.pk)
        context["prices"] = CoursePrice.objects.filter(course=course.pk)
        context["faqs"] = Faq.objects.all()
        context["openLessons"] = CourseOpenLessons.objects.filter(course=course.pk)
        return context

    def form_valid(self, form):
        form.save()
        return redirect('home')

