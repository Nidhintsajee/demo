from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,JsonResponse
from serializers import UserProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
	return render(request,'index.html',{})

def signup(request):
	return render(request,'index.html',{})  

def about(request):
	return render(request,'about.html',{})


def signout(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	try:
		if request.method == "POST":
			phone = request.POST.get('phone')
			password = request.POST.get('password')
			user = authenticate(username=phone, password=password)
			print"user",user
			if user:
				user_pro = UserProfile.objects.get(user=user)
				login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				error = " Sorry! Phone Number and Password didn't match, Please try again ! "
				return render(request, 'login.html', {'error': error})
		else:
			return render(request, 'login.html')
	except Exception as e:
		print "error", e
		return HttpResponseRedirect(reverse('home'))

def sign_up(request):
	try:
		if request.method == 'POST':
			name = request.POST.get('name')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			pass_1 = request.POST.get('pass1')
			user_em = User.objects.filter(email=email).exists()
			user_ph = User.objects.filter(username=str(phone)).exists()
			if not user_em and not user_ph:
				user = User.objects.create_user(
					username=phone,
					email=email,
					first_name=name,
					password=pass_1,
				)
				try:
					user_pro = UserProfile(
						user=user,
						email=email,
						phone_no=phone,
					)
					user_pro.save()
				except Exception as e:
					print "error", e
				return render(request, 'login.html', {'phone': phone})
			else:
				error = " Email or Phone-Number already exists "
				return render(request, 'signup.html', {'error': error})
		else:
			return render(request, 'signup.html')
	except Exception as e:
		print"errror",e
		return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def user_details(request):
	try:
		user  = UserProfile.objects.all()
		print "user",user
		serializer = UserProfileSerializer(user, many=True)
	except Exception as e:
		print "error",e
		return JsonResponse({0:e.args[0]})
	return JsonResponse({'data':serializer.data},safe=False)