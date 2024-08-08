from django.shortcuts import render
from .models import Customer, Employee
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, UserRegistrationSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

# CRUD Customer
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get_queryset(self):
            # Extract token from the Authorization header
            auth_header = self.request.headers.get('Authorization', '')
            token_key = auth_header.replace('Token ', '')
            if not token_key:
                raise AuthenticationFailed('Token is missing')

            try:
                token = Token.objects.get(key=token_key)
                user = token.user
                employee = Employee.objects.get(user=user)
            except Token.DoesNotExist:
                raise AuthenticationFailed('Invalid token')
            except Employee.DoesNotExist:
                return Customer.objects.none()
            print(employee)
            return Customer.objects.filter(createdBy=employee)
    
class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Registration
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)