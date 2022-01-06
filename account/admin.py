from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name',
                    'last_name', 'email', 'address']


admin.site.register(Session)
