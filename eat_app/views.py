from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import os
import math
from django.core.mail import send_mail
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request,'index.html')

def online(request):
    return render(request,'online.html')

def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:

                    return redirect(adminbutton)
            else:
                return HttpResponse("failed")

    return render(request,'adminlogin.html')

def adminbutton(request):
    return render(request,'adminbutton.html')

 # choice to select bf rice
def uploadchoice(request):
    return render(request,'uploadchoice.html')

# Special Dish
def adminupload(request):
    if request.method=='POST':
        a=profilform(request.POST,request.FILES)
        if a.is_valid():
            dn=a.cleaned_data['dishname']
            p=a.cleaned_data['price']
            de=a.cleaned_data['description']
            card=a.cleaned_data['card']
            b=profilmodel(dishname=dn,price=p,description=de,card=card)
            b.save()
            return redirect(admindisplay)
        else:
            return HttpResponse("file upload failed")
    return render(request,'adminupload.html')

#adminpage display

def admindisplay(request):
    try:
        a = profilmodel.objects.all()
        idd = []
        dishname = []
        price = []
        description = []
        img = []
        for i in a:
            id = i.id
            idd.append(id)
            nm = i.dishname
            dishname.append(nm)
            pr = i.price
            price.append(pr)
            dec = i.description
            description.append(dec)
            im = str(i.card).split('/')[-1]
            img.append(im)
        pair = zip(dishname, price, description, img, idd)
        return render(request, 'profile.html', {'a': pair})
    except:
        return redirect(adminlogin)

def editadmin(request,id):
    a=profilmodel.objects.get(id=id)
    img = str(a.card).split('/')[-1]
    if request.method == 'POST':
        a.dishname = request.POST.get('dishname')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        if len(request.FILES)!=0:
            if len(a.card)>0:
                os.remove(a.card.path)
            a.card = request.FILES['card']
        a.save()
        return redirect(admindisplay)

    return render(request,'adminedit.html',{'a':a,'img':img})

def deletecard(request,id):
    a=profilmodel.objects.get(id=id)
    a.delete()
    return redirect(admindisplay)
# ##########################################

# Breakfast
def bfupload(request):
    if request.method=='POST':
        a=bfform(request.POST,request.FILES)
        if a.is_valid():
            bfn=a.cleaned_data['bfname']
            pr=a.cleaned_data['price']
            de=a.cleaned_data['description']
            card=a.cleaned_data['img']
            b=bfmodel(bfname=bfn,price=pr,description=de,img=card)
            b.save()
            return redirect(admindisplay)
        else:
            return HttpResponse("file upload failed")
    return render(request,'bfupload.html')

def bfdisplay(request):
    a=bfmodel.objects.all()
    idd=[]
    bfname=[]
    price=[]
    description=[]
    img=[]
    for i in a:
        id = i.id
        idd.append(id)
        nm=i.bfname
        bfname.append(nm)
        pr=i.price
        price.append(pr)
        de=i.description
        description.append(de)
        im=str(i.img).split('/')[-1]
        img.append(im)
    pair=zip(bfname,price,description,img,idd)
    return render(request,'bfdisplay.html',{'a':pair})

def editbf(request,id):
    a=bfmodel.objects.get(id=id)
    im = str(a.img).split('/')[-1]
    if request.method == 'POST':
        a.bfname = request.POST.get('bfname')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        if len(request.FILES)!=0:
            if len(a.img)>0:
                os.remove(a.img.path)
            a.img = request.FILES['img']
        a.save()
        return redirect(admindisplay)

    return render(request,'adminedit.html',{'a':a,'img':im})

def deletebf(request,id):
    a=bfmodel.objects.get(id=id)
    # os.remove(str(a.card))
    a.delete()
    return redirect(bfdisplay)
########################################

