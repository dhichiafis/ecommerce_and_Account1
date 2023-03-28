from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from django.contrib import messages
'''
@login_required()
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})

'''

def user_registration(request):
    if request.method=='POST':
        user=UserRegistrationForm(request.POST)
        if user.is_valid():
            new_user=user.save(commit=False)
            new_user.set_password(user.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request,'you have been successfully registerd')
            return redirect('account:homepage')
    else:
        user=UserRegistrationForm()


    context={'user':user}
    return render(request,'account/user_register.html',
                  context)

@login_required()
def homepage(request):
    return render(request,'account/homepage.html')
