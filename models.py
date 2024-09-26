from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Category(models.Model):
    category_name=models.CharField(max_length=100)

class Design(models.Model):
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    description=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    design_name=models.CharField(max_length=100)

class Post(models.Model):
    post_name=models.CharField(max_length=100)
    DESIGN=models.ForeignKey(Design,on_delete=models.CASCADE)
    photo_1=models.CharField(max_length=100)
    photo_2= models.CharField(max_length=100)
    photo_3 = models.CharField(max_length=100)
    description_1=models.CharField(max_length=100)
    description_2 = models.CharField(max_length=100)
    description_3 = models.CharField(max_length=100)

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price = models.BigIntegerField()
    photo=models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)

class Customer(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobilenumber=models.BigIntegerField()
    place=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()

class Order(models.Model):
    DESIGN=models.ForeignKey(Design,on_delete=models.CASCADE)
    CUSTOMER_ID= models.ForeignKey(Customer,on_delete=models.CASCADE)
    date= models.DateField()
    status= models.CharField(max_length=100)
    totalamount= models.CharField(max_length=100)
    quantity=models.BigIntegerField()

class Customized_order(models.Model):
    CUSTOMER=models.ForeignKey(Customer, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)


class Customized_payment(models.Model):
    CUSTOMIZED_ORDER = models.ForeignKey(Customized_order, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    date = models.DateField()
    status = models.CharField(max_length=100)

class Payment(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    CUSTOMER_ID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    date=models.DateField()
    status = models.CharField(max_length=100)

class review_and_rating(models.Model):
    CUSTOMER = models.ForeignKey(Customer,on_delete=models.CASCADE)
    DESIGN = models.ForeignKey(Design,on_delete=models.CASCADE)
    rating= models.CharField(max_length=100)
    review= models.CharField(max_length=100)
    date = models.DateField()






