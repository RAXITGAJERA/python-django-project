import email
import imp
from django.shortcuts import  render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()
from . models import video as myvideo
from . models import videocommets as myvideocommets
from . models import signup as mysignup


# Create your views here.

def home(request):
    sel = myvideo.objects.all()
    return render(request, 'usersite/home.html',{'sel':sel})


def edituser(request,id):
    sel=get_object_or_404(mysignup,id=id)
    return render(request,'usersite/edituser.html',{'sel':sel})

def updateuser(request):
    id = request.POST['userid']
    obj = get_object_or_404(mysignup,id=id)
    obj.email = request.POST['email']
    obj.is_staff = request.POST['is_staff']
    obj.user_fullname = request.POST['user_fullname']
    obj.user_address = request.POST['user_address']
    obj.user_gender = request.POST['user_gender']
    obj.user_country = request.POST['user_country']
    obj.user_city = request.POST['user_city']
    obj.save()
    return redirect('homepage')

def homeadmin(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel = myvideo.objects.all()
    return render(request,'admin/homeadmin.html',{'sel':sel})

def addvideo(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    if request.method == 'POST':
        obj = myvideo()
        obj.Video_name = request.POST['Video_name']
        obj.channel = request.POST['channel']
        obj.Video_link = request.POST['Video_link']
        obj.Country = request.POST['Country']
        obj.City = request.POST['City']
        obj.save()
        return redirect('homeadminpage')
    else:
        return render(request,'admin/addvideo.html')

def editvideo(request,id):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel=get_object_or_404(myvideo,id=id)
    return render(request,'admin/editvideoadmin.html',{'sel':sel})

def updatevideo(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    id = request.POST['Video_id']
    obj = get_object_or_404(myvideo,id=id)
    obj.Video_name = request.POST['Video_name']
    obj.channel = request.POST['channel']
    obj.Video_link = request.POST['Video_link']
    obj.Country = request.POST['Country']
    obj.City = request.POST['City']
    obj.save()
    return redirect('homeadminpage')

def deletevideo(request,id):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel=get_object_or_404(myvideo,id=id)
    sel.delete()
    return redirect('homeadminpage')


def addcoments(request,id):
    sel=get_object_or_404(myvideo,id=id)
    comments=myvideocommets.objects.filter(post_id=id)
    return render(request,'admin/addcoments.html',{'sel':sel, 'comments':comments})

def videocomments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postVideo_id = request.POST.get('postVideo_id')
        post = myvideo.objects.get(id=postVideo_id)

        comment = myvideocommets(comment=comment, user=user, post=post)
        comment.save()
    return redirect('homepage')

def showcomments(request,id):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel=get_object_or_404(myvideo,id=id)
    comments=myvideocommets.objects.filter(post_id=id)
    return render(request,'admin/showcoments.html',{'sel':sel, 'comments':comments})

def homeuseradmin(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel = mysignup.objects.filter(is_superuser=False).values()
    return render(request,'admin/homeuseradmin.html',{'sel':sel})

def edituseradmin(request,id):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel=get_object_or_404(mysignup,id=id)
    return render(request,'admin/edituseradmin.html',{'sel':sel})

def updateuseradmin(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    id = request.POST['userid']
    obj = get_object_or_404(mysignup,id=id)
    obj.email = request.POST['email']
    obj.is_staff = request.POST['is_staff']
    obj.user_fullname = request.POST['user_fullname']
    obj.user_address = request.POST['user_address']
    obj.user_gender = request.POST['user_gender']
    obj.user_country = request.POST['user_country']
    obj.user_city = request.POST['user_city']
    obj.block_unblock = request.POST['block_unblock']
    obj.save()
    return redirect('homeuseradminpage')

def deleteuseradmin(request,id):
    if not request.user.is_superuser:
        return redirect('homepage')
    sel=get_object_or_404(mysignup,id=id)
    sel.delete()
    return redirect('homeuseradminpage')

def adduserbyadmin(request):
    if not request.user.is_superuser:
        return redirect('homepage')
    if request.method == 'POST':
        obj = mysignup()
        obj.email = request.POST['email']
        obj.is_staff = request.POST['is_staff']
        obj.user_fullname = request.POST['user_fullname']
        obj.user_address = request.POST['user_address']
        obj.user_gender = request.POST['user_gender']
        obj.user_country = request.POST['user_country']
        obj.user_city = request.POST['user_city']
        obj.save()
        return redirect('homeuseradminpage')
    else:
        return render(request,'admin/adduserbyadmin.html')

def signupuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_fullname = request.POST['user_fullname']
        user_address = request.POST['user_address']
        user_gender = request.POST['user_gender']
        user_country = request.POST['user_country']
        user_city = request.POST['user_city']

        myuser = User.objects.create_user( email, password)
        myuser.user_fullname = user_fullname
        myuser.user_address = user_address
        myuser.user_gender = user_gender
        myuser.user_country = user_country
        myuser.user_city = user_city
        myuser.save()
        msg="Your account has been successfully created"
        return render(request,'registration/signup.html',{'msg':msg})
        
    return render(request, 'registration/signup.html')


def loginuser(request):
    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(email=loginemail,password=loginpassword)
        check = user.is_superuser 
        if check==False:
            if user.block_unblock == 'block':
                msg="Sorry! Admin block you"
                return render(request,'registration/siginuser.html',{'msg':msg})
            else:
                if user is not None:
                    login(request, user) 
                    return redirect('homepage')
                else:
                    msg="Invalid detail, Please try again"
                    return render(request,'registration/siginuser.html',{'msg':msg})
        else:
            msg="Admin not login in user site"
            return render(request,'registration/siginuser.html',{'msg':msg})
    else:
        return render(request, 'registration/siginuser.html')

def loginadmin(request):
    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(email=loginemail,password=loginpassword)
        check = user.is_superuser
        if check==True:
            if user is not None:
                login(request, user) 
                return redirect('homeadminpage')
            else:
                msg="Invalid detail, Please try again"
                return render(request,'registration/adminlogin.html',{'msg':msg})
        else:
            msg="User not login in Admin site"
            return render(request,'registration/adminlogin.html',{'msg':msg})
    else:
        return render(request, 'registration/adminlogin.html')

def logoutuser(request):
    logout(request)
    return redirect('homepage')