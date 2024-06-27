from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User


from .forms import SignUpForm, UserUpdateForm, AccUpdateForm

from . import models

# Create your views here.
def index(request):
    users = User.objects.all().exclude(pk=request.user.id)
    rooms = models.Room.objects.all()
    return render(request, 'chatback/index.html')

def room(request, room_name):
    return render(request, 'chatback/room.html', {
        'room_name': room_name
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('name')
            messages.success(request, f'Аккаунт создан! Можете войти!')
            return redirect('login.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    user_update_form = UserUpdateForm(request.POST, instance=request.user)
    acc_update_form = AccUpdateForm(request.POST, request.FILES, instance=request.user.account)
    context = {
        'user_update_form': user_update_form,
        'account_update_form': acc_update_form
    }
    return render(request, 'account.html', context)

