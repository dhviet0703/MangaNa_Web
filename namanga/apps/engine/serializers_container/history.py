from namanga.apps.engine.models_container.chapter import Chapter
from namanga.apps.engine.models_container.manga import Manga
from namanga.apps.engine.serializers_container import (
    History, serializers
)


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class CreateHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['content']

    def create(self, validated_data):
        current_user = self.context['request'].user
        mission = History.objects.create(user=current_user, **validated_data)
        return mission


class UpdateHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['content']

    def update(self, instance, validated_data):
        current_user = self.context['request'].user
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

