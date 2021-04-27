from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.db import models
# Create your views here.
# from .models import message
from .models import message,friend,img,bio
import datetime


def index(request):
    # user_form = Registration(request.POST)
    return render(request, 'index.html')

def regst(request):
    # user_form = Registration(request.POST)
    # user_form.save()
    ref = request.POST['regst']
    print(ref)
    return render(request, 'index.html')

def home(request):
    user_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    if user_name != '':
        if password !=  '':
            if email != '':
                if User.objects.filter(username=user_name).exists():
                    print('user already exsites')
                else:
                    user = User.objects.create_user(username=user_name, password=password, email=email)
                    user.save()
                    print("user created!")
                    return render(request, 'login.html')
    return render(request, 'index.html')
def vf_login(request):
    img_friend = img.objects.all()
    bio_friend = bio.objects.all()
    if request.method == 'POST':
        username = request.POST['user_login']
        password = request.POST['pass_login']
        friends = []
        if username!='' and password!='':
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                all_mess = message.objects.all()
                username = request.user.username
                imgs = img.objects.all()
                for each in img.objects.all():
                    img_user = each.image
                    user_img = each.userr
                    if img.objects.filter(userr=username).exists():
                        break
                    elif user_img == 'home':
                        imgmain = img(image=img_user,userr=username)
                        imgmain.save()
                for each in friend.objects.all():
                    request_to = each.request_to
                    request_from  = each.requset_frinend
                    accept_friend = each.accepted_friend
                    accept_to = each.accepted_to
                    if request_from == username:
                        if request_to == accept_to :
                            if request_from == accept_friend:
                                friends.append(accept_to)
                    if request_to == username:
                        if request_to == accept_to:
                            if request_from == accept_friend:
                                friends.append(accept_friend)
                                print(len(friends))
                return render(request, 'jame.html',{"username":username,"friends":friends,"friend_img":img_friend,"user_fri":img_friend,"bio":bio_friend})
    return render(request, 'login.html')
def prof(request):
    friends = []
    username = request.user.username
    print("hi venkat")
    for each in friend.objects.all():
        request_to = each.request_to
        request_from  = each.requset_frinend
        accept_friend = each.accepted_friend
        accept_to = each.accepted_to
        if request_from == username or request_to == username:
            if request_to == accept_to:
                if request_from == accept_friend:
                    friends.append(accept_to)
        if request_to == username:
            if request_to == accept_to:
                if request_from == accept_friend:
                    friends.append(accept_friend)
    return render(request, 'jame.html',{"friends":friends})
def back_fun(request):
    friends = []
    bio_friend = bio.objects.all()
    img_friend = img.objects.all()
    username = request.user.username
    for each in friend.objects.all():
        request_to = each.request_to
        request_from  = each.requset_frinend
        accept_friend = each.accepted_friend
        accept_to = each.accepted_to
        if request_from == username:
            if request_to == accept_to :
                if request_from == accept_friend:
                    friends.append(accept_to)
        if request_to == username:
            if request_to == accept_to:
                if request_from == accept_friend:
                    friends.append(accept_friend)
    return render(request, 'jame.html',{"username":username,"friends":friends,"user_fri":img_friend,"friend_img":img_friend,"bio":bio_friend})
def inhome(request):
    # form=inhome_form(request.POST)
    all_src = []
    all_messages = []
    username = request.user.username
    img_friends = img.objects.all()
    bio_friend = bio.objects.all()
    userto = request.GET['name_friend']
    print(userto,"hello")
    all_mess = message.objects.all()

    return render(request, 'index1.html',{"all_mess":all_mess,"usersend":username,"userto":userto,"all_message":all_messages,"friend_img":img_friends,"bio":bio_friend})
def loginpage(request):
    return render(request, 'login.html')

def onhome(request):
    # form = inhome_form(data=request.POST)
    # form.save();
    all_src = []
    all_messages = []
    img_friends = img.objects.all()
    userna = request.POST['textma']
    username = request.user.username
    all_mess = message.objects.all()
    userto = request.POST['userto']
    print(userto)
    if userna != '':
        time = datetime.datetime.now()
        mess = message(textmess=userna,usersend=username,userto=userto,year=time.strftime("%y"),mon=time.strftime("%m"),day=time.strftime("%d"),Hour=time.strftime("%H"),mins=time.strftime("%M"),sec=time.strftime("%S"))
        mess.save()
    return render(request, 'index1.html',{"all_mess":all_mess,"userto":userto,"all_message":all_messages,"friend_img":img_friends})
