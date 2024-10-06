from rest_framework import serializers

from rest_framework.parsers import JSONParser


class DogsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    time_updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# class DogsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255) # автоматически проверка длины
#     # нужно для того, чтобы сериалайзер знал какого типа атрибут
#     content = serializers.CharField() # TextField и CharField объединены в один


# class DogsModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# def encode(): # преобразование объектов класса в JSON
#     model = DogsModel("Yaroslav", "My name is Yaroslav")
#     model_sr = DogsSerializer(model)
#     # передаем объект модели в  сериалайзер, получаем объект сериалайзера
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # сериализованные данные, то есть словарь (model_sr.data)
#     json = JSONRenderer().render(model_sr.data)
#     # преобразование данных в JSON (байтовая строка JSON)
#     print(json)

# def decode():
# stream = io.BytesIO(b'{"title":"Yaroslav","content":"My name is Yaroslav"}') # поток байтового JSON файла
# data = JSONParser().parse(stream)
# serializers = DogsSerializer(data=data) # при декодировании используем параметр data
# serializers.is_valid() # проверка корректности принятых данных.
# print(serializers.validated_data)


# class DogsSerializer(serializers.ModelSerializer): # работает с моделями
#     # берем определенные записи и представляем их в формате JSON
#     class Meta:
#         model = Dog
#         fields = ("title", "category_id")
