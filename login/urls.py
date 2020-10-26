from django.urls import path,include
from django.conf.urls import url
from . import views
app_name='login'
#from login import views

urlpatterns = [

    path('',views.login,name='lgn'),
    path('signup/',views.signup,name='account_signup'),
    path('success/',views.success,name='success'),
    path('changepassword/',views.changepassword,name='chp'),
    path('passwordsuccess/',views.passwordsuccess,name='psc'),
    path('logout/',views.logout,name='lgt'),


    #path('',views.login,name='login'),

]