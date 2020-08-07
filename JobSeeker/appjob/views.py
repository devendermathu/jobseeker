from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from appjob.models import *
# from appjob.admin import *
# Create your views here.

def homepage(request):
    # jb = JOBS.objects.all()
    jb = create.objects.all()
    return render(request,'home.html',{'T1':jb,'user':request.user})

def Login_page(request):
    if(request.method == 'POST'):
        usern = request.POST['user']
        pas = request.POST['pass']
        user = authenticate(request,username=usern,password=pas)
        if(user):
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')      
    else:
        return render(request,'login.html')
    # if(request.user.is_authenticated):
    #     return HttpResponseRedirect('/')
        
    #     if(request == "POST"):
    #         us = request.POST['user']
    #         ps = request.POST['pass']    
    #         login(request,us)
    #         return HttpResponseRedirect('/')
    #     else:
    #         return render(request,'login.html')

    # else:
    #     return render(request,'login.html')

    # if(request.user.is_authenticated):
    #     return HttpResponseRedirect('/')

    #     if(request == "POST"):
    #         us = request.POST['user']
    #         ps = request.POST['pass']
    #         usr = authenticate(username=us,password=ps)
    #         if(usr is not None):
    #             login(request,usr)
    #             return HttpResponseRedirect('/')
    #         else:
    #             return render(request,'login.html')

    #     else:
    #         return render(request,'login.html')
    # else:
    #     return render(request,'login.html')


def createpage(request):
    return render(request,'create.html')

def contain_page(request):
    if(request.method == "POST"):
        ps = request.POST
        nm = ps.get('name')
        ad = ps.get("add")
        cn = ps.get("cnt")
        em = ps.get("email")
        org = ps.get("org")
        jb = ps.get("jbs")
        expt = ps.get('expt')
        # print(ad)
        str(create.objects.create(name=nm,addres=ad,contact=cn,email=em,org_name=org,jobs=jb,exp=expt))
        return HttpResponseRedirect('/')
        # nst.save()


    else:
        return render(request,'create.html')


def details(request,e):
    dt = create.objects.get(id=e)
    return render(request,'detail.html',{'T1':dt})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



def search_page(request):
    sr = request.POST.get('search')
    dt = create.objects.filter(jobs__icontains=sr)
    # print(sr)
    # print(dt)
    return render(request,'home.html',{'data':dt,'src':sr,'user':request.user})


def lpage(request):
    return render(request,'login.html')