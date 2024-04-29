from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
path('index',views.index,name='index'),
path('book',views.books,name ='books'),
path('update/<int:id>', views.update, name='update'),
path('delete/<int:id>',views.delete, name = 'delete'),


]