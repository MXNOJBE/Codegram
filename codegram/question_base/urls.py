from django.urls import path
from . import views

app_name = 'codegram'

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    
    #CRUD Functions
    path('questions/', views.QuestionListView.as_view(), name ="question-lists")
    
]
