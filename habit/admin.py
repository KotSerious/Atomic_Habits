from django.contrib import admin
from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """
    Админка для привычек
    """
    list_display = ('user', 'action', 'date_of_creation', 'id', 'good_habit', 'is_public')
    list_filter = ('user', 'date_of_creation',)
