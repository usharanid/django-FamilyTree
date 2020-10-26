from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [


    path('add/',views.add,name='add'),
    path('mail/',views.mail,name='mail'),
    path('addsuccess/',views.addsuccess,name='addsuccess'),
    path('search/', views.search, name='search'),
    path(r'^search1/(?P<pk>\d+)/$',views.search1,name='search1'),
    path('levelsearch/',views.levelsearch,name='levelsearch'),
    # path('search1/',views.search1,name='search1'),
    path('modify/',views.modify,name='modify'),
    #url(r'^update/(?P<pk>\d+)/$',views.update,name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.delete,name='delete'),
    url(r'^actualmodify/(?P<pk>\d+)/$',views.actualmodify,name='actualmodify'),




    #path('',views.login,name='login'),

]