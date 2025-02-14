from rest_framework import serializers
from dogs.models import Dog

class DogsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    # автоматическое заполнение поля текущим пользователем
    class Meta:
        model = Dog
        # fields = ("title", "content", "category") # поля возвращаемые сериализатором клиенту
        # если хотим использовать все поля то __all__  
        fields = "__all__" 


