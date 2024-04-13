from django.urls import path , include
from . import views
urlpatterns = [
  
    path('newuser/', views.newuser , name='newuser'), 
    path('login/', views.login_view , name='login'), 
    path('logout/', views.logout_view , name='logout'), 
    path('dashboard/', views.dashboard , name='dashboard'), 
    path('create_inspector/', views.create_inspector , name='create_inspector'), 
    path('manage_users/', views.manage_user , name='manage_user'), 
    path('manage_users/<int:id>/', views.view_user , name='view_user'), 
    path('delete/<int:id>/', views.delete_user , name='delete_user'), 
    path('update_user/<int:id>/', views.update_user , name='update_user'), 
    path('verify/<str:auth_token>', views.verify , name='verify'), 

]
