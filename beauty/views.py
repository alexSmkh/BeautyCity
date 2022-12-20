from django.shortcuts import render, redirect
from .models import Salon, Procedure, Employee, Feedback, Category
from users.models import User
from users.forms import UserToCallForm


def index(request):
    salons = Salon.objects.all()
    procedures = Procedure.objects.all()
    employees = Employee.objects.all()
    feedbacks = Feedback.objects.all()
    context = {
        'salons': salons,
        'procedures': procedures,
        'employees': employees,
        'feedbacks': feedbacks,
        'is_authenticated': request.user.is_authenticated
    }

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
    categories = Category.objects.all()
    service_items = []

    context = {
        'salons': salons,
        'is_authenticated': request.user.is_authenticated
    }

    for category in categories:
        service_item = {
            category.name: {
                procedure.name: procedure.price for procedure in category.procedure.all()}
        }
        service_items.append(service_item)

    context['service_items'] = service_items

    return render(request, 'beauty/service.html', context)


def service_finally(request):
    return render(request, 'beauty/serviceFinally.html')


def notes(request):
    user=request.user
    if user.is_authenticated:
        user = User.objects.get(phonenumber = str(user.phonenumber))
        user_attrs = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': user.avatar
        }
    return render(request, 'beauty/notes.html', context = user_attrs)
