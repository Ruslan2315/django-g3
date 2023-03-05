from rest_framework import serializers
from films.models import Film


class FilmsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(min_length=5, max_length=50, allow_null=False)
    description = serializers.CharField(allow_null=False, allow_blank=False)
    duration = serializers.IntegerField(min_value=0, allow_null=False)

    def create(self, validated_data):
        film = Film(**validated_data)
        film.save()
        return film

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
