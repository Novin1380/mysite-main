from django.urls import reverse
from .Forms import RegisterationForm,AccountAuthenticationForm,LoginForm
from django.http import HttpResponse
from django.core.mail import send_mail , BadHeaderError
from django.contrib.auth.forms import PasswordResetForm ,SetPasswordForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

'''def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AccountAuthenticationForm(data = request.POST)
            #username = request.POST["username"]
            #password = request.POST["password"]
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                
                if not authenticate(email=username, password=password):
                    messages.add_message(request,messages.ERROR,'incorrect login')
                account = authenticate(request, username=username, password=password)
                if account is not None:
                    login(request, account)
                    return redirect('/')

                # Redirect to a success page.
    else :
        return redirect('/')

    
    if request.user.is_authenticated:
        msg = f'You are logged in as {request.user.username} '
    else:
        msg = 'You are not logged in
        
    form = AuthenticationForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)

@login_required
def logout_view(request):
    #if request.user.is_authenticated:
    logout(request)
    return redirect('/')

def signup_view(request):
    user=request.user
    form =RegistrationForm()
    if request.user.is_authenticated:
        return HttpResponse("you are already authenticated as %s"%user.email)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        form = RegistrationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else :
        return redirect('/')
    
def forgot_password_view(request):
    form =RegistrationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                
def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                #send email to user to reset password
                for user in user_email:
                    subject = 'password reset'
                    email_template_name ='accounts/password_message.txt'
                    parameters = {'email': user.email ,
                                'domain' : '127.0.0.1:8000',
                                'site_name':'travel' , 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                'token':default_token_generator.make_token(user),
                                'protokol':'https'
                                }
                    email = render_to_string(email_template_name,parameters)
                    print(parameters)
                    try:
                        send_mail(subject,email,'',[user.email],fail_silently=False)
                    except:
                        return HttpResponse('invalid header')
                    return redirect('accounts:passres')
    else :
        password_form = PasswordResetForm()
    context = {'password_form':password_form}
    return render(request,'accounts/reset_password.html',context)


def password_reset_complete(request):
    return render(request,'accounts/password_reset_complete.html')

def password_reset_proccess(request):
    return render(request,'accounts/password_reset_procces.html')


def change_password(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.POST) 
            password = form.cleaned_data.get('password')
            if password.is_valid():
                data = password.cleaned_data['email']
                
            
            
def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.please login')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.Now you can login')
            return redirect('/accounts/login')
        else:
            messages.error(request, 'token doesnot match and check your mail')
            return redirect('/register')
    except Exception as e:
        print(e)'''
        #return redirect('/')'''




# Create your views here.

def login_View(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if '@' in username:
                kwargs = {'email': username.lower()}
            else:
                kwargs = {'username': username}
            try:
                username = User.objects.get(**kwargs).username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'warning that invalid Username/Email and pssword')
                return render(request, 'accounts/login.html')

    messages.add_message(request, messages.ERROR, 'warning that might need attention.')
    return render(request, 'accounts/login.html',{'form': form})

@login_required(login_url='/accounts/login')
def logout_View(request):
    logout(request)
    return redirect('/')

def signup_View(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                email = email.lower()
                kwargs = {'email': email}
                try:
                    username = User.objects.get(**kwargs).username
                    messages.add_message(request, messages.ERROR, 'warning that invalid Email because used')
                except User.DoesNotExist:
                    form.save()
                    return redirect('/accounts/login')
        form = RegisterationForm()
        return render(request, 'accounts/signup.html',{'form': form})
    else:
        return redirect('/')



    