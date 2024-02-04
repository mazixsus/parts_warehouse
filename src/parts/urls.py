from rest_framework.routers import DefaultRouter
from .views import StartUpsModels

router = DefaultRouter()
router.register('startups', StartUpsModels, basename='startups')

urlpatterns = router.urls