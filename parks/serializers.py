from rest_framework import serializers
from .models import Park

class ParkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Park
        fields = ['id', 'name', 'longitude', 'latitude', 'dogfriendly', 'details']

    def create(self, validated_data):
        return Park.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)       
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.dogfriendly = validated_data.get('dogfriendly', instance.dogfriendly)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        return instance
        