from rest_framework_mongoengine.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls