from django.shortcuts import render, reverse, redirect

def index(request):
    return(request, 'index.html')
