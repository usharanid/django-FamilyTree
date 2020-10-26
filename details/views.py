from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Person
from invitations.models import Invitation
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db import connection
from django.core.mail import send_mail


def mail(request):
    send_mail('Invitation to join Family Tree', 'Body of the message.',
              'from@example.com',
              ['usharanid@gmail.com'])

@login_required(login_url='/login/')
def levelsearch(request):
    #
    # #Q= Person.objects.filter(first_name=username)
    # #raw queries
    # #lname = 'Doe'
    # cursor=connection.cursor()
    #
    # username = request.POST.get('search', False)
    #
    # print(username)
    # print("hello")
    # cursor.execute("select * from details_person as d where d.parentID = (select s.id from auth_user as s where s.username=%s)",username)
    #
    # Q=cursor.fetchall()
    # for x in Q:
    #     print(x)
    # # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s',

    # data = User.objects.filter(id = request.user.id)
    # for i in data:
    #     print(i.email)
    # dat = Invitations.objects.values_list('sentto_mailid', flat=True).filter(sentby=request.user.id)
    # print(dat)
    # P = list(User.objects.values_list('id', flat=True).filter(email__in=dat))
    # print(P)
    # P.append(request.user.id)
    # print(P)

    Q = Person.objects.filter(parentID=request.user.id)
    for i in Q:
        print(i.first_name)
    return render(request, 'details/search.html', {'results': Q})

@login_required(login_url='/login/')
def actualmodify(request,pk):
    if request.method=='POST':
        if pk:
           a= Person.objects.get(pk=pk)
           a.first_name = request.POST['fname']
           a.last_name = request.POST['lname']
           a.sur_name = request.POST['sname']
           a.gender = request.POST['info1']

           a.city = request.POST['city']
           print(request.POST['city'])
           a.country = request.POST['country']
           a.relation = request.POST['info']
           a.save()
           print(a.city)
           return render(request, 'details/modifysuccess.html')
    else:

           Q = Person.objects.filter(pk=pk)
           for i in Q:
               print(i.city)
           return render(request, 'details/showmodify.html',{'results': Q})



@login_required(login_url='/login/')
def delete(request,pk=None):
    if pk:
        Person.objects.filter(pk=pk).delete()
    return render(request, 'details/deletesuccess.html')


# def update(request,pk=None):
#
#     if pk:
#         Q=Person.objects.filter(pk=pk)
#     return render(request, 'details/showmodify.html',{'results': Q})
#
# def update(request,pk=None):
#     if request.method == "POST":
#         form =

@login_required(login_url='/login/')
def modify(request):
    cursor = connection.cursor()

    userid=request.user.id

    print(userid)
    print("hello")
    cursor.execute(
        "select * from details_person as d where d.parentID = %s",userid)

    Q = cursor.fetchall()
    for x in Q:
        print(x)
    # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s',
    return render(request, 'details/modify.html', {'results': Q})

@login_required(login_url='/login/')
def search1(request, pk=None):
        if pk:
            print(pk)
            emailid = Invitation.objects.values_list('email', flat=True).get(id=pk)
            print(emailid)
            P = User.objects.values_list('id', flat=True).get(email=emailid)
            print(P)

            Q = Person.objects.filter(parentID=P)

            return render(request, 'details/search.html', {'results': Q})


@login_required(login_url='/login/')
def search(request):


               dat = Invitation.objects.values_list('email',flat=True).filter(inviter_id=request.user.id)
               print(dat)
               T=[]
               while(True):
                  P = list(User.objects.values_list('id',flat=True).filter(email__in=dat))
                  T.extend(P)
                  print(P)
                  if Invitation.objects.filter(inviter_id__in=P):
                      dat = Invitation\
                          .objects.values_list('email', flat=True).filter(inviter_id__in=P)
                  else:
                      break
               T.append(request.user.id)
               print("T value is",T)


               Q = Person.objects.filter(parentID__in=T).order_by('parentID')
               for i in Q:
                   print(i.first_name)

               return render(request, 'details/search.html', {'results': Q})


@login_required(login_url='/login/')
def addsuccess(request):

        return render(request, 'details/addsuccess.html')

@login_required(login_url='/login/')
def add(request):
        if request.method == 'POST':

                firstname = request.POST['fname']
                lastname = request.POST['lname']
                surname = request.POST['sname']
                gender = request.POST['info1']
                image = request.POST['filename']
                city = request.POST['city']
                country  = request.POST['country']
                relation = request.POST['info']
                r=relation
                relation=request.user.username+relation
                parentID=request.user.id
                createdby=request.user.username
                invitationID=0
                if r == 'Self':
                   print(request.user.email)
                   if request.user.email in Invitation.objects.values_list('email',flat=True):
                       print("Hi")
                       id=Invitation.objects.values_list('inviter_id',flat=True).get(email=request.user.email)

                       parentID=id
                       username=User.objects.values_list('username',flat=True).get(id=id)
                       #relation=Invitations.objects.values_list('relation',flat=True).get(sentto_mailid=request.user.email)
                       relation = username+request.POST['info2']
                       invitationID=Invitation.objects.values_list('id',flat=True).get(email=request.user.email)

                P=Person(first_name=firstname,last_name=lastname,sur_name=surname,gender=gender,image=image,city=city,country=country,parentID=parentID,CreatedBy=createdby,relationship=relation,invitationID=invitationID)
                if not Person.objects.filter(first_name=firstname,last_name=lastname,sur_name=surname).exists():
                     P.save()
                else:
                     messages.info(request, "details already exists")
                     return redirect("details:add")


        else:

          return render(request, 'details/add.html')

        messages.info(request, "Signup completed Successfully")
        return redirect("login:account_signup")
