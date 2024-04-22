from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.permissions import IsAuthor
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from habit.serializers import HabitSerializer, PublicHabitSerializer
from habit.paginators import HabitPagination


class HabitCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущностей модели Привычки
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class HabitListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех сущностей модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class GetPublicHabit(generics.ListAPIView):
    """
    Контроллер для просмотра списка всех публичных привычек
    """
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = PublicHabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]


class HabitRetriveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsAuthor]


class HabitDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
