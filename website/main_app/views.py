from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ContactForm
from .models import contact
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'main_app/home.html', context)


def women_rights(request):
    return render(request, 'main_app/women_rights.html', {'title': 'women_rights'})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created Successfully: {username}")
            login(request, user)
            messages.info(request, f"Logged in as {username}")
            return redirect('main_app:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")

    form = UserCreationForm
    return render(request, 'main_app/register.html', context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main_app:home")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Successfully logged in as {username} !")
                return redirect("main_app:home")
            else:
                messages.error(request, f"Invalid username or password {username} ")
        else:
            messages.error(request, "Invausername or password  ")

    form = AuthenticationForm
    return render(request, "main_app/login.html", {'form': form})

# @login_required(login_url='login/')
def emergency_contact(request):
    users = User.objects.all()
    curr = 0
    for user in users:
        if request.user.is_authenticated:
            curr = user
            break
    user = curr
    contacts = contact.objects.filter(user=user)
    total_contacts = contacts.count()
    context = {'contacts': contacts, 'total_contacts': total_contacts, 'user':user}

    return render(request, 'main_app/emergency_contact.html', context)


def create_contact(request):
    users = User.objects.all()
    curr = 0
    for user in users:
        if request.user.is_authenticated:
            curr = user
            break
    inst = contact(user=curr)
    form = ContactForm(instance=inst)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            messages.info(request, f"Successfully created new contact !")
            # request.user.contact.add(form)
            return redirect('main_app:home')

        messages.error(request, f"Invalid username or password")
    # messages.error(request, f"Invalid contact!!")
    context = {'form': form}
    return render(request, 'main_app/create_contact.html', context)


def update_contact(request, pk):
    curr_contact = contact.objects.get(id=pk)
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=curr_contact)
        if form.is_valid():
            form.save()
            return redirect('main_app:home')

    context = {'form': form}
    return render(request, 'main_app/create_contact.html', context)


def delete_contact(request, pk):
    curr_contact = contact.objects.get(id=pk)
    if request.method == "POST":
        curr_contact.delete()
        return redirect('main_app:home')

    context = {'item': curr_contact}
    return render(request, 'main_app/delete_contact.html', context)

