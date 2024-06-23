from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('home/', views.homepage, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('add_task', views.add_task, name='add_task'),
     path('toggle-task-status/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
]
