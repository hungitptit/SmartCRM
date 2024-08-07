from django.contrib import admin
from .models import Department, Employee, Customer, Course, EmployeeCourse, Schedule, CustomerInteraction, Lead, ApartmentOwner, Apartment, Recommendation, District, EmployeeDistrict

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('departmentID', 'departmentName')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeID', 'departmentID', 'email', 'position', 'active')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customerID', 'name', 'email', 'phone', 'age', 'income', 'job')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'name', 'description', 'instructor', 'duration')

@admin.register(EmployeeCourse)
class EmployeeCourseAdmin(admin.ModelAdmin):
    list_display = ('employeeCourseID', 'employeeID', 'courseID', 'status')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('scheduleID', 'customerID', 'employeeID', 'description', 'time')

@admin.register(CustomerInteraction)
class CustomerInteractionAdmin(admin.ModelAdmin):
    list_display = ('interactionID', 'employeeID', 'customerID', 'description', 'status', 'updatedTime')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('leadID', 'customerID', 'budget', 'location', 'productType', 'purpose', 'area', 'numberOfBedroom', 'surroundingAmenities', 'addition')

@admin.register(ApartmentOwner)
class ApartmentOwnerAdmin(admin.ModelAdmin):
    list_display = ('apartmentOwnerID', 'name', 'email', 'phone')

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('apartmentID', 'apartmentOwnerID', 'productName', 'description', 'price', 'numberOfBedroom', 'address')

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('recommendationID', 'apartmentID', 'customerID', 'confidence')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('districtID', 'name')

@admin.register(EmployeeDistrict)
class EmployeeDistrictAdmin(admin.ModelAdmin):
    list_display = ('employeeDistrictID', 'employeeID', 'districtID')