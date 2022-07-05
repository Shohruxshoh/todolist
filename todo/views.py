from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def listTodo(request):
    list_todo = Todo.objects.all()
    context = {'list_todo':list_todo}
    return render(request, 'todo/home.html', context)

def createTodo(request):
    form = TodoForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('/')
    context = {
        "form":form
    }  
    return render(request, 'todo/create.html', context)

def updateTodo(request, pk):
    todo =Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'todo/update_todo.html', context)


def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todo/delete.html', context)