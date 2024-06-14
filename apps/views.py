from rest_framework import generics
from .models import Image, Annotation
from .serializers import ImageSerializer, AnnotationSerializer
from rest_framework.exceptions import NotFound


class ImageView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AnnotationView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    serializer_class = AnnotationSerializer
    
    def get_queryset(self):
        uuid = self.kwargs["uuid"]
        return Annotation.objects.filter(uid=uuid)
    
    def get_object(self):
        qs = self.get_queryset()
        if qs.exists():
            return qs.first()
        raise NotFound('Not found annotation')
    