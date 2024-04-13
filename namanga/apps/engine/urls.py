from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from namanga.apps import *
# from velociti.apps.engine.routers import user, system_information

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='login_api'),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('auth/', include('namanga.apps.engine.routers.auth')),
    path('', include('namanga.apps.engine.routers.user')),

]
