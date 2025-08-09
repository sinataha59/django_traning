from django.db import models
class category (models.Model):
    title = models.CharField(max_length = 256)
    slug = models.TextField()


class discount(models.Model):
    discount = models.FloatField()
    discription = models.CharField(max_length = 255)

class product(models.Model):
    name = models.CharField(max_length = 250)
    slug =models.SlugField(max_length = 200 )
    category = models.ForeignKey(category , on_delete =models.CASCADE)
    price = models.DecimalField(max_digits= 5, decimal_places=2) 
    datetime_created = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now = True)
    inventory = models.IntegerField()
    discount =models.ManyToManyField(discount)

class customer (models.Model):
    name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length = 255)
    birthdate = models.DateField(blank = True)
    postoal_code = models.CharField(max_length=250)

class addres (models.Model):
    name = models.OneToOneField(customer, on_delete = models.CASCADE , primary_key = True)
    province = models.CharField(max_length = 255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length = 255)



class order (models.Model):
    PAIED_ORDER = "P"
    UNPAIED_ORDER = "U"
    CANCELED_ORDER = "C"
    ORDER_ITEM =[
        (PAIED_ORDER,"paid"),
        (UNPAIED_ORDER , "unpaid"),
        (CANCELED_ORDER , "canceled"),
    ]
    
    customer =models.ForeignKey(customer,on_delete =models.PROTECT)
    datetime_created =models.DateTimeField(auto_now_add = True)
    order_status = models.CharField(max_length = 255 , choices = ORDER_ITEM , default = UNPAIED_ORDER)
    
class order_item(models.Model):
    order = models.ForeignKey(order, on_delete=models.PROTECT)
    product = models.ForeignKey(product , on_delete = models.PROTECT)
    inventry = models.SmallIntegerField()
    price = models.DecimalField( max_digits=6, decimal_places=2)
    class Meta:
        unique_together =[["order",'product']]

class comment(models.Model):
    name = models.ForeignKey(customer , on_delete = models.CASCADE)
    product =models.ForeignKey(product , on_delete = models.CASCADE)
    APPROVED = "A"
    NOT_APPROVED = "NA"
    WAITE = "W"
    STATUS_ITEM =[
        (APPROVED , "approved yor comment"),
        (NOT_APPROVED , "your comment does not approved"),
        (WAITE , "waiting for look"),
    ]
    
    slug = models.TextField(max_length = 1000)
    datetime_created = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now= True)
    status =models.CharField(max_length = 2 , choices =STATUS_ITEM , default =WAITE)


class cart(models.Model):
    datetime_created =models.DateTimeField( auto_now=False, auto_now_add=True)

class cart_item(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.PROTECT)
    product = models.ForeignKey(product , on_delete = models.PROTECT)
    inventry = models.SmallIntegerField()
    class Meta:
        unique_together =[["cart",'product']]