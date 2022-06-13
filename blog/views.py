from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from blog.models import Todo

def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render(request, 'simpleTodo.html',{
        'todolist':todolist, 'finishtodos':finishtodos
    })

def todofinish(request):
    id=request.GET.get('id','')
    # if id== '':
        # return HttpResponseRedirect('/todolist')

    todo = Todo.objects.get(id=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
    return HttpResponseRedirect('/todolist')

def todoback(request):
    id=request.GET.get('id','')
    if id=='':
        return HttpResponseRedirect('/todolist')
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
    return HttpResponseRedirect('/todolist')

def todoadd(request):
    if request.method=='POST':
        todoc = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=todoc, priority=priority,flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'simpleTodo.html',{
            'todolist':todolist, 'finishtodos':finishtodos
        })
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'simpleTodo.html',{
            'todolist':todolist, 'finishtodos':finishtodos
        })

def tododelete(request):
    id = request.GET.get('id','')
    if id=='':
        return HttpResponseRedirect('/todolist')
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todolist')
    todolist = Todo.objects.filter(flag=1)
    return render(request, 'simpleTodo.html',{
        'todolist':todolist
    })
