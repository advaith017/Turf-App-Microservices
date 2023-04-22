from rest_framework import serializers
from .models import Turfs
class TurfSerializer (serializers.ModelSerializer):
    class Meta:
        model = Turfs
        fields = '__all__'
        