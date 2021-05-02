from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world!")


def system_monitoring(request):
    return render(request, 'dashboard.html', {})