from rest_framework.routers import DefaultRouter
from .views import PartsViewSet

router = DefaultRouter()
router.register('parts', PartsViewSet, basename='parts')

urlpatterns = router.urls