# Rice Briyani
def riceupload(request):
    if request.method=='POST':
        a=riceform(request.POST,request.FILES)
        if a.is_valid():
            gn=a.cleaned_data['ricename']
            pr=a.cleaned_data['price']
            de=a.cleaned_data['description']
            card=a.cleaned_data['img']
            b=rice(ricename=gn,price=pr,description=de,img=card)
            b.save()
            return redirect(admindisplay)
        else:
            return HttpResponse("file upload failed")
    return render(request,'riceupload.html')

def ricedisplay(request):
    a = rice.objects.all()
    idd = []
    ricename = []
    price = []
    description = []
    img = []
    for i in a:
        id = i.id
        idd.append(id)
        nm = i.ricename
        ricename.append(nm)
        pr = i.price
        price.append(pr)
        de = i.description
        description.append(de)
        im = str(i.img).split('/')[-1]
        img.append(im)
    pair = zip(ricename, price, description, img, idd)
    return render(request, 'ricedisplay.html', {'a': pair})


def editrice(request,id):
    a=rice.objects.get(id=id)
    im = str(a.img).split('/')[-1]
    if request.method == 'POST':
        a.dishname = request.POST.get('ricename')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        if len(request.FILES)!=0:
            if len(a.img)>0:
                os.remove(a.img.path)
            a.img = request.FILES['img']
        a.save()
        return redirect(admindisplay)

    return render(request,'adminedit.html',{'a':a,'img':im})

def deleterice(request,id):
    a=rice.objects.get(id=id)
    # os.remove(str(a.card))
    a.delete()
    return redirect(ricedisplay)

# ################################

# Gravy
def graupload(request):
    if request.method=='POST':
        a=gravyform(request.POST,request.FILES)
        if a.is_valid():
            gn=a.cleaned_data['gravyname']
            pr=a.cleaned_data['pri']
            de=a.cleaned_data['des']
            card=a.cleaned_data['im']
            b=grav(gravyname=gn,pri=pr,des=de,im=card)
            b.save()
            return redirect(admindisplay)
        else:
            return HttpResponse("file upload failed")
    return render(request,'sampleupload.html')

def sdisplay(request):
    a=grav.objects.all()
    idd=[]
    gravyname=[]
    pri=[]
    des=[]
    im=[]
    for i in a:
        id = i.id
        idd.append(id)
        nm=i.gravyname
        gravyname.append(nm)
        pr=i.pri
        pri.append(pr)
        de=i.des
        des.append(de)
        img=str(i.im).split('/')[-1]
        im.append(img)
    pair=zip(gravyname,pri,des,im,idd)
    return render(request,'sdisplay.html',{'a':pair})

def editgrav(request,id):
    a = grav.objects.get(id=id)
    img = str(a.im).split('/')[-1]
    if request.method == 'POST':
        a.gravyname = request.POST.get('gravyname')
        a.pri = request.POST.get('pri')
        a.des = request.POST.get('des')
        if len(request.FILES) != 0:
            if len(a.im) > 0:
                os.remove(a.im.path)
            a.im = request.FILES['im']
        a.save()
        return redirect(adminfinal)
    return render(request, 'editgravy.html', {'a': a, 'im': img})

def deletegrav(request,id):
    a=grav.objects.get(id=id)
    a.delete()
    return redirect(admindisplay)
# ################################

# Drink
def iceupload(request):
    if request.method=='POST':
        a=iceform(request.POST,request.FILES)
        if a.is_valid():
            gn=a.cleaned_data['name']
            pr=a.cleaned_data['price']
            de=a.cleaned_data['description']
            card=a.cleaned_data['img']
            b=icemodel(name=gn,price=pr,description=de,img=card)
            b.save()
            return redirect(admindisplay)
        else:
            return HttpResponse("file upload failed")
    return render(request,'iceupload.html')

