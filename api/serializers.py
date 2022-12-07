from rest_framework import serializers
from base.models import Event, Registrant

class EventSerializer(serializers.ModelSerializer):
    """EventSerializer is a class for serializing event data."""
    class Meta:
        """Meta configures EventSerializer model and fields"""
        model = Event
        fields = '__all__'

class RegistrantSerializer(serializers.ModelSerializer):
    """
    RegistrantSerializer is a class for serializing registrant data.
    """
    event = EventSerializer(many=False)
    class Meta:
        """Meta configures RegistrantSerializer model and fields"""
        model = Registrant
        fields = '__all__'
