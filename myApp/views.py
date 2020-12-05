from django.shortcuts import render, HttpResponse
from django.utils import timezone
from myApp.models import  Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('added_date' )
    return  render(request,"myApp/index.html")

def add_todo(request):
    print(request.POST)
    current_data = timezone.now()
    content = request.POST.get("content")
    
    
    Created_obj = Todo.objects.create(text=content, added_date=current_data)
    
    legth_of_todos = Todo.objects.all().count()
    
    return  render(request,"myApp/index.html")
