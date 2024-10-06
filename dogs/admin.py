from django.contrib import admin
from dogs.models import Dog, Category  
# Register your models here.
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "time_created", "is_published"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]