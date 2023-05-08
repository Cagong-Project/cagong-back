from django.contrib import admin
from django.urls import path, re_path
import user.views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', user_views.signup),
]
