from rest_framework_mongoengine.routers import DefaultRouter
from .views import PartsViewSet

router = DefaultRouter()
router.register('parts', PartsViewSet, basename='parts')

urlpatterns = router.urls