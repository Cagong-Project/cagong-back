from django.contrib import admin
from .models import *
from rest_framework_simplejwt.models import TokenUser

admin.site.register(User)
admin.site.register(CustomerUser)
admin.site.register(OwnerUser)
# admin.site.register(TokenUser)
