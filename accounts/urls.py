from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #login
    path('login/',views.login_View,name='login'),
    #logout
    path('logout/',views.logout_View,name='logout'),
    #registeration(signin or singup)
    path('signup/',views.signup_View,name='signup'),
    #forgot-password
    #path('password_reset/',views.password_reset_request,name='reset'),
    #send an email
    #path('password_reset_email/',views.password_reset_proccess,name='passres'),
    #change_password
    #path('change_password/',views.change_password,name='change_password'),
    #successfully
    #path ('password_reset_complete/',views.password_reset_complete,name='complete'),
]