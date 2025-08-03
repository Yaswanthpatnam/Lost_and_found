from django.contrib import admin
from .models import  FoundItem


# Register your models here.


@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'contact_info', 'date_found')
    search_fields = ('title', 'description', 'location')    