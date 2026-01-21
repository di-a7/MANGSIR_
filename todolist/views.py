from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist
# Create your views here.
def home(request):
   people_data = [
      {"name": "Diya", "age": 23, "gender": "Female"},
      {"name": "Aarav", "age": 55, "gender": "Male"},
      {"name": "Sita", "age": 30, "gender": "Female"},
      {"name": "Rohan", "age": 68, "gender": "Male"},
      {"name": "Maya", "age": 12, "gender": "Female"}
   ]
   
   context = {
      "title":"Home",
      "people": people_data
   }
   return render(request, 'home.html', context)


def about_us(request):
   return render(request,'about_us.html')

# about_us, contact_us, our_team, form, form_edit

def todolist(request):
   todolist = Todolist.objects
   tasks = todolist.all()
   total = tasks.count()
   completed = todolist.filter(status = True).count()
   incompleted = todolist.filter(status = False).count()
   
   context = {
      "tasks": tasks,
      "total":total,
      "completed": completed,
      "incomplete": incompleted
   }
   
   return render(request, 'todolist.html', context) 