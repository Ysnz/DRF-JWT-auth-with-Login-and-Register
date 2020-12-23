from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', include('users.urls')),
]