from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from rest_framework.parsers import JSONParser
from recordApp.models import Books, Customers, Orders, OrderItems, Payments
from recordApp.serializers import BookSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer


def index(request):
    all_books = Books.objects.all()
    all_bookSerializer = BookSerializer(all_books, many=True).data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
		# Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('index')
    else:
        return render(request, 'index.html', {'all_bookSerializer':all_bookSerializer})

@csrf_exempt
def get_all_books(request, id=0):
    if request.method == 'GET':
        all_books = Books.objects.all()
        all_bookSerializer = BookSerializer(all_books, many=True)
        return JsonResponse(all_bookSerializer.data[0], safe=False)
    elif request.method == 'POST':#(admin only) to be modified later
        book_data = JSONParser().parse(request)
        book_dataSerializer = BookSerializer(data=book_data)
        if book_dataSerializer.is_valid():
            book_dataSerializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':#(admin only) to be modified later
        book_change = JSONParser().parse(request)
        book_update = Books.objects.get(BookID=book_change['BookID'])
        book_updateSerializer = BookSerializer(book_update, data=book_change)
        if book_updateSerializer.is_valid():
            book_updateSerializer.save()
            return JsonResponse("Updated Succefully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE': #(admin only) to be modified later
        book_delete = Books.objects.get(BookID=id)
        book_delete.delete()
        return JsonResponse("Deleted Succefully",safe=False)

@csrf_exempt
def get_a_book(request, id):
    if request.method == 'GET':
        a_book = Books.objects.get(BookID=id)
        a_bookSerializer = BookSerializer(a_book, many=False)
        return JsonResponse(a_bookSerializer.data, safe=False)


@csrf_exempt
def get_all_orders(request):#(admin only) to be modified later
    if request.method == 'GET':
        all_orders = Orders.objects.all()
        all_orderSerializer = OrderSerializer(all_orders, many=True)
        return JsonResponse(all_orderSerializer.data, safe=False)
    elif request.method == 'POST':
        new_order = JSONParser().parse(request)
        new_orderSerializer = OrderSerializer(data=new_order)
        if new_orderSerializer.is_valid():
            new_orderSerializer.save()
            return JsonResponse("Posted order succeffully", safe=False)
        return JsonResponse("Failed to post orde", safe=False)

@csrf_exempt
def get_an_order(request, id):
    if request.method == 'GET':
        an_order = Orders.objects.get(OrderID=id)
        an_orderSerializer = OrderSerializer(an_order, many=False)

@csrf_exempt
def make_payments(request):
    if request.method == 'POST':
      pay_data = JSONParser().parse(request)
      pay_dataSerializer = PaymentSerializer(data=pay_data)
      if pay_dataSerializer.is_valid():
        pay_dataSerializer.save()
        return JsonResponse("Paid succefully", safe=False)
    return JsonResponse("Payment error", safe=False)