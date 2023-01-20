from django.http import HttpResponse


def bills(request):
    return HttpResponse("Hello, world. You're at the Bills index.")