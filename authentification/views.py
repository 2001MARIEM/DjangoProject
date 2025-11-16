from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from functools import wraps
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'authentification/register.html')

        # vérifier si user existe
        if User.objects(username=username).first():
            messages.error(request, "Nom d'utilisateur déjà utilisé.")
            return render(request, 'authentification/register.html')

        # Créer user
        User(username=username, password=make_password(password)).save()
        messages.success(request, "Compte créé ! Vous pouvez maintenant vous connecter.")
        return redirect('login')

    return render(request, 'authentification/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects(username=username).first()

        if user and check_password(password, user.password):
            # enregistrer la session Django
            request.session['user_id'] = str(user.id)
            request.session['username'] = user.username
            return redirect('dashboard')

        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        return render(request, 'authentification/login.html')

    return render(request, 'authentification/login.html')


def login_required_custom(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper


def logout_view(request):
    request.session.flush()
    return redirect('login')
