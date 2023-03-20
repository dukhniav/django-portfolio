from django.contrib import admin
from django.urls import include, path
from home import views
from theme.views import change_theme


urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch-theme/', change_theme, name='change-theme'),
    path('', include('home.urls'), name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
]
