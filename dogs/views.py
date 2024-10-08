from django.forms import model_to_dict
from dogs.models import Dog
from dogs.serializers import DogsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class DogsApiView(APIView):
    def get_object(
        self, pk
    ):  # пользовательская функция для проверки пользовательского pk
        # (уникального id объекта модели Dog)
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            return Response({"error": "Current method is not allowed"})

    def get(self, request):
        dogs = Dog.objects.all()
        return Response({"posts": DogsSerializer(dogs, many=True).data})

    def post(self, request):
        # POST запрос с данными от клиента (JSON преобразуется в словарь request.data) в HTTP запросе
        serializer = DogsSerializer(
            data=request.data
        )  # десериазизация данных от пользователя
        serializer.is_valid(
            raise_exception=True
        )  # сохраняет результат в validated_data
        # валидаторы находятся внутри класса DogsSerializer
        serializer.save()  # вызов метода create, результат в атрибуте data
        # каждая функция должна выполнять только одну область действий

        return Response({"posts": serializer.data})

    def put(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        instance = self.get_object(pk=pk)

        serializer = DogsSerializer(data=request.data, instance=instance)
        serializer.is_valid(
            raise_exception=True
        )  # валидированные данные в validated_data
        serializer.save()  # вызовет метод update из-за instance
        return Response({"post": serializer.data})

    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})

        instance = self.get_object(pk=pk, method="DELETE")
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
