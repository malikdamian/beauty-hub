from rest_framework import routers

from employee import views

router = routers.SimpleRouter()
router.register(r"employee", views.EmployeeViewSet, basename="employee")

urlpatterns = router.urls
