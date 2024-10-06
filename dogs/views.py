from django.forms import model_to_dict
from rest_framework import generics
from dogs.models import Dog
from dogs.serializers import DogsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DogsApiView(APIView):
    def get(self, request):
        dogs = Dog.objects.all()
        return Response({"posts": DogsSerializer(dogs, many=True).data})
        # преобразование Queryset в словарь на основе атрибутов DogsSerializer -> JSONRenderer

# # Во главе иерархии класов API находится APIView (родительский класс)
# class DogsApiView(APIView):
#     def get(self, request): # GET запрос
#         dogs = Dog.objects.all().values() 
#         # получаем не объекты модели, а значения внутри этих объектов
#         return Response({"title": dogs}) # преобразование атрибутов в JSON.
    

    def post(self, request): 
        # POST запрос с данными от клиента (JSON преобразуется в словарь request.data) в HTTP запросе
        serializer = DogsSerializer(data=request.data) # десериазизация данных от пользователя
        serializer.is_valid(raise_exception=True) 
        # валидаторы находятся внутри класса DogsSerializer

        post_new = Dog.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            category_id=request.data["category_id"]
        ) # на основе этих данных создается строка в таблице Dog, результат в переменной post_new
        return Response({"post": DogsSerializer(post_new).data}) # объект модели в словарь
        # затем, Responce == JSONRenderer.



# class DogsApiView(generics.ListAPIView):
#     queryset = Dog.objects.all()
#     serializer_class = DogsSerializer # сериализатор будет использоваться представлением 
