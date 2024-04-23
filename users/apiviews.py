from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности моедли Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        self.object = serializer.save()
        self.object.set_password(password)
        self.object.save()


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотора конкретной сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        password = serializer.validated_data.get('password')
        if password:
            password = serializer.validated_data.pop('password')
            self.object = serializer.save()
            self.object.set_password(password)
            self.object.save()
        self.object = serializer.save()
        self.object.save()


class UserDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
