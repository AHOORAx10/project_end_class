from django.shortcuts import render

# Create your views here.

def home_func(request):
    return render(request,'home_module/home_page.html')