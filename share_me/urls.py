from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MessageViewSet,
    ImageUploadViewSet,
    VideoUploadViewSet,
    AudioUploadViewSet
)

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'images', ImageUploadViewSet)   # 👈 ADD THIS
router.register(r'videos', VideoUploadViewSet)   # 👈 ADD THIS
router.register(r'audio', AudioUploadViewSet)    # 👈 ADD THIS

urlpatterns = [
    path('', include(router.urls)),
]