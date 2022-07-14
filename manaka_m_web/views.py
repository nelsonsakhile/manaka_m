from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	queryset = ClintsRegister.objects.all()
	form = ClintsRegisterForm(request.POST or None)
	title = 'Nothing'
	total_clients =  ClintsRegister.objects.count()

	context = {
	'title': title,
	'queryset': queryset,
	'form': form,
	'total_clients': total_clients,
	}
	return render(request, "index.html", context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')