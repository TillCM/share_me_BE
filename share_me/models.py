from django.db import models

class Message(models.Model):
    text = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)

    is_public = models.BooleanField(default=True)
    is_research = models.BooleanField(default=False)
    allow_external_sharing = models.BooleanField(default=False)
    recipient = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id}"


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')

    is_public = models.BooleanField(default=True)
    is_research = models.BooleanField(default=False)
    allow_external_sharing = models.BooleanField(default=False)
    recipient = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Image {self.id}"

class VideoUpload(models.Model):
    video = models.FileField(upload_to='videos/')

    is_public = models.BooleanField(default=True)
    is_research = models.BooleanField(default=False)
    allow_external_sharing = models.BooleanField(default=False)
    recipient = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id}"

class AudioUpload(models.Model):
    audio = models.FileField(upload_to='audio/')

    is_public = models.BooleanField(default=True)
    is_research = models.BooleanField(default=False)
    allow_external_sharing = models.BooleanField(default=False)
    recipient = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio {self.id}"

