import datetime

from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment, DayOfWork
from .models import Salon, Procedure, Employee, Feedback, Category
from users.models import User
from users.forms import UserToCallForm
from .serializers import EmployeeAppointmentDetailSerializer, RequestAvailableTimeSerializer, \
    RequestMastersForAppointmentDetailSerializer, ServiceCategoryAppointmentDetailSerializer
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
                procedure.name: procedure.price for procedure in category.services.all()}
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

    master_ids = DayOfWork.objects.filter(
        salons__id=request_serializer.data['salon_id'],
        employees__category_id=request_serializer.data['category_id'],
    ).distinct().values_list('employees', flat=True)

    masters = Employee.objects.filter(id__in=master_ids)
    serializer = EmployeeAppointmentDetailSerializer(masters, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def get_available_time(request):
    request_serializer = RequestAvailableTimeSerializer(request.query_params)

    try:
        employee_word_day = DayOfWork.objects.get(
            salons_id=request_serializer.data['salon_id'],
            employees_id=request_serializer.data['master_id'],
            day_of_week=request_serializer.data['weekday']
        )
    except DayOfWork.DoesNotExist:
        return Response([])

    if not employee_word_day.ready:
        return Response([])

    appointments = Appointment.objects.filter(
        employee_id=request_serializer.data['master_id'],
        salon_id=request_serializer.data['salon_id'],
        date=request_serializer.data['date']
    ).values_list('appointment_hour', flat=True)

    time_begins = set(map(lambda time: time.split(' - ')[0], appointments))
    free_times = list(Appointment.day_times.difference(time_begins))
    free_sorted_times = sorted(free_times, key=lambda time: datetime.datetime.strptime(time, '%H:%M'))
    return Response(free_sorted_times)


def service_finally(request):
    pass


def notes(request):
    user = request.user
    if user.is_authenticated:
        user = User.objects.get(phonenumber = str(user.phonenumber))
        user_attrs = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': user.avatar
        }
    return render(request, 'beauty/notes.html', context=user_attrs)


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Вы ввели некорректные данные. Пожалуйста, попробуйте еще раз.')
            return redirect('beauty:service')

        form.save()
        messages.success(request, 'Вы успешно записались на прием.')
        return redirect('beauty:index')

    return redirect('beauty:index')
