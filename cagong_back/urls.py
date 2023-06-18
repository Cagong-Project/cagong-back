from django.contrib import admin
from django.urls import path, include, re_path
import user.views as user_views
import cafe.views as cafe_views
import pushQue.views as pushQue_views
import orders.views as order_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', user_views.signup),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='api/token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('api/signin/', user_views.signin),
    path('api/charge_point/', user_views.charge_point, name='charge_point'),
    path('api/cafe/', cafe_views.cafelist, name='cafe'),
    path('api/cafe/detail/<int:cafe_id>/',
         cafe_views.detail, name='detail'),
    path('api/getpush/', pushQue_views.get_push_notification),
    path('api/createpush/', pushQue_views.create_push_notification),
    path('api/record/', include('records.urls')),
    path('api/charge_point/', user_views.charge_point),
    re_path(r'^webpush/', include('webpush.urls')),
    path('api/order/', order_views.order, name='order'),
    path('api/get_user/', user_views.get_userDB, name='get_userDB'),
]
