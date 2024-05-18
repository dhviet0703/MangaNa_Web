from namanga.apps.engine.models_container import (models, uuid)
from namanga.apps.engine.models_container.chapter import Chapter


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    src = models.CharField(max_length=255, null=True, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
