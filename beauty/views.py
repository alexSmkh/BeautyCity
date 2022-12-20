from http import HTTPStatus
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers import serialize

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Salon, Procedure, Employee, Feedback
from .models import Salon, Procedure, Employee, Feedback, Category
from users.models import User
from users.forms import UserToCallForm
from .serializers import EmployeeAppointmentDetailSerializer, RequestMastersForAppointmentDetailSerializer, \
    SalonAppointmentDetailSerializer, \
    ServiceCategoryAppointmentDetailSerializer
from .forms import AppointmentForm


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
    return render(request, 'beauty/service.html', context=context)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = ServiceCategoryAppointmentDetailSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_masters(request):
    request_serializer = RequestMastersForAppointmentDetailSerializer(request.query_params)
    masters = Employee.objects.filter(
        salon_id=request_serializer.data['salon_id'],
        category_id=request_serializer.data['category_id'],
    )

    serializer = EmployeeAppointmentDetailSerializer(masters, many=True)

    return Response(data=serializer.data)


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


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if not form.is_valid():
            return redirect('service')

        form.save()
        return redirect('index')

    return redirect('index')
