import uuid

from django.db import models


class Image(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to="images/")


class Annotation(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    