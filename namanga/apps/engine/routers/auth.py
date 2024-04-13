from namanga.apps.engine.routers import *

from namanga.apps.engine.views import (RegisterViewSet, ResendVerificationViewSet, VerifyCodeViewSet)

urlpatterns = [
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('resend-email/', ResendVerificationViewSet.as_view(), name='resend'),
    path('verify-code/', VerifyCodeViewSet.as_view(), name='verify'),
]
