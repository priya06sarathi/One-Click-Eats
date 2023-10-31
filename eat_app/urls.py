from django.urls import path
from.views import *
urlpatterns=[
    path('index/',index),
    path('onlineservice/',online),
    path('adminlogin/',adminlogin),
    path('adminupload/',adminbutton),
    path('uploadchoice/',uploadchoice),

    path('dishupload/',adminupload),
    path('profile/',admindisplay),
    path('editadmindishes/<int:id>', editadmin),
    path('deletedishes/<int:id>', deletecard),

    path('bfupload/',bfupload),
    path('bfdisplay/',bfdisplay),
    path('deletebf/<int:id>',deletebf),
    path('editbf/<int:id>',editbf),

    path('graupload/',graupload),
    path('sdisplay/',sdisplay),
    path('editgrav/<int:id>',editgrav),
    path('deletegrav/<int:id>',deletegrav),

    path('riceupload/',riceupload),
    path('ricedisplay/',ricedisplay),
    path('deleterice/<int:id>',deleterice),
    path('editrice/<int:id>',editrice),

    path('iceupload/', iceupload),
    path('icedisplay/', icedisplay),
    path('editice/<int:id>',editice),
    path('deleteice/<int:id>', deleteice),

    path('orderhistory/',orderhistory),


    path('register/',register),
    path('registersuccess/',regsuccess),
    path('login/',login),
    path('forgetpsw/',forgetpsw),
    path('changepsw/<int:id>',changepsw),


    path('userdisplay/',userdisplay),
    path('dishview/<int:id>',dishview),

    path('addcart/<int:id>',add_cart),
    path('showcart/',show_cart),
    path('deletecart/<int:id>',deletecart),

    path('adddetails/',adddetails),

    path('payment/',payment),
    path('paymentbill/',bill),
    path('ordersuccess/',ordersuccess),
    path('payconfirm/',userprofile),
    path('logout/',logoutview),



    path('adminfinal/',adminfinal),















]