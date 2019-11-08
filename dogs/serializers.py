from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'gender', 'color', 'weight', 'longitude', 'latitude', 'lastupdated']

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.lastupdated = validated_data.get('lastupdated', instance.lastupdated)
        instance.save()
        return instance
