from django.shortcuts import render
from django.views.generic import ListView
#from .models import Question
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

#CRUD
 
#class QuestionListView(ListView):
    #model = Question