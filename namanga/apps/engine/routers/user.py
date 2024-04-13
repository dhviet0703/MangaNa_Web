from namanga.apps.engine.routers import *

from namanga.apps.engine.views import (UserDetailView)

urlpatterns = [
    path('user/me/', UserDetailView.as_view(), name='user-detail'),
]
