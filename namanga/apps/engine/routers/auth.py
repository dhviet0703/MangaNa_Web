from namanga.apps.engine.routers import *

from namanga.apps.engine.views import (RegisterViewSet, ResendVerificationViewSet, VerifyCodeViewSet)

urlpatterns = [
    path('auth/register/', RegisterViewSet.as_view(), name='register'),
    path('auth/resend-email/', ResendVerificationViewSet.as_view(), name='resend'),
    path('auth/verify-code/', VerifyCodeViewSet.as_view(), name='verify'),
]
