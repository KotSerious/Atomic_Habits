from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда для создания супер пользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Enter your email address: '),
            first_name=input('First Name: '),
            last_name=input('Last Name: '),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        password = input('Password: ')

        user.set_password(password)
        user.save()
