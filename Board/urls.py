from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'index.html'),name='index'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('list/',views.ListView.as_view(),name='list'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('home/',views.HomeListView.as_view(),name='home'),
]
