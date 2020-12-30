from django.urls import path
from django.views.generic import TemplateView
from . import views

#app_name = 'Board'
urlpatterns = [
    path('',TemplateView.as_view(template_name = 'index.html'),name='index'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('all_list',views.AllListView.as_view(),name='all_list'),
    path('list/',views.ListView.as_view(),name='list'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('home/',views.HomeListView.as_view(),name='home'),
    path('profile/<int:pk>/',views.UpdateProfileView.as_view(),name='profile'),
    path('other/<str:username>/',views.OtherListView.as_view(),name='other'),
    path('create_follow/<str:follow_username>',views.create_follow,name='create_follow'),
    path('delate_follow/<str:follow_username>',views.delete_follow,name='delete_follow'),
    path('tweet/',views.CreateTweetView.as_view(),name='tweet'),
]
