from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from .forms import RegisterForm, AddRecordForm, AuthorForm
from rest_framework.parsers import JSONParser
from recordApp.models import Book, Customer, Order, OrderItem, Payment
from recordApp.serializers import BookSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer


#Views
#frontend signup
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #Authnenticate and sign in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Signed Up! Welcome!")
            return redirect('index')
        else:
            form = RegisterForm()
            messages.info(request, "{Error: Could not Sign Up}")
            form_content = {"form": form}
            return render(request, 'signup.html', form_content)
        
    form = RegisterForm()
    messages.info(request, "Welcome to Sign Up page")
    form_content = {"form": form}
    return render(request, 'signup.html', form_content)

#logout
def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('index')

#Frontend homepage
def index(request):
    all_bookSerializer = Book.objects.all()
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
        
def addbook(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully Added Book")
            return redirect('index')
        else:
            form = AddRecordForm()
            messages.info(request, "{Error: Could not Add Book}")
            return render(request, 'addbook.html', {"form": form})
    form = AddRecordForm()
    return render(request, 'addbook.html', {"form": form})

def authoradd(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully Added Author")
            return redirect('addbook')
        else:
            form = AuthorForm()
            messages.info(request, "{Error: Could not Add Author}")
            return render(request, 'authoradd.html', {"form": form})
    form = AuthorForm()
    return render(request, 'authoradd.html', {"form": form})

def records(request, pk):
    if request.user.is_authenticated:
        book_record = Book.objects.get(BookID=pk)
        return render(request, 'records.html', {"book_record": book_record})
    else:
        messages.info(request, "You need to be logged in")
        return redirect('index')

def delete_book(request, pk):
    if request.user.is_authenticated and request.user.is_staff:
        book_record = Book.objects.get(BookID=pk)
        book_record.delete()
        messages.info(request, "Successfully Deleted")
        return redirect('index')
    else:
        messages.info(request, "{Error: Could not delete. You are not an Admin}")
        return redirect('index')

def update_book(request, pk):
    if request.user.is_authenticated:
        current_book = Book.objects.get(BookID=pk)
        form = AddRecordForm(request.POST or None, instance=current_book)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully Updated Book")
            return redirect('index')
        return render(request, 'update_book.html', {"form": form})
    messages.info(request, "You need to be logged in")
    return redirect('index')


@csrf_exempt
def get_all_books(request, id=0):
    if request.method == 'GET':
        all_books = Book.objects.all()
        all_bookSerializer = BookSerializer(all_books, many=True)
        return JsonResponse(all_bookSerializer.data, safe=False)
    elif request.method == 'POST':#(admin only) to be modified later
        book_data = JSONParser().parse(request)
        book_dataSerializer = BookSerializer(data=book_data)
        if book_dataSerializer.is_valid():
            book_dataSerializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method == 'PUT':#(admin only) to be modified later
        book_change = JSONParser().parse(request)
        book_update = Book.objects.get(BookID=book_change['BookID'])
        book_updateSerializer = BookSerializer(book_update, data=book_change)
        if book_updateSerializer.is_valid():
            book_updateSerializer.save()
            return JsonResponse("Updated Succefully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE': #(admin only) to be modified later
        book_delete = Book.objects.get(BookID=id)
        book_delete.delete()
        return JsonResponse("Deleted Succefully",safe=False)

@csrf_exempt
def get_a_book(request, id):
    if request.method == 'GET':
        a_book = Book.objects.get(BookID=id)
        a_bookSerializer = BookSerializer(a_book, many=False)
        return JsonResponse(a_bookSerializer.data, safe=False)


@csrf_exempt
def get_all_orders(request):#(admin only) to be modified later
    if request.method == 'GET':
        all_orders = Order.objects.all()
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
        an_order = Order.objects.get(OrderID=id)
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
