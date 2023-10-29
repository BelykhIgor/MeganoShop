from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(1, 5):
            random_name = fake.first_name()
            User.objects.create_user(username=random_name, password='123456')
