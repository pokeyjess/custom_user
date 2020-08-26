from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user.models import MyUser

admin.site.register(MyUser, UserAdmin)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('display_name', 'age', 'homepage')}),

# https://stackoverflow.com/questions/50396023/django-custom-user-model-fields-not-appearing-in-django-admin/50396172

