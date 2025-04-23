from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet  # we’ll build this next

router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
