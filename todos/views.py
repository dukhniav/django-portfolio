from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from .forms import UserRegistrationForm, TodoForm
from .models import TodoItem


'''
Based on https://medium.com/@nsew1999gokulcvan/create-a-to-do-application-with-user-authentication-and-pagination-in-django-be4a797b20e6
'''

def todos_register(request):
    '''
    User registration form
    
    Args:
        request (POST): New User registered
    '''
    form = UserRegistrationForm
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos/login')
        else:
            form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'todos/register.html',context)

@login_required
def todos_home(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        todo_name = request.POST.get("new-todo")
        todo = TodoItem.objects.create(name=todo_name, user=request.user)
        return redirect("home")

    # retrieving todo items which are incomplete
    todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("-id")

    # paginating 4 items per page
    paginator = Paginator(todos, 4)
    
    # It's URL param for getting the current page number
    page_number = request.GET.get("page")
    
    # retrieving all the todo items for that page
    page_obj = paginator.get_page(page_number)

    context = {"todos": todos, "page_obj": page_obj}
    return render(request, "todo/crud.html", context)


def update_todo(request, pk):
    """
    Update todo item
    Args:
        pk (Integer): Todo ID - primary key
    """
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    # NOTE: request.POST.get("todo_{pk}") is the input name of the todo modal
    todo.name = request.POST.get(f"todo_{pk}")
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_todo(request, pk):
    """
    Delete todo item
    Args:
        pk (Integer): Todo ID - Primary key
    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete_todo(request, pk):
    """
    Updating todo as completed item
    Args:
        pk (Integer): Todo ID - primary key
    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))