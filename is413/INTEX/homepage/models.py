from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''User (Extends AbstractUser)''' 
    #username
    #first_name
    #last_name
    #email
    #is_staff
    #is_active
    #date_joined
    #security_question = models.TextField(max_length=100)

    phone = models.TextField(max_length=100)
    account_balance = models.IntegerField(default=0)
    full_name = models.TextField()

    # for password reset
    temp_password = models.TextField(null=True)
    activation_key = models.TextField(null=True)
    expiration_date = models.DateField(null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Venue(models.Model):
    '''Venue'''
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    street = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=100)
    zip_code = models.TextField(max_length=100)


    def __str__(self):
        return self.name

class Event(models.Model):
    '''Event'''
    name = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    venue = models.ForeignKey(Venue, null=True)

    def __str__(self):
        return self.name

class Area(models.Model):
    '''Area'''
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    venue = models.TextField(max_length=100)
    event = models.ForeignKey(Event)

    def __str__(self):
        return self.name

class Area_Item(models.Model):
    '''Product'''
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    area = models.ForeignKey(Area)

    def __str__(self):
        return self.name + ': ' + str(self.price)

class Item(models.Model):
    '''Item'''
    name = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    value = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    rental_price = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    available = models.BooleanField(default = True)
    condition = models.TextField(null=True)

    def __str__(self):
        return self.name + ': ' + str(self.value)

class Product(models.Model):
    '''Product'''
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.TextField(max_length=100)
    current_price = models.DecimalField(max_digits=7,decimal_places=2, null=True)

    def __str__(self):
        return self.name + ': ' + str(self.current_price)

class Rental(models.Model):
    description = models.TextField(max_length=500, null=True)
    rental_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    user = models.ForeignKey(User, null=True)
    item = models.ForeignKey(Item, null=True)
    charge_id = models.TextField(null=True)
    returned = models.BooleanField(default = False)

    def __str__(self):
        return 'Rental: ' + self.description + ', Due Date: ' + str(self.due_date)

class Order(models.Model):
    order_date = models.DateField(null=True)
    total = models.DecimalField(max_digits=7,decimal_places=2, null=True)
    user = models.ForeignKey(User, null=True)
    charge_id = models.TextField(null=True)

    def __str__(self):
        return 'Order for: ' + self.user.first_name + ' ' + self.user.last_name

class Address(models.Model):
    street = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    zip_code = models.TextField(null=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.street + ', ' + self.city + ', ' + self.state + ' ' + self.zip_code
