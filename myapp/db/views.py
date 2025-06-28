from django.shortcuts import render, redirect,get_object_or_404
from .forms import DashboardForm, LoginForm, ContactForm, ForgotPasswordForm
from django.contrib.auth import authenticate, login as auth_login , logout as django_logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dashboard, Post 
#from django.contrib.auth.decorators import login_required

#forgot password


from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request): # type: ignore
    posts = Post.objects.all()

    blog = "Celebration @ AVSEC"

    return render(request,"index.html", {'blog': blog, 'posts': posts}) # type: ignore

# Create your views here.

def detail(request, post_id): # type: ignore
    post = get_object_or_404(Post,pk=post_id)
    return render(request, "detail.html", {'post': post}) # type: ignore
def aboutus(request): # type: ignore
    return render(request,"aboutus.html") # type: ignore



def dashboard(request): # type: ignore
    dashboard = Dashboard.objects.get(user=request.user) 
    return render(request,"dashboard.html",{'dashboard': dashboard})# type: ignore




def register(request):# type: ignore
    
    if request.method == 'POST':# type: ignore
        form = DashboardForm(request.POST, request.FILES)# type: ignore
        if form.is_valid():
            form.save()
            return redirect('db:login')  # redirect to your login page
    else:
        form = DashboardForm()
    return render(request, 'register.html', {'form': form})# type: ignore

def login(request):# type: ignore
    form = LoginForm(request.POST)# type: ignore
    if request.method == 'POST':# type: ignore
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # type: ignore
            

            if user is not None:
                auth_login(request,user)# type: ignore
              
                return redirect('db:dashboard')
            else:
                form = LoginForm()
        else:
            messages.error(request, "Invalid username or password.") # type: ignore
            
    return render (request, 'login.html')# type: ignore



def contact(request): # type: ignore
    form = ContactForm(request.POST) # type: ignore
    if request.method == 'POST': # type: ignore
        print("POST request received")
        if form.is_valid():
            print("FORm is valid")
            print(form.cleaned_data)
            form.save() # type: ignore
            success_message = 'Your Email has been sent!'
            return render(request,'contact.html', {'form':form,'success_message':success_message})# type: ignore
            
    return render(request,"contact.html") # type: ignore

def logout(request):  # type: ignore
    django_logout(request) # type: ignore
    return redirect('db:login')

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "No user found with this email.")
                return redirect('forgot_password')

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain

            subject = "Reset Password Request"
            message = render_to_string('reset_password_email.html', {
                'domain': domain,
                'uid': uid,
                'token': token,
                'user': user,
            })

            send_mail(subject, message, 'saravanannagappan2004@gmail.com', [email])  # You will setup Gmail in settings.py
            messages.success(request, 'Password reset email sent.')
            return redirect('db:forgot_password')
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .forms import ResetPasswordForm

def reset_password(request, uidb64, token):
    UserModel = get_user_model()

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, "Password reset successful.")
                return redirect('db:login')
        else:
            form = ResetPasswordForm()
        return render(request, 'reset_password_form.html', {'form': form})
    else:
        messages.error(request, 'The reset link is invalid or has expired.')
        return redirect('db:forgot_password')
    
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, DashboardUpdateForm

@login_required
def edit_profile(request):
    user = request.user
    dashboard = Dashboard.objects.get(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        dashboard_form = DashboardUpdateForm(request.POST, request.FILES, instance=dashboard)

        if user_form.is_valid() and dashboard_form.is_valid():
            user_form.save()
            dashboard_form.save()
            return redirect('db:dashboard')  # or any success URL
    else:
        user_form = UserUpdateForm(instance=user)
        dashboard_form = DashboardUpdateForm(instance=dashboard)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'dashboard_form': dashboard_form
    })