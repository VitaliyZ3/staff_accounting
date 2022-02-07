from tabnanny import verbose
from phonenumber_field.modelfields import PhoneNumberField 
from django.db import models

# Create your models here.

class Employer(models.Model):
    name = models.CharField(max_length=120, verbose_name='Iмя')
    patronymic = models.CharField(max_length=120, verbose_name='По-батьковi')
    surname = models.CharField(max_length=120,verbose_name='Прiзвище')
    post = models.ForeignKey('Post', verbose_name='Посада', on_delete=models.DO_NOTHING)
    insurance = models.ForeignKey('Insurance', verbose_name='Страховка', on_delete=models.DO_NOTHING)
    status = models.ForeignKey('Status', verbose_name='Статус', on_delete=models.DO_NOTHING)
    phone_number = PhoneNumberField(verbose_name = 'Номер телефону')
    email = models.CharField(max_length=120, verbose_name='Електронна скринька')
    description = models.TextField(verbose_name='Опис')
    
    class Meta():
        verbose_name = 'Працiвник'
        verbose_name_plural = 'Працiвники'

    def __str__(self) -> str:
        return self.surname


class Post(models.Model):
    name = models.CharField(max_length=120, verbose_name='Посада')
    calary = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Зарплата')
    description = models.TextField(verbose_name='опис')

    class Meta():
        verbose_name = 'Посада'
        verbose_name_plural = 'Посади'

    def __str__(self) -> str:
        return self.name

class Insurance(models.Model):
    name = models.CharField(max_length=120, verbose_name='Страховка')
    description = models.TextField(verbose_name='опис')

    class Meta():
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'

    def __str__(self) -> str:
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=120, verbose_name='Статус')
    description = models.TextField(verbose_name='опис')

    class Meta():
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'

    def __str__(self) -> str:
        return self.name