from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import CustomUserCreationForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


def home(request):
    if request.user.is_superuser:
        return render(request, "dashboards/admin_dashboard.html")
    elif request.user.is_staff:
        return render(request, "bases/employee_base.html")
    elif request.user.is_active:
        return render(request, "bases/user_base.html")
    else:
        return render(request, "index.html")


def register(request):

    if request.method == "GET":
        return render(
            request, "registration/signup.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
    else:
        return redirect(reverse("register"))


def list_users(request):
    users = User.objects.all()
    profile = Profile.objects.all()
    context = {'users': users, 'profile': profile}
    return render(request, "users/list_users.html", context)


def view_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(Profile, pk=pk)
    context = {'user': user, 'profile': user_profile}
    return render(request, "users/view_user.html", context)


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST or None, instance=user)
        form_profile = ProfileForm(instance=user_profile)
        if form.is_valid():
            form.save()
            context = {'form': form}
            context = {'user': user, 'form': form, 'profile': form_profile}
            return render(request, "users/view_user.html", context)
    else:
        form = UserForm(instance=user)
        form_profile = ProfileForm(instance=user_profile)
    context = {'user': user, 'form': form, 'profile': form_profile}
    return render(request, "users/edit_user.html", context)


def del_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    context = {'user': user}
    return render(request, "users/list_users.html", context)

