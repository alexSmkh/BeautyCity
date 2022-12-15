from django.shortcuts import render, redirect
from .models import Salon
from users.forms import UserToCallForm


def index(request):
    context = {}
    if request.method == 'POST':
        form = UserToCallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = UserToCallForm()
    context['form'] = form
    return render(request, 'beauty/index.html', context)


def service(request):
    salons = Salon.objects.all()
    context = {
        'salons': salons,
    }

    return render(request, 'beauty/service.html', context)


def service_finally(request):
    return render(request, 'beauty/serviceFinally.html')


def notes(request):
    return render(request, 'beauty/notes.html')