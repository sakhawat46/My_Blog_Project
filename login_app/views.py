from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login_app.forms import SignUpForm, ProfileChangeForm, ProfilePic

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    register = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            register = True

    diction = {'form':form, 'register':register}
    return render (request, 'login_app/sign_up.html', context=diction)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'login_app/login_page.html', context={'form':form})


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render (request, 'login_app/profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = ProfileChangeForm(instance=current_user)
    if request.method =='POST':
        form = ProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = ProfileChangeForm(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:profile'))
    return render (request, 'login_app/change_profile.html', context={'form':form})


@login_required
def password_change(request):
    current_user = request.user
    change = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data = request.POST)
        if form.is_valid():
            form.save()
            change = True
    return render (request, 'login_app/change_pass.html', context={'form':form, 'change':change})


@login_required
def add_profile_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_object = form.save(commit=False)
            user_object.user = request.user
            user_object.save()
            return HttpResponseRedirect(reverse('login_app:profile'))
    return render (request, 'login_app/add_pro_pic.html', context={'form':form})


@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_app:profile'))
    return render (request, 'login_app/add_pro_pic.html', context={'form':form})