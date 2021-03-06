from part_three.views import ReceivedFromSPOViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'election/(?P<election>.*)/received-from-spo', ReceivedFromSPOViewSet)

urlpatterns=router.urls