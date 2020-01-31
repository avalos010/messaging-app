from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is taken!')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is taken!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, 'You are not succesfully registered!')
                    return render(request, 'users/login.html')
        else:
            messages.error(request, 'The Passwords Do Not Match!')
            return redirect('register')
    else:
        return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Succesfully loggedin')
            return redirect('loggedin')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'users/login.html')


def loggedin(request):
    if User.is_authenticated:
        return render(request, 'messages/messages.html')
    else:
        messages.error(request, 'must be logged in to view this page!')
        return render(request, 'users/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('index')


def compose(request):
    return
