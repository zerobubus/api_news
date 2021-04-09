from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):  
    list_display = ('id', 'pub_date', 'headline', 'text')  
    search_fields = ('text',)  
    list_filter = ('pub_date',)  
    empty_value_display = '-пусто-'  


admin.site.register(News, NewsAdmin)
 