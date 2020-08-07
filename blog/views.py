from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registration,Get_Email
from .models import User
# Create your views here.
def home(request):
    return render(request,'blog/home.html')
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
def getdata(request):
    if request.method == 'POST':
        demo_reg = Registration(request.POST)
        if demo_reg.is_valid():
            curr_name = demo_reg.cleaned_data['name']
            curr_email =demo_reg.cleaned_data['email']
            curr_password = demo_reg.cleaned_data['password']
            curr_user = User(name = curr_name,email=curr_email,password=curr_password)
            curr_user.save()
    else:
        demo_reg = Registration()
    return render(request,'blog/getdata.html',{'demo_form':demo_reg})
def inp_data(request):
    curr_form = Get_Email()
    
    return  render(request,'blog/get_email.html',{ 'curr_form' : curr_form})
def display_rel_data(request):
    if (request.method == 'POST'):
        email_form = Get_Email(request.POST)
        email = email_form.cleaned_data['email']
        obj = Registration.objects.get(email = email)
        context_dict = {
            'name_user':obj.name,
            'email_user':obj.email,
            'password_user':obj.password
        }
    return render(request, 'blog/show_details.html',context_dict)