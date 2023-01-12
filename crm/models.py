from django.db import models


# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=50, verbose_name='Имя')
    order_surname = models.CharField(max_length=50, verbose_name='Фамилия')
    order_international = models.CharField(max_length=50, verbose_name='Гражданство')
    order_phone = models.CharField(max_length=50, verbose_name='Телефон')
    order_mail = models.CharField(max_length=50, verbose_name='Мэйл')
    order_country = models.CharField(max_length=50, verbose_name='Страна куда хочет')
    order_CV = models.CharField(max_length=50, verbose_name='Его CV')
    order_vakansia = models.CharField(max_length=50, verbose_name='На какую вакансию')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
