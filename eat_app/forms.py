from django import forms


class regiform(forms.Form):
    name=forms.CharField(max_length=50)
    phone=forms.IntegerField()
    email=forms.EmailField()
    psw=forms.CharField(max_length=20)
    cpsw=forms.CharField(max_length=20)

class loginform(forms.Form):
    name=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class profilform(forms.Form):
    dishname = forms.CharField(max_length=30)
    price = forms.IntegerField()
    description = forms.CharField(max_length=50)
    card = forms.FileField()

class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class adddetailsform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.ImageField()
    address=forms.CharField(max_length=50)

class paymentform(forms.Form):
    num=forms.IntegerField()
    expir=forms.IntegerField()
    cvv=forms.IntegerField()
    name=forms.CharField(max_length=40)

class gravyform(forms.Form):
    gravyname = forms.CharField(max_length=30)
    pri = forms.IntegerField()
    des = forms.CharField(max_length=50)
    im = forms.FileField()

class riceform(forms.Form):
    ricename = forms.CharField(max_length=30)
    price = forms.IntegerField()
    description = forms.CharField(max_length=50)
    img = forms.FileField()


class bfform(forms.Form):
    bfname = forms.CharField(max_length=30)
    price = forms.IntegerField()
    description = forms.CharField(max_length=50)
    img = forms.FileField()

class iceform(forms.Form):
    name = forms.CharField(max_length=30)
    price = forms.IntegerField()
    description = forms.CharField(max_length=50)
    img = forms.FileField()






























































