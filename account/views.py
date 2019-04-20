from django.shortcuts import render,redirect
from account.forms import (
    userregister,
    updateprofile,
    updateuser
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'account/home.html')

def trial(request):
    return render(request, 'account/trial.html')    

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = updateuser(request.POST, instance=request.user)
        p_form = updateprofile(request.POST,request.FILES,
                            instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('Home')

    else:
        u_form = updateuser(instance=request.user)
        p_form = updateprofile(instance=request.user.profile)
        
        context = {
            'u_form': u_form,
            'p_form': p_form   
        }
    return render(request, 'account/profile.html', context)
    

def register(request):
    if request.method == 'POST':
        form = userregister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} ')
            return redirect('Home')
    else:
        form = userregister()  
    return render(request, 'account/register.html', {'form': form})