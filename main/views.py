from django.shortcuts import render , redirect
from .forms import SignUpForm , tweetform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import tweet
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request,'main/register.html',{'form':form})
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None :
        login(request, user)
        return redirect("main:timeline")

    else:
        return render(request, 'main/login.html',)


def timeline_view(request):
    tweets = tweet.objects.all()

    return render(request,'main/timeline.html',context={"tweets":tweets})


def form(request):
    Form = tweetform()
    if request.method == "POST":
        Form = tweetform(request.POST)
        if Form.is_valid() :
            content = Form.cleaned_data['content']
            user = User.objects.get(pk=request.user.id)

            q = tweet(content=content,author=user, created_at=timezone.now())
            q.save()
            return redirect('main:timeline')

    else:
        return render(request, 'main/form.html', context={'form':Form})
