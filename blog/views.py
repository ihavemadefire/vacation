from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)

def all_dogs(request):
    dogs = Dog.objects.all()
    context = {'dogs': dogs}
    return render(request, 'blog/all_dogs.html', context)

def one_dog(request, pk):
    dog = Dog.objects.get(pk=pk)
    context = {'dog': dog}
    return render(request, 'blog/one_dog.html', context)

def create_dog(request):
    if request.method == "POST":
        dog_form = DogForm(request.POST)
        if dog_form.is_valid():
            dog_form.save()
            messages.success(request, ('Your Doggo was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("all_dogs")
    dog_form = DogForm()
    context = {'dog_form': dog_form}
    return render(request, 'blog/create_dog.html', context)

def update_dog(request, pk):
    dog = Dog.objects.get(pk=pk)
    if request.method == "POST":
        dog_form = DogForm(request.POST, instance=dog)
        if dog_form.is_valid():
            dog_form.save()
            return redirect("one_dog", dog.id)
    else:
        dog_form = DogForm(instance=dog)
    context = {'dog_form': dog_form}
    return render(request, 'blog/update_dog.html', context)

def all_owners(request):
    owners = Owner.objects.all()
    context = {'owners': owners}
    return render(request, 'blog/all_owners.html', context)


def one_owner(request, pk):
    owner = Owner.objects.get(pk=pk)
    context = {'owner': owner}
    return render(request, 'blog/one_owner.html', context)


def create_owner(request):
    if request.method == 'POST':
        owner_form = OwnerForm(request.POST)
        if owner_form.is_valid():
            owner_form.save()
            messages.success(request, ('Your Owner was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("blog:index")
    owner_form = OwnerForm()
    context = {'owner_form': owner_form}
    return render(request, 'blog/create_owner.html', context)


def update_owner(request, pk):
    owner = Owner.objects.get(pk=pk)
    if request.method == 'POST':
        owner_form = OwnerForm(request.POST, instance=owner)
        if owner_form.is_valid():
            owner_form.save()
            return redirect("one_owner", owner.id)
    else:
        owner_form = OwnerForm(instance=owner)            
    context = {'owner_form': owner_form}
    return render(request, 'blog/update_owner.html', context)