def icedisplay(request):
    a=icemodel.objects.all()
    idd=[]
    name=[]
    price=[]
    description=[]
    img=[]
    for i in a:
        id = i.id
        idd.append(id)
        nm=i.name
        name.append(nm)
        pr=i.price
        price.append(pr)
        de=i.description
        description.append(de)
        im=str(i.img).split('/')[-1]
        img.append(im)
    pair=zip(name,price,description,img,idd)
    return render(request,'icedisplay.html',{'a':pair})

def editice(request,id):
    a = icemodel.objects.get(id=id)
    im = str(a.img).split('/')[-1]
    if request.method == 'POST':
        a.name = request.POST.get('name')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        if len(request.FILES) != 0:
            if len(a.img) > 0:
                os.remove(a.img.path)
            a.img = request.FILES['img']
        a.save()
        return redirect(admindisplay)
    return render(request, 'editice.html', {'a': a, 'img': im})

def deleteice(request,id):
    a=icemodel.objects.get(id=id)
    # os.remove(str(a.card))
    a.delete()
    return redirect(icedisplay)


#admin view user order
def orderhistory(request):
    a=cartmodel.objects.all()
    dishname = []
    price = []
    img = []

    for i in a:
        nm = i.dishname
        dishname.append(nm)
        pr = i.price
        price.append(pr)
        im = str(i.card).split('/')[-1]
        img.append(im)

    pair = zip(dishname, img, price)
    return render(request,'orderhistory.html',{'a':pair})


###########User Page######

def register(request):
    if request.method == 'POST':
        a=regiform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['name']
            ph=a.cleaned_data['phone']
            request.session['ph']=ph
            em=a.cleaned_data['email']
            ps=a.cleaned_data['psw']
            cps=a.cleaned_data['cpsw']
            if ps==cps:
                b= regimodel(name=nm,phone=ph,email=em,psw=ps)
                b.save()
                subject = "your account has been created"
                message = f"your new account number is {ph}"
                email_from = "priyaluminar@gmail.com"
                email_to = em
                send_mail(subject, message, email_from, [email_to])
                return redirect(regsuccess)
            else:
                return HttpResponse("password dosn't match")
        else:
            return HttpResponse("registration failed")

    return render(request,'register.html')

def regsuccess(request):
    return render(request,'registrationsuccess.html')
#user login
def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            ps=a.cleaned_data['password']
            b=regimodel.objects.all()
            for i in b:
                if i.name==nm and i.psw==ps:
                    return redirect(userdisplay)
            else:
                return HttpResponse("login failed")
    return render(request,'login.html')


def forgetpsw(request):
    a=regimodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        for i in a:
            if(i.email==em and i.phone==int(ph)):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/eat_app/changepsw/{id}"
                frm="priyaluminar@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check email")
        else:
            return HttpResponse("SORRY")
    return render(request,'forgotpsw.html')


