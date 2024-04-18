from namanga.apps.engine.models_container import (models, uuid)
from namanga.apps.engine.models import Manga


class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    number = models.IntegerField(null=False, blank=True)
    title = models.CharField(max_length=255, null=True, blank=False)
    views = models.IntegerField(default=0, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
