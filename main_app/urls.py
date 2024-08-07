from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy, UserRegistrationView

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]