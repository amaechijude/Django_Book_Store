from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='books'),
    path('books/<int:id>',views.get_all_books, name='booksdel'),
    path('books/<int:id>', views.get_a_book, name='a_book'),
    path('orders/', views.get_all_orders, name='orders'),
    path('orders/<int:id>', views.get_an_order, name='an_order'),
    path('payments/', views.make_payments, name='paid'),
    path('', views.index, name='index'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('addbook', views.addbook, name='addbook'),
    path('authoradd', views.authoradd, name='authoradd'),
    path('records/<int:pk>', views.records, name='records'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
    path('update_book/<int:pk>', views.update_book, name='update_book'),
    path('signup', views.signup, name='signup'),
]
