from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'auth/signup.html', {'form': form})



def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
        return redirect('login')
    return render(request, 'user/signin.html')


@login_required
def log_out(request):
    logout(request)
    return render(request, 'user/signin.html')