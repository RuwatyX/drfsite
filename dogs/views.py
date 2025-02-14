from dogs.models import Category, Dog
from dogs.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from dogs.serializers import DogsSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from dogs.paginations import DogsApiListPagination



class DogAPIList(generics.ListCreateAPIView): # реализует get и post запросы 
    queryset = Dog.objects.all() # в данном примере все объекты модели будут возвращены клиенту
    # queryset - список записей возвращаемых клиенту (serializer возвращает конкретные поля записей)
    # запрос в бд для получение записей на основе queryset, передача их сериализатору 
    serializer_class = DogsSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, ) # Only GET request
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )
    pagination_class = DogsApiListPagination


class DogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
    serializer_class = DogsSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAuthenticated, )
    
class DogAPIDestroy(generics.DestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogsSerializer
    permission_classes = (IsAdminOrReadOnly, )