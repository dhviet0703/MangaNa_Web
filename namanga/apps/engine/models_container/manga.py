from namanga.apps.engine.models_container import (models, uuid)
from namanga.apps.engine.models import User


class Manga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    total_chapter = models.IntegerField(null=True, blank=True)
    manga_stats = models.JSONField(default=dict(likes=0, ratting=0, follower=0, views=0), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
