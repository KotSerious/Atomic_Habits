from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка для пользователей
    """
    list_display = ('email', 'first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
