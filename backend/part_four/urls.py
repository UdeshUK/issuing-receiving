from rest_framework import routers
from part_four.views import IssuedToCCOViewSet, BallotBoxesIssuedToCCOViewSet

router = routers.DefaultRouter()
router.register(r'election/(?P<election>.*)/issued-to-cco', IssuedToCCOViewSet)
router.register(r'election/(?P<election>.*)/issued-ballot-boxes-to-cco', BallotBoxesIssuedToCCOViewSet)

urlpatterns = router.urls
