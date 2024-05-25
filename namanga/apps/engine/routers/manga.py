from rest_framework import routers
from namanga.apps.engine.routers import *
from namanga.apps.engine.views import (MangaViewSet, CreateMangaViewSet, UpdateMangaViewSet, DeleteMangaViewSet)

router = routers.DefaultRouter(trailing_slash=False)
router.register('', MangaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("post/", CreateMangaViewSet.as_view(), name="create-manga"),
    path("put/", UpdateMangaViewSet.as_view(), name="create-manga"),
    path("delete/", DeleteMangaViewSet.as_view(), name="delete-manga"),
]
