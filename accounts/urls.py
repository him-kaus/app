from django.contrib import admin
from django.urls import path, include
from .views import signin, signup, signout, change_password, password_reset_request, email_message,account_verify

app_name = "accounts"   # App name for calling Url's in template/Html

urlpatterns = [
    path('', signin, name="login"),
    path('signout', signout, name="signout"),
    path('signup', signup, name="signup"),
    path('change-password', change_password, name="change-password"),
    path('password_reset/', password_reset_request, name="password_reset"),
    path('email-activation/', email_message, name="email-activation"),
    path('account-verify/<slug:token>',account_verify,name='account_verify')
]
