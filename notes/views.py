from django.shortcuts import render, redirect
from .models import Tweet
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import NewTweet


# Create your views here.
def tweet_display(request):
    if request.method == 'POST':
        form = NewTweet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    tweets = Tweet.objects.all()
    form = NewTweet()
    context = {
        'tweets': tweets,
        'form': form
    }
    return render(request, 'index.html', context)

# create tweet
