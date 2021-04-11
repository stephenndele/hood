from rest_framework import serializers
from .models import Hood, Profile

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = ('name')