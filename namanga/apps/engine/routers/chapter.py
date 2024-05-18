from rest_framework import routers
from namanga.apps.engine.routers import *
from namanga.apps.engine.views import (CreateChapterViewSet)


urlpatterns = [
    path("post/", CreateChapterViewSet.as_view(), name="create-chapter"),
    # path("delete/", DeleteMangaViewSet.as_view(), name="delete-manga"),
]
