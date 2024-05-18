from namanga.apps.engine.models_container import (models, uuid, RoleMangaEnum)
from namanga.apps.engine.models import User, Manga


class UserManga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    is_favorite = models.BooleanField(default=False)
    is_like = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    role = models.CharField(max_length=30, null=True, blank=False, choices=RoleMangaEnum.choices(),
                            default=RoleMangaEnum.USER)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
