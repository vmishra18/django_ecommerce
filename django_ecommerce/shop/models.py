from django.db import models

# Create your models-1 here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    cateogry= models.CharField(max_length=50, default='')
    subcateogry= models.CharField(max_length=50, default='')
    price= models.IntegerField(default=0)

    desc = models.CharField(max_length=200)
    publish_date = models.DateField()
    image= models.ImageField(upload_to='shop/images', default='')


    def __str__(self):
        return self.product_name

# Create your models-2 here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=30, default='')
    phone= models.CharField(max_length=15, default='')
    message= models.CharField(max_length=1000, default='')



    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50, default='')
    address= models.CharField(max_length=100, default='')
    city= models.CharField(max_length=30, default='')
    state= models.CharField(max_length=30, default='')
    zip_code= models.CharField(max_length=10, default='')
    phone= models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):

    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(max_length=50)
    update_desc = models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.update_desc[0:8]+"..."


# add model
# >: python manage.py makemigrations
# >: python manage.py migrate