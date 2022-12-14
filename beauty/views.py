from django.shortcuts import render


def index(request):
    return render(request, 'beauty/index.html')


def service(request):
    return render(request, 'beauty/service.html')


def service_finally(request):
    return render(request, 'beauty/serviceFinally.html')