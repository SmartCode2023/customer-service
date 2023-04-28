from django.db import models

from apps.shared.shared_models import SharedModelHistorical

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

    #Tipo de cliente
    customerType = models.CharField(
        "Tipo de cliente",
        max_length=20,
        blank=True,
        choices=CUSTOMER_TYPE_CHOICES,
        default=EMPRESA,
    )

    #User from user Microservice
    user = models.JSONField(
        "User ID from user Microservice",
        blank=True,
    )
    
    def __str__(self) -> str:
        return str(self.id) + " "+ self.customerType

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

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
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='phone_numbers', null=True)
    
    def __str__(self) -> str:
        return self.phoneNumber
    
    class Meta:
        verbose_name = "Telefono"
        verbose_name_plural = "Telefonos"
        