from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
        'page': 'signup',
})
