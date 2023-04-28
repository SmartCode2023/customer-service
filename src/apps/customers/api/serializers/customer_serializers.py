from rest_framework import serializers

from apps.customers.models.customer import Customer, Phone


class PhoneSerializer(serializers.ModelSerializer):
    """
    Phone serializer for viewing.
    """
    class Meta:
        model = Phone
        fields = [
            "id",
            "phoneType",
            "phoneNumber"
        ]


class CustomerViewSerializer(serializers.ModelSerializer):
    """
    Customer serializer for viewing.
    """
    phone_numbers = PhoneSerializer(many=True, read_only=True)

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
            "phone_numbers",
            "user"
        ]
