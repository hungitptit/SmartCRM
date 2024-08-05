from rest_framework import serializers
from .models import Customer
import string
import random

def generate_random_id(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'age', 'income', 'job')
  
    def create(self, validated_data):
        validated_data['customerID'] = generate_random_id()
        return super().create(validated_data)
    
    def validate(self, data):
        # Custom validation logic
        if 'name' not in data:
            raise serializers.ValidationError("Name is required.")
        return data