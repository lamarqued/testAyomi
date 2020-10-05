from django.shortcuts import render, redirect
from greatuserapp.forms import EditProfileForm
from django.contrib.auth.models import User

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'greatuserapp/index.html')
    elif request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            args = {'form': form}
        else:
            args = {'form': form, 'badadress': True}
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'greatuserapp/index.html', args)

def redirection(request):
    return redirect("/accounts/login/")