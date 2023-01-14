from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'created_time']
    fields = ['name', 'email', 'topic', 'text']


admin.site.register(Contact, ContactAdmin)