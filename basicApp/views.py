from django.shortcuts import render
from basicApp.forms import Userform
from .forms import UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = Userform(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user = user_form.save()

            up = profile_form.save(commit=False)
            up.user = user
            up.save()
            registered = True
    else:
        user_form = Userform()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html', {
        'userform': user_form,
        'profileform': profile_form,
        'registered': registered,
    })

def user_login(request):
    if request.method == 'POST':
        Uname = request.POST.get('username')
        pwd = request.POST.get('password')
      
        user = authenticate(username = Uname ,password = pwd)

        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            return HttpResponse('invalid user')
    else:

        return render(request,'login.html')