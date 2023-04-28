from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet

from apps.customers.api.serializers.customer_serializers import PhoneSerializer, CustomerViewSerializer, CustomerCreateSerializers 

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

import os
from dotenv import load_dotenv


class PhoneViewSet(GenericModelViewSet):
    serializer_class = PhoneSerializer
    
class CustomerViewSet(GenericModelViewSet):
    serializer_class = CustomerViewSerializer
    serializer_create_class = CustomerCreateSerializers
    serializer_update_class = CustomerCreateSerializers
   