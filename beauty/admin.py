from django.contrib import admin
from users.models import User, UserToCall
from .models import Procedure, Employee, Salon, Appointment, Category, Feedback, DayOfWork


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    pass


class WorkDayInline(admin.TabularInline):
    model = DayOfWork
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [WorkDayInline]


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(UserToCall)
class UserToCall(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(DayOfWork)
class DayOfWorkAdmin(admin.ModelAdmin):
    pass