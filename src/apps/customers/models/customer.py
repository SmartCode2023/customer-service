from django.db import models

from apps.shared.shared_models import SharedModelHistorical, Person

class Phone(SharedModelHistorical):
    # Tipos de telefono
    NACIONAL = 'NACIONAL'
    INTERNACIONAL = 'INTERNACIONAL'

    PHONE_TYPE_CHOICES = [
        (NACIONAL, 'Nacional'),
        (INTERNACIONAL, 'Internacional'),
    ]

    phoneType = models.CharField(
        "Tipo de telefono",
        max_length=20,
        blank=True,
        choices=PHONE_TYPE_CHOICES,
        default=NACIONAL,
    )

    phoneNumber = models.CharField(
        "Numero de telefono",
        max_length=20,
        blank=True,
        default='',
    )
    
    class Meta:
        verbose_name = "Telefono"
        verbose_name_plural = "Telefonos"
        
        
class Customer(SharedModelHistorical):

    # Tipos de cliente
    EMPRESA = 'EMPRESA'
    GOBIERNO = 'GOBIERNO'
    PARTICULAR = 'PARTICULAR'

    CUSTOMER_TYPE_CHOICES = [
        (EMPRESA, 'Empresa'),
        (GOBIERNO, 'Gobierno'),
        (PARTICULAR, 'Particular'),
    ]

    customerType = models.CharField(
        "Tipo de cliente",
        max_length=20,
        blank=True,
        choices=CUSTOMER_TYPE_CHOICES,
        default=EMPRESA,
    )
    
    phone_numbers = models.OneToManyField("Telefono",Phone, related_name="customer_phone_numbers", blank=True)

    #User ID from user Microservice
    user = models.JSONField(
        "User ID from user Microservice",
        blank=True,
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
