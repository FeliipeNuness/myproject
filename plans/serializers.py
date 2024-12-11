from rest_framework import serializers
from .models import Signature, Plan

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ['id', 'user', 'plan', 'start_date', 'end_date', 'status']
        
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'price', 'periodicity']