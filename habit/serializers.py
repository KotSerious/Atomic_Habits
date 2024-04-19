from rest_framework import serializers
from habit.models import Habit
from habit.validators import (TimeToCompleteValidator, AssociatedAndPrizeValidator,
                              AssociatedValidator, GoodHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Привычек
    """

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'good_habit', 'associated_habit',
                  'period', 'prize', 'time_to_complete', 'is_public',)
        validators = [
            TimeToCompleteValidator(time_to_complete='time_to_complete'),
            # AssociatedAndPrizeValidator(associated_habit='associated_habit', prize='prize'),
            # AssociatedValidator(associated_habit='associated_habit', good_habit='good_habit'),
            # GoodHabitValidator(good_habit='good_habit', associated_habit='associated_habit', prize='prize')
        ]

    def validate_related_habits(self, value):
        if value is not None and not value.is_pleasant:
            raise serializers.ValidationError("Related habit must have the pleasant attribute set to True.")
        return value

    def validate(self, data):
        if data['good_habit']:
            if 'prize' in data:
                raise serializers.ValidationError("Pleasant habit cannot have a reward.")
            if 'associated_habit' in data:
                raise serializers.ValidationError("Pleasant habit cannot have related habits.")
        return data


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'good_habit', 'associated_habit',
                  'period', 'prize', 'time_to_complete', 'is_public',)
        read_only_fields = ('id', 'user', 'place', 'time', 'action', 'good_habit', 'associated_habit',
                  'period', 'prize', 'time_to_complete', 'is_public',)


