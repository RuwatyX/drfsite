from django.db import models



class Dog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Dogs'
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'