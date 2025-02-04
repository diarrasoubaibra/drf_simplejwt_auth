from django.contrib import admin
from jwtapp.models import Role, UserRole

# Register your models here.
admin.site.register(Role)
admin.site.register(UserRole)
