from django.contrib import admin
from django.urls import path, include, re_path
import user.views as user_views
from cafe.views import CafeListAPIView, CafeDetailAPIView
import pushQue.views as pushQue_views
import orders.views as order_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', user_views.SignupAPIView.as_view()),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='api/token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('api/signin/', user_views.SigninAPIView.as_view()),
    path('api/charge_point/', user_views.ChargePointAPIView.as_view(), name='charge_point'),
    path('api/cafe/', CafeListAPIView.as_view(), name='cafe'),
    path('api/cafe/detail/<int:cafe_id>/',
         CafeDetailAPIView.as_view(), name='detail'),
    path('api/getpush/<str:user_id>', pushQue_views.get_pushNotificationAPIView.as_view()),
    path('api/createpush/', pushQue_views.create_pushNotificationAPIView.as_view()),
    path('api/record/', include('records.urls')),
    re_path(r'^webpush/', include('webpush.urls')),
    path('api/order/', order_views.OrderAPIView.as_view(), name='order'),
    path('api/get_user/', user_views.GetUserDBAPIView.as_view(), name='get_userDB'),
]
