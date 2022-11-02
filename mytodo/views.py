

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from mytodo.models import Task

def index(request):
    todos=Task.objects.all()
    cont={'todo':todos}
    return render(request,'index.html',cont)



def addTodo(request):
    if request.method=='POST':
        title=request.POST['title']
        obj = Task.objects.create(title=title)

    todo=Task.objects.all()
    context={'todo':todo}
    return render(request,'index.html',context)

def deleteTodo(request,title):
    y = Task.objects.get(title=title)
    y.delete()
    todo=Task.objects.all()
    cont={'todo':todo}
    return render(request,'index.html',cont)






