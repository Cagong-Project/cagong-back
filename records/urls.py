from django.urls import path
from . import views


urlpatterns = [
    path('detail/<int:record_id>', views.detail, name='detail'),
    path('record_list/<str:user_id>',
         views.record_list, name='record_list'),
]
