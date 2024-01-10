from rest_framework import viewsets
from rest_framework.response import Response

from producer import CustomProducer
from .models import Enseignant
from .serializers import EnseignantSerializer
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    ListModelMixin

)

from rest_framework.viewsets import GenericViewSet

class EnseignantViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,

):

    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

    customProducer = CustomProducer('localhost:9092') 
    customProducer.send('profnotif', 'vous avez un nouveau support')

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=201, headers=headers)
    

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)