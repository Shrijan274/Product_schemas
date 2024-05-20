from django.http import HttpResponse
from django.shortcuts import render, redirect
from htmlforms.models import member
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


def loginindex(request):                                 #login page
    template_name="indexlogin.html"
    return render(request, template_name)

def signupindex(request):                                #signup page
    template_name="indexsignup.html"
    return render(request, template_name)

def forgotpwindex(request):                              #forgot password page
    template_name="indexforgotpw.html"
    return render(request, template_name)

def resetpassword(request):
    template_name="newpassword.html"
    return render(request, template_name)

def signup(request):
    if request.method == 'POST':
        email=request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        
        user=member.objects.filter(email=email).exists()
        if user:
            return HttpResponse('Account already exists with this email.')
        else:
            new_user=member(email=email, password=password, firstname=firstname, lastname=lastname)
            new_user.save()
            success='User ' +email+ ' created successfully.'
            return HttpResponse(success)
    return render(request,'indexsignup.html' )

@login_required
def logging(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #checking if email exists or not
        if not member.objects.filter(email=email).exists():
            return HttpResponse('Account doesnt exist')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_schemas')
        else:
            return HttpResponse('Email and Password does not.')
    else:
        return render(request,'indexlogin.html')
    
def resetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if member.objects.filter(email=email).exists():
            return render(request, 'newpassword.html')
        else:
            return HttpResponse('Account with this email doesnt exists.')
    else:
        return render(request, 'indexforgotpw.html')