from rest_framework import serializers
from base.models import Event, Registrant

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RegistrantSerializer(serializers.ModelSerializer):
    event = EventSerializer(many=False)
    class Meta:
        model = Registrant
        fields = '__all__'