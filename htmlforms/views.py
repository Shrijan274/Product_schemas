import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse,Http404
from django.shortcuts import render, redirect
from htmlforms.models import Product,Item
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import models
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.db import models
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
@cache_page(60 * 15)
@login_required(login_url='/')
def schemapage(request):
    source=request.GET.get('source','')
    product_id=request.GET.get('id')
    try:
        if product_id:
            product=Product.objects.get(pk=product_id)
            schema=json.dumps(product.schema)
            if source == 'addproduct':
                return JsonResponse({'schema':schema})
        print('product_id:',product_id)
        template_name="product_schemas.html"
        return render(request,template_name,locals())
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

@csrf_protect
#@csrf_protect
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
            success='Account with {' +email+ '} email does not exist.'
            return HttpResponse(success)
        else:
            success='Invalid login credentials.'
            return HttpResponse(success)
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

#@cache_page(60 * 15)
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

def schemalist(request):
    template_name="schemalist.html"
    return render(request,template_name)

def productnames(request):
    data=list(Product.objects.values('pk','productName'))
    return JsonResponse(data, safe=False)

def addproduct(request):
    if request.method == 'POST':
        # body_unicode = request.body.decode('utf-8')
        # print(body_unicode)
        body = request.POST.copy()
        body.pop('csrfmiddlewaretoken',None)
        print(body)
        product=request.GET.get("id")
        schema=body.get('schema')
        isactive=body.get('isactive')

        item=Item(product_id=product, data=body, user=request.user)
        item.save()
        success='Item created successfully.Close the page'
        return HttpResponse(success)
    template_name="addproduct.html"
    return render(request,template_name)

def viewlist(request):
    template_name="viewlist.html"
    return render(request,template_name)

def retrieveitems(request):
    data=list(Item.objects.values('pk','product__productName','data'))
    return JsonResponse(data, safe=False)

def goldenlayout(request):
    template_name="goldenlayout.html"
    return render(request,template_name)