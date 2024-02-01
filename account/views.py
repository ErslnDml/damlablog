from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def login_blog(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    
    if request.method == 'POST':
        username = request.POST["username"]
        userpassword = request.POST["userpassword"]
        user = authenticate(request, username = username, password = userpassword)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request,'account/login.html',{"error" : "Girdiğiniz bilgilerde kullanıcı bulunamadı."})
        
    return render (request,'account/login.html')

def register_blog(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['useremail']
        password = request.POST['userpassword']
        passwordagain = request.POST['passwordagain']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if password == passwordagain:
            if User.objects.filter(username = username).exists():
                return render(request,'account/register.html',{"error" : 'Girdiğiniz bilgilerde kullanıcı adı kullanılmaktadır.'})
            else :
                if User.objects.filter(email = email).exists():
                    return render(request,'account/register.html',{"error" : 'Girdiğiniz bilgilerde email adresi kullanılmaktadır.'})
                else:
                    user=User.objects.create_user(username=username, email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request,'account/register.html',{
                "error":"Girdiğiniz şifreler uyuşmuyor. "
            })
    return render (request,'account/register.html')

def logout_blog(request):
    logout(request)
    return redirect ('homepage')