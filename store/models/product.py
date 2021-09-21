from django.db import models
from.category import category


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(category,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='upload/products/')

    # call all data on index page
    @staticmethod
    def get_all_products():
        return product.objects.all()

    # all categories products
    @staticmethod
    def get_all_categories(category_id):
        if category_id:
            return product.objects.filter(category = category_id)
        else:    
            return product.get_all_products();
