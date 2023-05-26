from django.urls import path
from . import views


urlpatterns = [
    path('api/record/<int:record_id>', views.detail, name='detail'),
    path('api/record_list/<str:user_id>', views.record_list, name='detail'),
]
