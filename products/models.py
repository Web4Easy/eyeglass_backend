from django.db import models
from base.models import BaseModel
from users.models import User
# Create your models here.
class Product(BaseModel):
    title = models.CharField(max_length=1000)
    code = models.IntegerField()
    brand = models.CharField(max_length=1000)
    model_number = models.IntegerField()
    GENDER_CHOICES = (
        ("M","Male"),
        ("F","Female"),
        ("A","Adult"),
        ("K","Kid")
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to="frames/",blank=True,null=True)
    # category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, null=True, blank=True, decimal_places=2)
    count_in_stock = models.IntegerField(null=True, blank=True, default=0)



    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
    def __str__(self):
        return self.title
    

class ProductImages(models.Model):

    image = models.ImageField(null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.rating)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.created_at)



class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.name)



class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE,null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.address)