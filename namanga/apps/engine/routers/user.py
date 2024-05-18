from namanga.apps.engine.routers import *

from namanga.apps.engine.views import (UserDetailViewSet)

urlpatterns = [
    path('me/', UserDetailViewSet.as_view(), name='user-detail'),
]
