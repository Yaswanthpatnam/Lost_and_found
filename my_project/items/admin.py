from django.contrib import admin
from .models import LostItem, FoundItem


# Register your models here.

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'contact_info', 'date_lost')
    search_fields = ('title', 'description', 'location')
    
@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'contact_info', 'date_found')
    search_fields = ('title', 'description', 'location')    