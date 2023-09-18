from django.db import models
from django.contrib.auth.models import User  
import datetime

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    u_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False
class contact(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=11)
    desc= models.TextField()
    date=models.DateField()

    def __str__(self) :
        return self.name
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    category=models.CharField(max_length=50 ,default="")
    sub_category=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="home/images", default="")
    # def __str__(self) :
    #     return self.product_name
    @ staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids )
class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
