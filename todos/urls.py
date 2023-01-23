from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView


from . import views

urlpatterns = [
    path('', views.todos_home, name='todos_home'),
    path('register/', views.todos_register, name='todos_register'),
    path('login/', LoginView.as_view(template_name='todos/login.html'), name='todos_login'),
    path('logout/', LogoutView.as_view(template_name='todos/logout.html'), name='todos_logout'),

    path("update/todo/<int:pk>/", views.update_todo, name="update_todo"),
    path("complete/todo/<int:pk>/", views.complete_todo, name="complete_todo"),
    path("delete/todo/<int:pk>/", views.delete_todo, name="delete_todo"),

]