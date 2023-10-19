from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.create_room, name='create_room'),
    path('update-room/<str:pk>/', views.update_room, name='update_room'),
    path('delete-room/<str:pk>/', views.delete, name='delete_room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete_message'),
    path('user-profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('topics/', views.topics_page, name='topic_page'),
    path('activities/', views.activity_page, name='activity_page')

]