from django.urls import path
from . import views


urlpatterns = [
    path('detail/<int:record_id>', views.detail, name='detail'),
    path('detail2/<int:record_id>', views.detail2, name='detail2'),
    path('record_list/<str:user_id>',
         views.record_list, name='record_list'),
]
