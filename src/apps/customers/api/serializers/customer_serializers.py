from rest_framework import serializers

from apps.customers.models.customer import Customer, Phone
from apps.shared.shared_api.shared_serializers.ShortSerializers import CustomerSerializerShort, PhoneSerializerShort

class PhoneViewSerializer(serializers.ModelSerializer):
    """
    Phone serializer for viewing.
    """
    customer = CustomerSerializerShort(read_only=True)
    class Meta:
        model = Phone
        fields = [
            "id",
            "phoneType",
            "phoneNumber",
            "customer"
        ]
        
class PhoneCreateSerializers(serializers.ModelSerializer):
    '''
    Phone serializer for creation.
    '''
    class Meta:
        model = Phone
        fields = [
            "id",
            "phoneType",
            "phoneNumber",
            "customer"
        ]


class CustomerViewSerializer(serializers.ModelSerializer):
    """
    Customer serializer for viewing.
    """
    phone_numbers = PhoneSerializerShort(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "customerType",
            "phone_numbers",
            "user"
        ]


class CustomerCreateSerializers(serializers.ModelSerializer):
    '''
    Customer serializer for creation.
    '''
    class Meta:
        model = Customer
        fields = [
            "id",
            "customerType",
            "user",
            "phone_numbers"
        ]
