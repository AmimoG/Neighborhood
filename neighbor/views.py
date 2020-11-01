from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
from .forms import SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingsForm
from django.http import HttpResponseRedirect
from .forms import *


def index(request):
    posts=Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    # try:
    #     posts = Post.objects.all()
    #     print(posts)
    # except Project.DoesNotExist:
    #     posts = None
    return render(request, 'neighbour/index.html', {'form': form, 'posts':posts})


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
            return redirect('/')
    else:
        form = SignupForm()
        register_form = {
            'form': form,
        }
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
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
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        uform = UpdateUserForm(instance=request.user)
        pform = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': uform,
        'prof_form': pform,
    }
    return render(request, 'neighbour/update_profile.html', params)


def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        posts = Project.objects.all()
        print(posts)
    except Project.DoesNotExist:
        posts = None
        return redirect('home')
    return render(request, 'upload.html', {'posts': posts, 'form': form})


def home(request):
    current_user = request.user
    project_images = Project.fetch_all_images()
    image_params = {
        'all_images': project_images,
        'current_user': current_user,
    }
    return render(request, "neighbour/index.html", image_params)


def rate(request):
    ratings = Rate.objects.all()
    rate_params = {
        'ratings': ratings
    }

    return render('project.html', rate_params)


def profile(request):
    profile = Profile.get_profile_data()
    profile_data = {
        'profile': profile
    }

    return render('userprofile.html', profile_data)


@login_required(login_url='login')
def project(request, post):
    post = Post.objects.get(title=post)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'project.html', params)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, '/award/search_results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'neighbour/search_result.html', {'message': message})

@login_required
def upload(request):
    current_user=request.user
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=current_user
            project.save()
        return redirect('index')
    
    else:
        form=PostForm()
        
    return render(request,'upload.html',{'form':form})