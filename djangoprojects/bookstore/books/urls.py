from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    path('authors',views.authors, name='authors'),
    path('authordetail/<int:authorid>',views.authorDetails, name='authorDetails')
]