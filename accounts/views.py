# Reverse allows us to pass the name of a URLs instead of a name of a view
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    return render(request, "index.html")


# A decorator that we can put on top of our function signature to check if the
# user is logged in before executing any more of the code 
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    # Don't want to display the login page to users that are logged in.
    # Without this if statement in, we could access the login page by entering
    # the URL into the URL bar.
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        # We're going to pass in the request post as our other constructor
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        # Create an instance of the login form
        login_form = UserLoginForm()

    # Pass that form to the template. We'll give our context dictionary and
    # that should be a string so the key is login form and the value is the
    # name of the form instance that we just created 
    return render(request, "login.html", {'login_form': login_form})


def registration(request):
    return render(request, "register.html")