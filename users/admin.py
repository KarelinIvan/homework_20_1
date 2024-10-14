from django.contrib import admin

from users.models import User

# Список пользователей в админке
admin.site.register(User)
