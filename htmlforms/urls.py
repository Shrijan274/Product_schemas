from django.urls import path, reverse
from htmlforms import views

urlpatterns = [
    path("", views.loginindex, name="loginpage"),                       #default login page
    path("signupindex/", views.signupindex, name="signuppage"),         #sign up page to register
    path("forgotpwindex/", views.forgotpwindex, name="forgotpwpage"),   #forgot password page
    path("signup/", views.signup, name="signup"),                       #signing up a new user
    path("resetpassword/", views.resetpassword, name="resetPassword"), 
    path('logging/', views.logging, name='logging'),
    path('product_schemas/', views.schemapage, name='product_schemas'),
    path('resetpassword/<str:email>/',views.newpassword, name='newpassword'),
    path('logout/', views.log_out, name='logout'),
    path('configsave/',views.configsave,name='configsave'),
    path('retrievedata/',views.retrievedata, name='retrievedata'),
    path('CRUDview/',views.CRUDview,name='CRUDview'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('product_schemas/<int:productID>/',views.update_product,name='update_product'),
]


