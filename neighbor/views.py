from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, PostForm, UpdateUserProfileForm, UpdateUserForm
from django.http import HttpResponseRedirect
from .forms import *

@login_required(login_url='login')
def index(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except:
        return redirect('edit_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None
    return render(request, 'neighbour/index.html', {'posts':posts, 'profile':profile})


def signup(request):
    global register_form
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
        register_form = {
            'form': form,
        }
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    return render(request, 'neighbour/profile.html')

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)


@login_required(login_url='login')
def edit_profile(request, username):
    current_user = request.user
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=current_user)
            form = UpdateUserProfileForm(request.POST,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
        except:
            form = UpdateUserProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
            return redirect('index')
    else:
        if Profile.objects.filter(user=current_user):
            profile = Profile.objects.get(user=current_user)
            form = UpdateUserProfileForm(instance=profile)
        else:
            form = UpdateUserProfileForm()
    return render(request, 'neighbour/update_profile.html', {'form': form} )

@login_required(login_url='login')
def upload(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except:
        return redirect('edit_profile',username = current_user.username)

    try:
        posts = Post.objects.filter(neighborhood = profile.neighborhood)
    except:
        posts = None

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=current_user
            post.neighborhood = profile.neighborhood
            post.save()
        return redirect('index')
    else:
        form = PostForm()
   
    return render(request, 'neighbour/upload.html', {'posts': posts, 'form': form})



