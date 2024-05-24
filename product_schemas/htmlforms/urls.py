from django.urls import path

from htmlforms import views

urlpatterns = [
    path("", views.loginindex, name="loginpage"),                       #default login page
    path("signupindex/", views.signupindex, name="signuppage"),         #sign up page to register
    path("forgotpwindex/", views.forgotpwindex, name="forgotpwpage"),   #forgot password page
    path("signup/", views.signup, name="signup"),                       #signing up a new user
    path("resetpassword/", views.resetpassword, name="resetPassword"), 
    path("home/",views.logging,name="product_schemas"),
    path('resetpassword/<str:email>/',views.newpassword, name='newpassword'),
    path('schemapage/',views.schemapage,name='schemapage'),
]


