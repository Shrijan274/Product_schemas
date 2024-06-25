import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from htmlforms.models import User,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required(login_url='/')
def schemapage(request):
    product_id=request.GET.get('id')
    if product_id:
        product=Product.objects.get(pk=product_id)
        schemas=json.dumps(product.schema)


      
    print('product_id:',product_id)
    template_name="product_schemas.html"
    return render(request,template_name,locals())

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
            new_user=User.objects.create_user(username=email,email=email, password=password, first_name=firstname, last_name=lastname)
            new_user.save()
            success='User ' +email+ ' created successfully.'
            return HttpResponse(success)
    return render(request,'indexsignup.html' )

def logging(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/product_schemas/')
        if not User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Account does not exist.'})
        else:
            return JsonResponse({'message': 'Invalid login credentials.'})
    else:
        return render(request,'indexlogin.html')
    
def newpassword(request, email):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = User.objects.get(username=email)
        u.set_password(password)
        u.save()
        return HttpResponse('Password has been updated.')
    else:
        return render(request, 'newpassword.html', {'email': email})
    
def log_out(request):
    logout(request)
    return render(request,'indexlogin.html')

def configsave(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        productname=body.get('productname')
        schema=body.get('schema')
        isactive=body.get('isactive')

        product=Product(productName=productname, schema=schema, is_active=isactive)
        product.save()
        return JsonResponse({'message': 'Product saved successfully.'})

def retrievedata(request):
    data=list(Product.objects.values('pk','productName','is_active'))
    return JsonResponse(data, safe=False)

def CRUDview(request):
    return render(request, 'CRUD.html')

@require_POST
def delete_product(request):
    product_id = request.POST.get('product_id')
    if product_id:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False}, status=400)
    
def configupdate(request):
    product_id=request.GET.get('id')
    print('product_id:',product_id)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    productname=body.get('productname')
    schema=body.get('schema')
    isactive=body.get('isactive')
    Product.objects.filter(id=product_id).update(productName=productname, schema=schema, is_active=isactive)
    return JsonResponse({'message': 'Product updated successfully.'})