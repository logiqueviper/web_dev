from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [int(i) for i in range(1,21)]
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html')
def option(request):
    first = int(request.GET['fname'])
    last = int(request.GET['lname'])
    listnums = []
    if (first < last):
        for i in range(first,last+1):
            listnums.append(i)
        context = {
            'list':listnums,
        }
        return render(request,'blog/option.html',context)
    return HttpResponse('<p> First number should be less than last number </p>')


    