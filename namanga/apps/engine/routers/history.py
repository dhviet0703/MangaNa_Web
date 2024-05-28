from rest_framework import routers
from namanga.apps.engine.routers import *
from namanga.apps.engine.views import (HistoryViewSet, HistoryDeleteViewSet)

router = routers.DefaultRouter(trailing_slash=False)
router.register('', HistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('<uuid:pk>/delete/', HistoryDeleteViewSet.as_view(), name='mission-delete'),
]