from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book

# Create your views here.

def get_authors(request, id):

    book = get_object_or_404(Book, id=id)

    return HttpResponse(book.authors.values())