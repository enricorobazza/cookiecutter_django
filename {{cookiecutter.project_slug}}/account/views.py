from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.views import (
    PasswordResetConfirmView as DjangoPasswordResetConfirmView,
    PasswordResetView as DjangoPasswordResetView
)
from django.contrib.auth.forms import (
    SetPasswordForm as DjangoSetPasswordForm,
    PasswordResetForm as DjangoPasswordResetForm
)
from account.forms import UserLoginForm, UserCreationForm

class PasswordResetForm(DjangoPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PasswordResetView(DjangoPasswordResetView):
    form_class = PasswordResetForm

class SetPasswordForm(DjangoSetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields["new_password2"].attrs['class'] += ' mt-2'
        self.fields["new_password1"].label = 'Senha'
        self.fields["new_password2"].level = 'Confirmar Senha'

class PasswordResetConfirmView(DjangoPasswordResetConfirmView):
    form_class = SetPasswordForm

class AuthView:
    def login(request):
        _next = request.GET.get('next')
        if(request.user.is_authenticated):
            return redirect(_next or '/')

        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect(_next or '/')

        return render(request, 'account/login.html', {'form': form})

    def logout(request):
        auth_logout(request)
        return redirect('/')

    def signup(request):
        if request.method == 'POST':
            data = request.POST.copy()
            form = UserCreationForm(data)
            if form.is_valid():
                user = form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                auth_login(request, user)
                return redirect('/')
        else:
            form = UserCreationForm()
        return render(request, 'account/signup.html', {'form': form})
