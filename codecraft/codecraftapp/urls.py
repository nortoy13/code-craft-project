from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<slug:slug>', NewsDetailView.as_view(), name='news_detail'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<slug:slug>', ProjectCategoryListView.as_view(), name='project_category'),
    path('courses/<slug:slug>', CourseDetailView.as_view(), name='course-detail'),
]
