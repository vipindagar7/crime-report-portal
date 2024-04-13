from django.urls import path , include
from . import views
urlpatterns = [
  
    path('add/', views.newReport , name='new_report'), 
    path('edit/', views.editReport , name='edit_report'),
    path('cases/', views.cases , name='cases'),
    path('cases/<int:id>/', views.view_case , name='view_case'),
    

    
    
]
