from django.urls import path
from . import views


urlpatterns = [
    path('api/record/<int:record_id>', views.detail, name='detail'),
]
