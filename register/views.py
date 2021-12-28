from django.shortcuts import render
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone

# Create your views here.
def homepage(request):
	return render(request,'index.html')

def aboutpage(request):
	return render(request,'about.html')

def Login_admin(request):
	
	return render(request,'adminlogin.html',)

def loginpage(request):
	
	return render(request,'login.html')

def createaccountpage(request):
	error = ""
	user="none"
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']
		try:
			if password == repeatpassword:
				Patient.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				pat_group = Group.objects.get(name='Patient')
				pat_group.user_set.add(user)
				#print(pat_group)
				user.save()
				#print(user)
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print("Error:",e)
	d = {'error' : error}
	#print(error)
	return render(request,'createaccount.html',d)
	#return render(request,'createaccount.html')