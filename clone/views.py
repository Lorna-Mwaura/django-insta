from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('welcome.html') # Redirect user to Homepage
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})