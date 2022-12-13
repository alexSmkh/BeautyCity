from django.shortcuts import render


def index(request):
    return render(request, 'beauty/index.html')


def service(request):
    return render(request, 'beauty/service.html')