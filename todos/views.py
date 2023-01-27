from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt


from .forms import UserRegistrationForm, TodoForm
from .models import TodoItem, TodoCategory


'''
Based on https://medium.com/@nsew1999gokulcvan/create-a-to-do-application-with-user-authentication-and-pagination-in-django-be4a797b20e6
'''


@login_required
def todos_home(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'POST':
        title = request.POST.get("new-todo")
        category = request.POST.get("new-category")

        if category == '':
            category, created = TodoCategory.objects.get_or_create(
                title='General')
        else:
            category, created = TodoCategory.objects.get_or_create(
                title=category)

        todo = TodoItem.objects.create(
            title=title, category=category, user=request.user)
        return redirect("todos_home")

    # todo items
    todos = TodoItem.objects.filter(
        user=request.user, is_completed=False).order_by("-id")

    # pagination 4 items per page
    paginator = Paginator(todos, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"todos": todos, "page_obj": page_obj}

    # NOTE: Need to change the html file to crud.html for displaying the todo's
    return render(request, "todos/crud.html", context)


class SettingsView(ListView):
    template_name = 'todos/settings.html'
    context_object_name = 'category_list'
    queryset = TodoCategory.objects.all()


def todos_register(request):
    """
    User Registration form

    Args:
        request (POST): New user registered
    """
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos_login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "todos/register.html", context)


def logout_user(request):
    logout(request)
    return redirect("todos_login")


def update_todo(request, pk):
    """
    Update todo item

    Args:
        pk (Integer): Todo ID - primary key
    """
    # NOTE: below get_object_or_404() returns a data if exists else status 404 not found
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)

    # NOTE: request.POST.get("todo_{pk}") is the input name of the todo modal
    todo.title = request.POST.get(f"todo_{pk}")
    todo.save()
    # return redirect("home")
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
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
