from django.db import models


class File(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


# Create your models here.
class Service(models.Model):

    title = models.TextField(verbose_name="Название услуги", default='')
    decs = models.TextField(verbose_name="Описание услуги",default='')
    price = models.TextField(verbose_name="Цена услуги",default='')
    img = models.FileField(verbose_name="Картинка",upload_to='db.File/bytes/filename/mimetype', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Список услуг'


class History(models.Model):
    
    title = models.TextField(verbose_name="Название проекта",default='')
    decs = models.TextField(verbose_name="Описание проекта",default='')
    img = models.FileField(verbose_name="Фото проекта",upload_to='db.File/bytes/filename/mimetype', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты (портфолио)'