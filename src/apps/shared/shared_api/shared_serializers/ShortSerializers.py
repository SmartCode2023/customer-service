# File which contains the SHORT serializers for each model
from rest_framework import serializers

# Customer and Phone Short serializers
from apps.customers.models.customer import Phone, Customer
# --------------------------------------------SHORT SERIALIZERS--------------------------------------------

class PhoneSerializerShort(serializers.ModelSerializer):
    '''
    Phone Serializer Short
    - phoneType: Nacional/Internacional
    - phoneNumber
    '''
    
    class Meta:
        model = Phone
        fields = ("phoneType", "phoneNumber")
        
class CustomerSerializerShort(serializers.ModelSerializer):
    '''
    Customer Serializer Short
    
    '''
    class Meta:
        model = Customer
        fields = ("customerType", "user")