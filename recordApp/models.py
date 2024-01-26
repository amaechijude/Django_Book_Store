from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    Authors_Name = models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.Authors_Name}")


class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Authors_Name = models.ForeignKey(Author, on_delete=models.CASCADE)
    Price = models.FloatField()
    Stock = models.IntegerField()
    
    def __str__(self):
        return (f"{self.Title}")


class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    PasswordHash = models.CharField(max_length=100)#to be modified later
    IsAdmin = models.CharField(max_length=100)#to be modified later
    
    def __str__(self):
        return (f"{self.Name}")

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    OrderItem_ID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.FloatField()

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Amount = models.FloatField()
    PaymentDate = models.DateTimeField(auto_now_add=True)
