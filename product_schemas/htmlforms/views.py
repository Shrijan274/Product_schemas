from django.http import HttpResponse
from django.shortcuts import render, redirect
from htmlforms.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def schemapage(request):
    return render(request,'product_schemas.html')

def loginindex(request):                                 #login page
    template_name="indexlogin.html"
    return render(request, template_name)

def signupindex(request):                                #signup page
    template_name="indexsignup.html"
    return render(request, template_name)

def forgotpwindex(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return redirect('newpassword', email=email)
        else:
            return HttpResponse('Account with the email does not exist.')
    else:
        return render(request, 'indexforgotpw.html')
def resetpassword(request):
    template_name="newpassword.html"
    return render(request, template_name)

def signup(request):
    if request.method == 'POST':
        email=request.POST['email']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        
        user=User.objects.filter(email=email).exists()
        if user:
            return HttpResponse('Account already exists with this email.')
        else:
            new_user=User(email=email, password=password, firstname=firstname, lastname=lastname)
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
        if not User.objects.filter(email=email).exists():
            return HttpResponse('Account doesnt exist')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(request,'product_schemas.html')
        else:
            return HttpResponse('Email and Password does not match.')
    else:
        return render(request,'indexlogin.html')
    
def newpassword(request, email):
    if request.method == 'POST':
        password = request.POST.get('password')
        User.objects.filter(email=email).update(password=password)
        return HttpResponse('Password has been updated.')
    else:
        return render(request, 'newpassword.html', {'email': email})
    
