from rest_framework import serializers
from dogs.models import Dog

class DogsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    time_updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data): # создание новой строки в бд | Метод POST
        return Dog.objects.create(**validated_data) # результат в атрибут data
    
    def update(self, instance, validated_data): # Метод PUT
        # объект модели и валидированные данные в качестве параметров
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_updated = validated_data.get("time_updated", instance.time_updated)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save() # сохраняем изменения в бд
        return instance
    
