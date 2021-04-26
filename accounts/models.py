from django.db import models

# Create your models here.

# Simple Customer model with 4 fields


class Customer(models.Model):
    # Field variables extend from the models class
    # It is good practice to have  the null=True b/c this prevents users from passing null values within the database
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    # DateTimeField is one of many fields that extend from models
    # The parameter auto_now_add is a built method that returns the time the object was created
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # This class level function returns the name of the Customer in the admin portal insteal of the default django ID ex. Customer(1)
    def __str__(self):
        return self.name

# Simple Product model with dicitonary


class Product(models.Model):
    # Dicitonary definition in django syntax
    # The key is defined on the left and its value to the right
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    # By adding the chocies parameter in CharField we are able to define the values that populate the dropdoown for the variable in our application
    # We set choices = to the dictionary above
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# Simple Order model w/ dicitionary
# Refer to Product Model for class logic


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # customer =
    # product =
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
