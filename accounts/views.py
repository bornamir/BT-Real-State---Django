from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def register(req):
    if req.method == 'POST':
        # get form values:
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        # chcking 
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(req,'This username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(req,'This email address is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name= last_name)
                    messages.success(req,'You have successfully registered. Now you can login')
                    user.save()
                    return redirect('login')
        else:
            messages.error(req,'Passwords do not match')
            return redirect('register')
    else:
        return render(req,'accounts/register.html')

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username , password= password)

        if user is not None:
            auth.login(req,user)
            messages.success(req, 'You are logged in')
            return redirect('dashboard')

        else:
            messages.error(req,'Invalid credintials')
            return redirect('login')
        return redirect('login')
    else:
        return render(req,'accounts/login.html')


def logout(req):
    if req.method == "POST":
        auth.logout(req)
        messages.success(req,'You are now logged out')
        return redirect('index')


def dashboard(req):
    if req.user.is_authenticated:
        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = req.user.id)

        context = {
            'contacts': user_contacts
        }
        return render(req,'accounts/dashboard.html',context)

    else:
        messages.error(req,'You must login first')
        return redirect('login')