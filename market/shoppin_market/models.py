from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email=models.CharField(max_length=70)
  address=models.CharField(max_length=100,null=True)
  phoneNo=models.CharField(max_length=70)
  password=models.CharField(max_length=70)
  CreatedDate = models.DateTimeField(auto_now_add=True)
  UpdatedDate=models.DateTimeField(null=True)
  CreatedBy=models.CharField(max_length=70,null=True)
  UpdatedBy=models.CharField(max_length=70,null=True)

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.BigIntegerField()

class Orders(models.Model):
	UserID=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_order')
	active = models.BooleanField(default=True)

class OrderProduct(models.Model):
	OrderID=models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_of_products')
	ProductID=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_order')
	amount = models.BigIntegerField()

