from rest_framework import viewsets
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from .models import Message, ImageUpload, VideoUpload, AudioUpload
from .serializers import (
    MessageSerializer,
    ImageUploadSerializer,
    VideoUploadSerializer,
    AudioUploadSerializer
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Message.objects.all().order_by('-created_at')
        user = self.request.query_params.get('user')

        if user:
            return queryset.filter(Q(is_public=True) | Q(recipient=user))

        return queryset.filter(is_public=True)


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ImageUpload.objects.all().order_by('-created_at')
        user = self.request.query_params.get('user')

        if user:
            return queryset.filter(Q(is_public=True) | Q(recipient=user))

        return queryset.filter(is_public=True)


class VideoUploadViewSet(viewsets.ModelViewSet):
    queryset = VideoUpload.objects.all()
    serializer_class = VideoUploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = VideoUpload.objects.all().order_by('-created_at')
        user = self.request.query_params.get('user')

        if user:
            return queryset.filter(Q(is_public=True) | Q(recipient=user))

        return queryset.filter(is_public=True)


class AudioUploadViewSet(viewsets.ModelViewSet):
    queryset = AudioUpload.objects.all()
    serializer_class = AudioUploadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = AudioUpload.objects.all().order_by('-created_at')
        user = self.request.query_params.get('user')

        if user:
            return queryset.filter(Q(is_public=True) | Q(recipient=user))

        return queryset.filter(is_public=True)