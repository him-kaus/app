# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .forms import RegisterForm,MySignInForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings

# email verification
from verify_email.email_handler import send_verification_email

from .models import Profile
import uuid

def send_email_after_registration(email,token):
    subject = "Verify Email"
    message = f'hi, click on link for verify http://127.0.0.1:8000/accounts/account-verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

def signup(request):
    if request.user.is_authenticated:
        return redirect('core:appointments')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        phonenumber = request.POST.get('phonenumber')
        if form.is_valid():
            new_user = form.save()
            uid = uuid.uuid4()
            pr_obj = Profile(User=new_user,token=uid)
            pr_obj.save()
            send_email_after_registration(new_user.email,uid)
            messages.success(request,"your account created successfully")
            # inactive_user = send_verification_email(request, form)  # Send verification email to in-active user
            #
            # request.session['email'] = inactive_user.email  # save email in session, to add the same email for person
            # Profile.objects.create(User=inactive_user, PhoneNumber=phonenumber)
            return redirect('accounts:email-activation')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})

def account_verify(request,token):
    pf = Profile.objects.filter(token=token).first()
    pf.verify = True
    pf.save()
    return redirect('accounts:login')

@csrf_exempt
def signin(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('core:appointments')
    if request.method == 'POST':
        # fm = AuthenticationForm()
        fm = MySignInForm(request,data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

        # username = request.POST['username']
        # password = request.POST['password']

            user = authenticate(username=username, password=password)  # authenticate user's, email and password
        # print(user)
            pro = Profile.objects.get(User=user)
            if pro.verify:
                login(request, user)
                return redirect('core:appointments')
            else:
                error = 'Invalid Username or Password'
                form = AuthenticationForm(request.POST)
                return render(request, 'accounts/login.html', {'form': form, 'error': error})
        return redirect('core:book')



        # if user is not None:
        #     login(request, user)
        #     return redirect('core:book')


    else:
        form = AuthenticationForm()
        return render(request, 'core/book-appointment.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('accounts:login')


def password_reset_request(request):  # password reset for loged-out user
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']  # get user entered email
            associated_users = User.objects.filter(Q(email=data))  # find associated user with that email
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.txt"  # email body stored in txt file
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)  # All email data rendered as string
                    try:
                        send_mail(subject, email, 'panda.throwawayyy@gmail.com', [user.email],
                                  fail_silently=True)  # Send Email
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


@login_required
def change_password(request):  # change password for logged-in user
    message = ''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # converting password to hash
            message = 'Password changed successfully'
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'core/change-password.html', {'form': form, 'message': message})


def email_message(request):  # Show a message after signup process, to check email for verification
    return render(request, 'accounts/email_message.html')
