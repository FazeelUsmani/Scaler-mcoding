from django.shortcuts import render
from .models import Post, Comment, Like

# Create your views here.

def create_post(request, text): 
    return "creating posts"


def post(request):
    return "post"


def allpost(request):
    return "all post"

    