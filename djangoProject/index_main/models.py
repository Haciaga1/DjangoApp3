from django.db import models

# Create your models here.
class Articles(models.Model):
 title=models.CharField('Başlıq',max_length=50)
 anons = models.CharField('Xülasə', max_length=255)
 full_text=models.TextField('Mətn')
 date=models.DateField('Nəşr tarixi')
 TYPE_CHOICES = (
  (0, u'Adi məsəslə'),
  (1, u'Təcili məsəslə'),
  (2, u'Çox vacib'),
  (3, u'Başqa'),
 )
 type = models.PositiveIntegerField(choices=TYPE_CHOICES, verbose_name='İşin vacibliyi', default=0)
