from .serializers import PropertySerializer
from Property.models import Property

from rest_framework import generics


class PropertyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
