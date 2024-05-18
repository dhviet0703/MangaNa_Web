from namanga.apps.engine.serializers_container import (
    Manga, serializers, AppStatus, cfg, Response, check_role_crud_manga, join
)


class MangaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'
