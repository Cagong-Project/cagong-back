from django.urls import path
from .views import RecordDetailAPIView, RecordDoneAPIView, RecordListAPIView


urlpatterns = [
    path('detail/<int:record_id>', RecordDetailAPIView.as_view(), name='detail'),
    path('done', RecordDoneAPIView.as_view(), name='done'),
    path('record_list/<str:user_id>', RecordListAPIView.as_view(), name='record_list'),
]
