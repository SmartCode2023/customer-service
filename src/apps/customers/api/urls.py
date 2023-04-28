from rest_framework.routers import DefaultRouter

from apps.customers.api.views.customer_view_set import CustomerViewSet, PhoneViewSet

router = DefaultRouter()

router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"phones",PhoneViewSet, basename="phones" )

urlpatterns = []

urlpatterns += router.urls
