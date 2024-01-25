from rest_framework import serializers
from recordApp.models import Book, Customer, Order, OrderItem, Payment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'