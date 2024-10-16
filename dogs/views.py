from dogs.models import Category, Dog
from dogs.serializers import DogsSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response



class DogViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # предоставляет весь функционал методов
    # queryset = Dog.objects.all()
    serializer_class = DogsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk: # GET list; POST
            return Dog.objects.all()[:3]
        return Dog.objects.filter(pk=pk) 
    # get не подходит, т.к. данный метод обязан возвращать список, а не одну запись при get


    @action(methods=["get"], detail=True) # дополнительный маршрут для вывода категории по id
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({"category": cats.name})


    @action(methods=["get"], detail=False)
    def categories(self, request):
        cats = Category.objects.all()
        return Response({"categories": list(c.name for c in cats)})





# class DogAPIList(generics.ListCreateAPIView): # реализует get и post запросы 
#     queryset = Dog.objects.all() # в данном примере все объекты модели будут возвращены клиенту
#     # queryset - список записей возвращаемых клиенту (serializer возвращает конкретные поля записей)
#     # запрос в бд для получение записей на основае queryset, передача их сериализатору 
#     serializer_class = DogsSerializer


# class DogAPIUpdate(generics.UpdateAPIView):
#     queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
#     serializer_class = DogsSerializer
    
#     def put(self, request, *args, **kwargs):
#         return super().put(request, *args, **kwargs)
    

# class DogAPIDetailView(generics.RetrieveUpdateDestroyAPIView): 
#     # для одной конкретной записи CRUD операции
#     queryset = Dog.objects.all() # ленивый запрос, просто связывание queryset c моделью
#     serializer_class = DogsSerializer