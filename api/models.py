from django.contrib.auth import get_user_model 
from django.db import models


User = get_user_model() 


class News(models.Model): 
   
    pub_date = models.DateTimeField(
        verbose_name='дата новости', auto_now_add=True) 
    headline = models.CharField(verbose_name='заголовок новости', max_length=50) 
    text = models.TextField(verbose_name='текст новости') 
    
    def __str__(self): 
        return self.headline
    
    class Meta: 
        verbose_name_plural = 'Новости'