def requ(request):
    request_arr = []
    fri_imgs = img.objects.all()
    username = request.user.username
    for each in friend.objects.all():
        request_to = each.request_to
        request_from  = each.requset_frinend
        accept_friend = each.accepted_friend
        accept_to = each.accepted_to
        if request_to == username:
            if accept_friend != username:
                if accept_to != username:
                    request_arr.append(request_from)
    return render(request, 'requseted.html',{"req":request_arr,"fri_imgs":fri_imgs})
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def search_code(request):
    search = request.GET['search_box']
    btn_request = 'sendrequest'
    username = request.user.username
    friends = []
    friends_imgs = []
    img_friends = img.objects.all()
    bio_user = bio.objects.all()
    if User.objects.filter(username=search):
        for each in img.objects.all():
            img_user = each.image
            user_img = each.userr
            if user_img == search:
                obj = img_user.instance
            elif user_img == 'home':
                obj = img_user.instance
        if friend.objects.filter(requset_frinend=username,request_to=search,accepted_friend=username,accepted_to=search):
            btn_request = 'Unfriend'
        elif friend.objects.filter(requset_frinend=search,request_to=username,accepted_friend=search,accepted_to=username):
            btn_request = 'Unfriend'
        elif friend.objects.filter(requset_frinend=username,request_to=search):
            btn_request ='Requested'
        elif friend.objects.filter(requset_frinend=search,request_to=username):
            btn_request = 'Accept'
        elif search == username:
            btn_request = 'Your'
        # elif friend.objects.filter(requset_frinend =! username,request_to=!search) and  friend.objects.filter(requset_frinend=!search,request_to=!username):
        #     btn_request = ''
        return render(request, 'search_result.html',{"search":search,"imgs":obj,"btn_request":btn_request})
    else:
        for each in img.objects.all():
            img_user = each.image
            user_img = each.userr
            if user_img == username:
                obj = img_user.instance
            elif user_img == 'home':
                obj = img_user.instance
        for each in friend.objects.all():
                    request_to = each.request_to
                    request_from  = each.requset_frinend
                    accept_friend = each.accepted_friend
                    accept_to = each.accepted_to
                    if request_from == username:
                        if request_to == accept_to :
                            if request_from == accept_friend:
                                friends.append(accept_to)
                    if request_to == username:
                        if request_to == accept_to:
                            if request_from == accept_friend:
                                friends.append(accept_friend)
        for each in img.objects.all():
                    img_user = each.image
                    user_img = each.userr
                    for i in friends:
                        if user_img == i:
                            friends_imgs.append(img_user)
    
    return render(request, 'jame.html',{"username":username,"friends":friends,"imgs":obj,"user_fri":img_friends,"friend_img":img_friends,"bio":bio_user})

def request_button(request):
    search = request.GET['request_button']
    username = request.user.username
    btn_request = 'Sendrequest'
    print(search)
    # for each in friend.objects.all():
    #     request_to = each.request_to
    #     request_user = each.request_from
    #     if request_user == username: 
    #         if request_to != search:
    if User.objects.filter(username=search):
        imgs = img.objects.all()
        for each in img.objects.all():
            img_user = each.image
            user_img = each.userr
            if user_img == search:
                    obj = img_user.instance
            elif user_img == 'home':
                    obj = img_user.instance
       
        if friend.objects.filter(requset_frinend=username,request_to=search,accepted_friend=username,accepted_to=search):
            del_fri = friend.objects.filter(requset_frinend=username,request_to=search,accepted_friend=username,accepted_to=search)
            del_fri.delete()
        elif friend.objects.filter(requset_frinend=search,request_to=username,accepted_friend=search,accepted_to=username):
            del_fri = friend.objects.filter(requset_frinend=search,request_to=username,accepted_friend=search,accepted_to=username)
            del_fri.delete()
        elif friend.objects.filter(requset_frinend=username,request_to=search):
            dell_frih = friend.objects.filter(requset_frinend=username,request_to=search)
            dell_frih.delete()
        elif friend.objects.filter(requset_frinend=search,request_to=username):
            dell_frih = friend.objects.filter(requset_frinend=search,request_to=username)
            dell_frih.delete()
            add__friend = friend(requset_frinend=search,request_to=username,accepted_friend=search,accepted_to=username)
            add__friend.save()
            btn_request = 'Unfriend'
        elif search == username:
            btn_request = 'Your'
        elif btn_request == 'Sendrequest':
            add_friend = friend(requset_frinend=username,request_to=search)
            add_friend.save()
            btn_request = 'Requested'
    print(btn_request)
    return render(request, "search_result.html",{"search":search,"imgs":obj,"btn_request":btn_request})

