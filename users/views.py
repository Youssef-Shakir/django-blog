from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	form = UserRegisterForm()
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}')
			form.save()
			return redirect('blog_app:home')
	context = {'form':form}
	return render(request,'users/register.html',context)

@login_required
def profile(request):
	return render(request,'users/profile.html')