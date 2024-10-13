from django.forms import model_to_dict
from dogs.models import Dog
from dogs.serializers import DogsSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class DogAPIList(generics.ListCreateAPIView): # реализует get и post запросы 
    queryset = Dog.objects.all() # в данном примере все объекты модели будут возвращены клиенту
    # queryset - список записей возвращаемых клиенту (serializer возвращает конкретные поля записей)
    # запрос в бд для получение записей на основае queryset, передача их сериализатору 
    serializer_class = DogsSerializer


class DogAPIUpdate(generics.UpdateAPIView):
    queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
    serializer_class = DogsSerializer
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    

class DogAPIDetailView(generics.RetrieveUpdateDestroyAPIView): 
    # для одной конкретной записи CRUD операции
    queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
    serializer_class = DogsSerializer






# class DogAPIView(APIView):
#     def get_object(
#         self, pk
#     ):  # пользовательская функция для проверки пользовательского pk
#         # (уникального id объекта модели Dog)
#         try:
#             return Dog.objects.get(pk=pk)
#         except Dog.DoesNotExist:
#             return Response({"error": "Current method not allowed"})

#     def get(self, request):
#         dogs = Dog.objects.all()
#         return Response({"posts": DogsSerializer(dogs, many=True).data})

#     def post(self, request):
#         # POST запрос с данными от клиента (JSON преобразуется в словарь request.data) в HTTP запросе
#         serializer = DogsSerializer(
#             data=request.data
#         )  
#         # передача десериализованных данных в виде Python словаря (request.data) в сериализатор
#         serializer.is_valid( # валидация данных (на основе полей)
#             raise_exception=True
#         )  # сохраняет результат в validated_data
#         serializer.save()  # вызов метода create, результат в атрибуте data
#         # каждая функция должна выполнять только одну область действий

#         return Response({"posts": serializer.data})

#     def put(self, request, pk=None):  # из query-параметра
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         instance = self.get_object(pk=pk)

#         serializer = DogsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(
#             raise_exception=True
#         )  # валидированные данные в validated_data
#         serializer.save()  # вызовет метод update из-за instance
#         return Response({"post": serializer.data})

#     def delete(self, request, pk=None):
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         instance = self.get_object(pk=pk, method="DELETE")
#         instance.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
