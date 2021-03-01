from django.contrib import admin
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = u'This command creates new superuser and 2 test users.'

    def handle(self, *args, **options):
        User.objects.create_superuser(email='Admi12345@mail.com',
                                      username='Admi12345', password='qwerty12345')
        User.objects.create_user(username='Robert1122',
                                 email='robpat12@rembler.com')
        User.objects.create_user(username='MaryJ5678',
                                 email='MaryJ5678@gmail.com')

