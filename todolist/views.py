from django.shortcuts import render, redirect
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
   tasks = todolist.all()           # Todolist.objects.all()
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

def create_tasks(request):
   if request.method == 'POST':
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      Todolist.objects.create(title = user_title, description = user_description)
      return redirect('/todolist/')
   return render(request,'create.html')

# {'title':"ram", 'description':"abc"}

def mark_complete(request,id):
   task = Todolist.objects.get(id = id)
   task.status = True
   task.save()
   return redirect('/todolist/')

def edit(request,id):
   task = Todolist.objects.get(id = id)
   if request.method == "POST":
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      task.title = user_title
      task.description = user_description
      task.save()
      return redirect('/todolist/')
   context = {"task":task}
   return render(request,'edit.html', context)

def delete(request, id):
   task = Todolist.objects.get(id = id)
   task.delete()
   return redirect('/todolist/')