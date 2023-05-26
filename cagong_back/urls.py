from django.contrib import admin
from django.urls import path, include
import user.views as user_views
import pushQue.views as pushQue_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', user_views.signup),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='api/token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/signin/', user_views.signin),
    path('api/getpush/', pushQue_views.get_push_notification),
    path('api/createpush/', pushQue_views.create_push_notification),
    path('api/record/', include('records.urls')),
]
