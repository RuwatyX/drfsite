from dogs.models import Category, Dog
from dogs.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from dogs.serializers import DogsSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser







class DogAPIList(generics.ListCreateAPIView): # реализует get и post запросы 
    queryset = Dog.objects.all() # в данном примере все объекты модели будут возвращены клиенту
    # queryset - список записей возвращаемых клиенту (serializer возвращает конкретные поля записей)
    # запрос в бд для получение записей на основае queryset, передача их сериализатору 
    serializer_class = DogsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) # Only GET request


class DogAPIUpdate(generics.UpdateAPIView):
    queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
    serializer_class = DogsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    
class DogAPIDestroy(generics.DestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogsSerializer
    permission_classes = (IsAdminOrReadOnly, )