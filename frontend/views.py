from django.shortcuts import render, reverse, redirect

def index(request):
    return render(request, 'frontend/index.html')
