from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Category(models.Model):
    name = models.CharField(
        'Категория',
        max_length=25
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Procedure(models.Model):
    name = models.CharField(
        'название',
        max_length=50,
    )
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(0)]
    )
    image = models.FileField(
        'картинка',
        null=True,
        upload_to='media/',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='services',
        default=None,
        verbose_name='Категории'
    )

    def __str__(self):
        return f'{self.name}. {self.price}'

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'


class Employee(models.Model):

    name = models.CharField(
        'Имя',
        max_length=50
    )
    surname = models.CharField(
        'Фамилия',
        max_length=80
    )
    avatar = models.FileField(
        'аватар',
        null=True,
        upload_to='media/',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Специальность'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Salon (models.Model):

    name = models.CharField(
        'Название',
        max_length=50
    )
    address = models.CharField(
        'Адрес',
        max_length=100,
        blank=True
    )
    image = models.FileField(
        'Картинка',
        null=True,
        upload_to='media/',
        blank=True
    )
    employee = models.ManyToManyField(
        'Employee',
        through='DayOfWork',
        through_fields=('salons', 'employees')
    )

    def __str__(self):
        return f'{self.name} {self.address}'

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Feedback(models.Model):
    feedback_text = models.TextField(
        'Текст'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_reviews'
    )
    value = models.IntegerField(
        'Оценка',
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='Мастер',
        default=None
    )

    def __str__(self):
        return f' Оценка - {self.value}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class DayOfWork(models.Model):
    MONDAY = 'Mo'
    TUESDAY = 'Tu'
    WEDNESDAY = 'We'
    THURSDAY = 'Td'
    FRIDAY = 'Fr'
    SATURDAY = 'Sa'
    SUNDAY = 'Su'

    DAYS_OF_WEEK = [
        (MONDAY, 'Пн'),
        (TUESDAY, 'Вт'),
        (WEDNESDAY, 'Ср'),
        (THURSDAY, 'Чт'),
        (FRIDAY, 'Пт'),
        (SATURDAY, 'Сб'),
        (SUNDAY, 'Вс')
    ]

    day_of_week = models.CharField(
        max_length=20,
        verbose_name='Рабочие дни',
        choices=DAYS_OF_WEEK,
        blank=True
    )

    ready = models.BooleanField(
        default=False
    )

    employees = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='day_of_works',
        verbose_name='Мастер'
    )

    salons = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name='day_of_works'
    )


class Appointment(models.Model):

    MORNING_1 = '9:00'
    MORNING_2 = '10:00'
    MORNING_3 = '11:00'
    AFTERNOON_1 = '12:00'
    AFTERNOON_2 = '13:00'
    AFTERNOON_3 = '14:00'
    DAY_1 = '15:00'
    DAY_2 = '16:00'
    DAY_3 = '17:00'
    EVENING_1 = '18:00'
    EVENING_2 = '19:00'
    EVENING_3 = '20:00'
    day_times = {
        MORNING_1, MORNING_2, MORNING_2, MORNING_3, AFTERNOON_1, AFTERNOON_2,
        AFTERNOON_3, DAY_1, DAY_2, DAY_3, EVENING_1, EVENING_2, EVENING_3
    }
    WORK_HOURS = [
        (MORNING_1, MORNING_1),
        (MORNING_2, MORNING_2),
        (MORNING_3, MORNING_3),
        (AFTERNOON_1, AFTERNOON_1),
        (AFTERNOON_2, AFTERNOON_2),
        (AFTERNOON_3, AFTERNOON_3),
        (DAY_1, DAY_1),
        (DAY_2, DAY_2),
        (DAY_3, DAY_3),
        (EVENING_1, EVENING_1),
        (EVENING_2, EVENING_2),
        (EVENING_3, EVENING_3),
    ]
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='appointment',
        verbose_name='Процедура',
        default=None
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Мастер'
    )
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    appointment_hour = models.CharField(
        max_length=15,
        verbose_name='Время записи',
        choices=WORK_HOURS,
        blank=True
    )
    user = models.ForeignKey(
        User,
        related_name='appointments',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    question = models.TextField(
        'вопрос',
        null=True,
        blank=True
    )
    client_name = models.CharField('имя клиента', max_length=100, null=True, blank=True)
    date = models.DateField(
        'Дата',
        null=True
    )

    def __str__(self):
        return f'{self.employee}'

    class Meta:
        verbose_name = 'Приём'
        verbose_name_plural = 'Приёмы'
