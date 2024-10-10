from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm,OtpForm,CustomAuthenticationForm,EditProfilePageForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login
#from django.contrib import messages
from .models import OTP
from .utils import generate_otp
from django.contrib.auth import get_user_model
from myblog.models import Profile,Post
from django.contrib.auth.views import LoginView

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            request.session['user_form_data'] = form.cleaned_data
            generate_otp(email)
            #messages.success(request, 'OTP sent to your email.')
            return redirect('verify_otp', email=email)
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def verify_otp(request, email):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            otp_record = OTP.objects.filter(email=email, otp=otp).first()
            if otp_record and otp_record.is_valid():
                user_form = SignUpForm(request.session['user_form_data'])
                if user_form.is_valid():
                    user = user_form.save()
                    login(request, user)
                    #messages.success(request, 'Registration successful and you are now logged in.')
                    return redirect('create_profile_page')
            else:
                pass
                #messages.error(request, 'Invalid OTP or OTP expired.')
    else:
        form = OtpForm(initial={'email': email})
    return render(request, 'verify_otp.html', {'form': form, 'email': email})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def set_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user
        user.set_password(password)
        user.save()
        #messages.success(request, 'Password set successfully! You are now logged in.')
        return redirect('some_protected_view')
    return render(request, 'set_password.html')

class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfileView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        posts = Post.objects.filter(author=page_user.user.id).values().order_by('-post_date')
        #print(posts)
        context['page_user'] = page_user
        context['posts'] = posts
        return context

def ShowProfile(request):
    if request.user.is_authenticated :
        return redirect('profile',request.user.profile.id)
    else:
        return render(request,'registration/no_profile.html',{})
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    #success_url = reverse_lazy('home')

def password_success(request):
    return render(request,'registration/password_success.html',{})

class EditProfileView(generic.UpdateView):
    model = Profile
    form_class=EditProfilePageForm
    template_name = "registration/edit_profile_page.html"
    #fields = ['profile_pic','bio','web_url','facebook_url','instagram_url','twitter_url','github_url']
    success_url = reverse_lazy('home')

class CreateProfileView(generic.CreateView):
    model = Profile
    form_class=ProfilePageForm
    template_name = "registration/create_user_profile.html"
    #fields = "__all__"
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