def accept(request):
    accept = request.GET['acc_name']
    username = request.user.username
    request_arr = []
    fri_imgs = img.objects.all()
    username = request.user.username

    if friend.objects.filter(requset_frinend=accept,request_to=username):
        dell_frih = friend.objects.filter(requset_frinend=accept,request_to=username)
        dell_frih.delete()
        friends = friend(requset_frinend=accept,request_to=username,accepted_friend=accept,accepted_to=username)
        friends.save()
    for each in friend.objects.all():
        request_to = each.request_to
        request_from  = each.requset_frinend
        accept_friend = each.accepted_friend
        accept_to = each.accepted_to
        if request_to == username:
            if accept_friend != username:
                if accept_to != username:
                    request_arr.append(request_from)
    
    return render(request, 'requseted.html',{"req":request_arr,"fri_imgs":fri_imgs})
def imgupload(request):
    username = request.user.username
    img_friend = img.objects.all()
    bio_user = bio.objects.all()
    imgs = img.objects.all()
    if request.FILES['myfile']:
        myfile = request.FILES['myfile']
        friends = []
        friends_imgs = []
        if img.objects.filter(userr=username).exists():
            img1 = img.objects.get(userr=username)
            img1.delete()
            imgmain = img(image=myfile,userr=username)
            imgmain.save()
        else:
            imgmain = img(image=myfile,userr=username)
            imgmain.save()
        
        for each in img.objects.all():
            img_user = each.image
            user_img = each.userr
            if user_img == username:
                obj = img_user.instance
        for each in img.objects.all():
            img_user = each.image
            user_img = each.userr
            for i in friends:
                if user_img == friends[i]:
                    friends_imgs.append(img_user)
                    
        for each in friend.objects.all():
                    request_to = each.request_to
                    request_from  = each.requset_frinend
                    accept_friend = each.accepted_friend
                    accept_to = each.accepted_to
                    if request_from == username:
                        if request_to == accept_to :
                            if request_from == accept_friend:
                                friends.append(accept_to)
                    if request_to == username:
                        if request_to == accept_to:
                            if request_from == accept_friend:
                                friends.append(accept_friend)

        return render(request, 'jame.html',{"username":username,"friends":friends,"user_fri":img_friend,"imgs":obj,"friend_img":img_friend,"bio":bio_user})
def bioon(request):
    return render(request,"bio.html")
def bioinput(request):
    bioinput = request.GET['Bio_input']
    username = request.user.username
    bio_user = bio.objects.all()
    img_friend = img.objects.all()
    if bioinput != '':
        if bio.objects.filter(userr2=username).exists():
            bio1 = bio.objects.get(userr2=username)
            bio1.delete()
            biocha = bio(bio=bioinput,userr2=username)
            biocha.save()
        else:
            biocha = bio(bio=bioinput,userr2=username)
            biocha.save()
        friends = []
        
        for each in friend.objects.all():
            request_to = each.request_to
            request_from  = each.requset_frinend
            accept_friend = each.accepted_friend
            accept_to = each.accepted_to
            if request_from == username:
                if request_to == accept_to :
                    if request_from == accept_friend:
                        friends.append(accept_to)
            if request_to == username:
                if request_to == accept_to:
                    if request_from == accept_friend:
                        friends.append(accept_friend)
                      
        return render(request, 'jame.html',{"username":username,"friends":friends,"user_fri":img_friend,"friend_img":img_friend,"bio":bio_user})
    else:
        return render(request,"bio.html")
