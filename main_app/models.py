from django.db import models

# Create your models here.

class Department(models.Model):
    departmentID = models.CharField(max_length=255, primary_key=True)
    departmentName = models.CharField(max_length=255)

    def __str__(self):
        return self.departmentName

class Employee(models.Model):
    employeeID = models.CharField(max_length=255, primary_key=True)
    departmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.email

class Customer(models.Model):
    customerID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    courseID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class EmployeeCourse(models.Model):
    employeeCourseID = models.CharField(max_length=255, primary_key=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class Schedule(models.Model):
    scheduleID = models.CharField(max_length=255, primary_key=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField()

class CustomerInteraction(models.Model):
    interactionID = models.CharField(max_length=255, primary_key=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.PositiveIntegerField()
    updatedTime = models.DateTimeField()

class Lead(models.Model):
    leadID = models.CharField(max_length=255, primary_key=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    productType = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    numberOfBedroom = models.CharField(max_length=50)
    surroundingAmenities = models.TextField()
    addition = models.TextField()

class ApartmentOwner(models.Model):
    apartmentOwnerID = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Apartment(models.Model):
    apartmentID = models.CharField(max_length=255, primary_key=True)
    apartmentOwnerID = models.ForeignKey(ApartmentOwner, on_delete=models.CASCADE)
    productName = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    numberOfBedroom = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.productName

class Recommendation(models.Model):
    recommendationID = models.CharField(max_length=255, primary_key=True)
    apartmentID = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confidence = models.DecimalField(max_digits=5, decimal_places=2)