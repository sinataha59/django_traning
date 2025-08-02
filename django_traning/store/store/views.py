from django.shortcuts import render
from django.http import HttpResponse

def say_hello (request):
    return HttpResponse("hello")
def say_name(request):
    user_name = input("pleas enter your name :   ")
    return HttpResponse(f"hello {user_name}")