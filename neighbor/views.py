from django.shortcuts import render

# Create your views here.

def index(request):
    # posts=Post.objects.all()
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()
    # else:
    #     form = PostForm()

    # try:
    #     posts = Post.objects.all()
    #     print(posts)
    # except Project.DoesNotExist:
    #     posts = None
    return render(request, 'neigbor/index.html',)

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