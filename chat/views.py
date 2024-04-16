from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import EditProfileForm,RegistrationForm,LogInForm,ProfileForm
from django.db.models import Q
# Create your views here.




def register(request):
    fm = RegistrationForm()
    if request.method=='POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('log-in')
       
        
    return render(request,'signup.html',context={'form':fm})







@login_required
def create_profile(request):
    user = request.user
    username = User.objects.get(id=request.user.id)
    print(username)
    if request.method=='POST':
        user = username
        bio = request.POST.get('bio')
        pic = request.FILES.get('profile_pic')
        user_profile = Profile.objects.update_or_create(username=username,bio=bio,profile_picture=pic)
        return redirect('home')



    return render(request,'profile.html',{'username':username})

def show_all_profiles(request):
    profiles = Profile.objects.all()
   
    
        
    return render(request,'all_profiles.html',{'profiles':profiles})






    
    

@login_required
def send_message(request,profile_id):
    user = User.objects.get(id=request.user.id)
    send_to = User.objects.get(id=profile_id)
    try:
        con = Thread.objects.create(first_person=user,second_person=send_to)
    except Exception as e:
        print(e)
    return redirect('home')       

@login_required
def logout_user(request):
   
    logout(request)
    return redirect('log-in')
        

@login_required
def message_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    query = request.GET.get('search-user')
    
    return render(request,'messages.html',{'threads':threads,})