def changepsw(request,id):
    a=regimodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('re-pin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse("password changed successfully")
        else:
            return HttpResponse("SORRY")
    return render(request,'changepsw.html')


def userdisplay(request):
        try:
            a = profilmodel.objects.all()
            idd = []
            dishname = []
            price = []
            description = []
            img = []
            for i in a:
                id = i.id
                idd.append(id)
                nm = i.dishname
                dishname.append(nm)
                pr = i.price
                price.append(pr)
                dec = i.description
                description.append(dec)
                im = str(i.card).split('/')[-1]
                img.append(im)
            pair = zip(dishname, price, description, img, idd)
            return render(request, 'userdisplay.html', {'a': pair})
        except:
            return redirect(login)

#DetailView of a particular dish
def dishview(request,id):
    a=profilmodel.objects.get(id=id)
    img = str(a.card).split('/')[-1]
    if request.method == 'POST':
        a.dishname = request.POST.get('dishname')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        a.id = request.POST.get('id')
        # return redirect(cart)
    return render(request,'dishview.html',{'a':a,'img':img})


#add to cart
def add_cart(request,id):
    a=profilmodel.objects.get(id=id)
    b=cartmodel.objects.all()
    for i in b :
        if a.id==i.pro_id:
            return HttpResponse("item already in cart")
    c=cartmodel(pro_id=a.id,dishname=a.dishname,price=a.price,card=a.card)
    c.save()
    return render(request,'addcartdisplay.html',{'a':a,'b':b,'c':c})

#cart display
def show_cart(request):
    a=cartmodel.objects.all()
    dishname = []
    price = []
    img = []
    idd = []
    for i in a:
        nm = i.dishname
        dishname.append(nm)
        pr = i.price
        price.append(pr)
        im = str(i.card).split('/')[-1]
        img.append(im)
        id = i.id
        idd.append(id)
    pair = zip(dishname, img, price, idd)
    return render(request,'cart.html',{'a':pair})

def deletecart(request,id):
    a=cartmodel.objects.get(id=id)
    # os.remove(str(a.card))
    a.delete()
    return redirect(show_cart)

#user details for payment
def adddetails(request):
    a=adddetailsmodel.objects.all()
    return render(request,'adddetails.html',{'a':a})

def payment(request):
    a=paymentmodel.objects.all()
    return render(request,'payment.html',{'a':a})

def userprofile(request):
    a=cartmodel.objects.all()
    return render(request,'payconfirm.html',{'a':a})

def bill(request):
     a=cartmodel.objects.all()
     b=regimodel.objects.all()
     return render(request,'paymentbill.html',{'a':a,'b':b})

def ordersuccess(request):
    return render(request,'ordersuccess.html')

def logoutview(request):
    logout(request)
    return redirect(login)

#####################




















































def adminfinal(request):
        a = profilmodel.objects.all()
        idd = []
        dishname = []
        price = []
        description = []
        img = []
        for i in a:
            id = i.id
            idd.append(id)
            nm = i.dishname
            dishname.append(nm)
            pr = i.price
            price.append(pr)
            dec = i.description
            description.append(dec)
            im = str(i.card).split('/')[-1]
            img.append(im)
        pair = zip(dishname, price, description, img, idd)
        c = bfmodel.objects.all()
        idd = []
        bfname = []
        price = []
        description = []
        img = []
        for i in c:
            id = i.id
            idd.append(id)
            nm = i.bfname
            bfname.append(nm)
            pr = i.price
            price.append(pr)
            de = i.description
            description.append(de)
            im = str(i.img).split('/')[-1]
            img.append(im)
        pa = zip(bfname, price, description, img, idd)
        d = rice.objects.all()
        idd = []
        ricename = []
        price = []
        description = []
        img = []
        for i in d:
            id = i.id
            idd.append(id)
            nm = i.ricename
            ricename.append(nm)
            pr = i.price
            price.append(pr)
            de = i.description
            description.append(de)
            im = str(i.img).split('/')[-1]
            img.append(im)
        p = zip(ricename, price, description, img, idd)
        b = grav.objects.all()
        idd = []
        gravyname = []
        pri = []
        des = []
        im = []
        for i in b:
            id = i.id
            idd.append(id)
            nm = i.gravyname
            gravyname.append(nm)
            pr = i.pri
            pri.append(pr)
            de = i.des
            des.append(de)
            img = str(i.im).split('/')[-1]
            im.append(img)
        pai = zip(gravyname, pri, des, im, idd)
        e = icemodel.objects.all()
        idd = []
        name = []
        price = []
        description = []
        img = []
        for i in e:
            id = i.id
            idd.append(id)
            nm = i.name
            name.append(nm)
            pr = i.price
            price.append(pr)
            de = i.description
            description.append(de)
            im = str(i.img).split('/')[-1]
            img.append(im)
        pairr = zip(name, price, description, img, idd)
        return render(request, 'adminfinaldisplay.html', {'a': pair, 'c': pa, 'd': p, 'b': pai, 'e': pairr})


















































