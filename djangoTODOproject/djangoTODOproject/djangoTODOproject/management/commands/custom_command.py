# from django.contrib import admin
# from django.core.management.base import BaseCommand
# from users.models import User
#
# class ManagmentCommand(BaseCommand):
#     help = u'This command creates new superuser and 2 test users.'
#
#     def create_sup_user(self):
#         self.username = 'Admin123'
#         self.email = 'Admin123@mail.com'
#         admin.site.register(self)
#         print(u'Superuser registered succesfully!')
#     def create_users(self):
#         i = 0
#         while i < 1:
#             User.username = 'Test' + str(i)
#             User.firstname = 'Test' + str(i)
#             User.lastname = 'TestSecondName' + str(i)
#             User.email = 'Test' + str(i) + 'mail.com'
#             User.save()
#             i+=1
#         print(u'Users registered succesfully!')