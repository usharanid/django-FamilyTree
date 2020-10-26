from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'login/home.html')

def passwordsuccess(request):
    return render(request, 'login/passwordsuccess.html')


def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login:psc')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/changepassword.html', {'form': form})

def logout(request):
    auth.logout(request)
    return render(request, 'login/logout.html')

def success(request):
    return render(request, 'login/success.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']



        user=auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect("login:success")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("login:lgn")

    else:
        return render(request,'login/login.html')

def signup(request):

  if request.method == 'POST':
      username=request.POST['UserName']
      password1=request.POST['password1']
      password2=request.POST['password2']
      email=request.POST['email']


      if password1==password2:
          if User.objects.filter(username=username).exists():
              messages.info(request,"Username Taken")
              return redirect("login:account_signup")
          elif User.objects.filter(email=email).exists():
              messages.info(request,"Email already exists")
              return redirect("login:account_signup")
          else:
              user=User.objects.create_user(username=username,password=password1,email=email)
              user.save();
              messages.info(request, "Signup completed Successfully")
              return redirect("login:account_signup")
      else:
          messages.info(request, "Password not matching")
          return redirect("login:account_signup")



  else:
    return render(request,'login/signup.html')
