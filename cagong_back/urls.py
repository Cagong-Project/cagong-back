from django.contrib import admin
from django.urls import include, path
import user.views as user_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import send_push

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', user_views.signup),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='api/token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/signin/', user_views.signin),
]
