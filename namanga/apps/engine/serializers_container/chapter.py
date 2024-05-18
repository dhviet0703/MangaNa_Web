from namanga.apps.engine.serializers_container import (
    Chapter, serializers
)


class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
