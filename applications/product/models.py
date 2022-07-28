from django.db import models

# Create your models here.


class Category(models.Model):

    title = models.TextField(max_length=50)
    slug = models.SlugField(primary_key=True, max_length=50, unique=True,blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def save(self,*args,**kwargs):
         self.slug = self.title.lower()
         super(Category, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent}> {self.parent}'
        else:
            return self.slug


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name





