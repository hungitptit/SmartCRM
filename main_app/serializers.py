from rest_framework import serializers
from .models import Customer, Employee
from django.contrib.auth.models import User, Group
import string
import random
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework.permissions import IsAuthenticated

def generate_random_id(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class CustomerSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Customer
        fields = ('customerID', 'name', 'email', 'phone', 'age', 'income', 'job')
        extra_kwargs = {
            'customerID': {'read_only': True}  # Make customerID read-only
        }
  
    def create(self, validated_data):
        validated_data['customerID'] = generate_random_id()
        return super().create(validated_data)
    
    def validate(self, data):
        # Custom validation logic
        if 'name' not in data:
            raise serializers.ValidationError("Name is required.")
        return data
    

class UserRegistrationSerializer(RegisterSerializer):
    departmentID = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=15)
    position = serializers.CharField(max_length=100)
    active = serializers.BooleanField(default=True)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'departmentID', 'address', 'phone', 'position', 'active']
    
    # override get_cleaned_data of RegisterSerializer
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'departmentID': self.validated_data.get('departmentID'),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age'),
            'address': self.validated_data.get('address', ''),
            'phone': self.validated_data.get('phone', ''),
            'position': self.validated_data.get('position', ''),
            'active': self.validated_data.get('active'),
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.age = self.cleaned_data.get('age')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.position = self.cleaned_data.get('position')
        user.active = self.cleaned_data.get('active')
        adapter.save_user(request, user, self)
        employee_data = {
            'departmentID': self.cleaned_data.get('departmentID'),
            'address': self.cleaned_data.get('address'),
            'phone': self.cleaned_data.get('phone'),
            'position':self.cleaned_data.get('position'),
            'active': self.cleaned_data.get('active'),
            'email': self.cleaned_data.get('email'),
            'employeeID': generate_random_id()
        }
        Employee.objects.create(user=user, **employee_data)
        group = Group.objects.filter(name='sale_agent')
        user.groups.add(group[0])
        user.save()
        return user


    # def create(self, validated_data):
    #     user_data = {
    #         'username': validated_data['username'],
    #         'password': validated_data['password'],
    #         'email': validated_data['email'],
    #     }
    #     employee_data = {
    #         'departmentID': validated_data['departmentID'],
    #         'address': validated_data['address'],
    #         'phone': validated_data['phone'],
    #         'position': validated_data['position'],
    #         'active': validated_data['active'],
    #         'email': validated_data['email'],
    #         'employeeID': generate_random_id()
    #     }
    #     user = User.objects.create_user(**user_data)
    #     Employee.objects.create(user=user, **employee_data)
    #     return user