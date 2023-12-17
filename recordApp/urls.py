from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='books'),
    path('books/<int:id>', views.get_a_book, name='a_book'),
    path('orders/', views.get_all_orders, name='orders'),
    path('orders/<int:id>', views.get_an_order, name='an_order'),
    path('payments/', views.make_payments, name='paid')
]