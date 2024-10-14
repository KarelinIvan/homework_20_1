from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='ivan.karelin.1993@mail.ru',
            first_name='Admin',
            last_name='Skypro',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('Mt076954')
        user.save()
