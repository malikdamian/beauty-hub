from rest_framework import routers

from service import views

router = routers.SimpleRouter()
router.register(r"service", views.ServiceViewSet, basename="service")

urlpatterns = router.urls
