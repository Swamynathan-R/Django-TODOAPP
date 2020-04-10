from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import TODO
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'base.html')

def operations(request):
    todo_items=TODO.objects.all().order_by("added_date")
    return render(request,'Todo.html',{
        "todo_items":todo_items
    })

def add_todo(request):
    searched_date=timezone.now()
    content=request.POST["searchcontent"]
    created_object=TODO.objects.create(added_date=searched_date,text=content)
    length=TODO.objects.all().count()
    return HttpResponseRedirect("/Todo")

def delete_todo(request,todo_id):
    TODO.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/Todo")
