from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from App_madical.models import *
from django.contrib import messages
# Create your views here.


def Homepage(request):
    mdata = order.objects.all().order_by('-id')
    return render(request,'home.html',{'data':mdata})
    # print(mdata)

def addpage(request):
    return render(request,'add.html')

def datapage(request):
    mt = request.POST
    nm = mt.get('name')
    pr = mt.get('price')
    quan = mt.get('quantity')
    sal = mt.get('saller')
    com = mt.get('company')
    tol = float(pr)*float(quan)
    # print(tol)
    print(com)
    s = order.objects.create(M_name=nm,M_price=pr,M_quantity=quan,M_saller=sal,M_comapany=com,M_amount=tol)
    s.save()
    # print(s)
    return  HttpResponseRedirect('/')

def view_content_page(request,a):
    content_data = order.objects.get(id=a)
    return render(request,'view.html',{'D':content_data})


def update_page(request,k):
    val = order.objects.get(id=k)
    return render(request,'UpdateItems/1Update.html',{'V':val})


def update_page2(request):
    dt = request.POST
    id = dt.get("id")
    nm = dt.get('name')
    pr = dt.get('price')
    qn = dt.get('quantity')
    sel = dt.get('saller') 
    com = dt.get('company')
    # to = dt.get('total')
    # tr = order.objects.create(M_name=nm,M_price=pr,M_quantity=qn,M_saller=sel,M_comapany=com)
    tr = order.objects.get(id=id)
    tr.M_name = nm
    tr.M_price = pr
    tr.M_quantity = qn
    tr.M_saller = sel
    tr.M_comapany = com
    tr.save()


    # tr.save
    return HttpResponseRedirect('/')


def deletepage(request,d):
    dl = order.objects.get(id=d)
    dl1=dl
    dl.delete()
    return render(request,'del.html',{'D1':dl1})

def product_page(request):
    fil = 'Instock/input_instock.html'
    D1 = Instock.objects.all()
    print(Instock.N_supplier_name)
    # print()
    return render(request,fil,{'D':D1})
    


def enter_product_page(request):
    rt = request.POST
    nm = rt.get('name')
    pr = rt.get('price')
    qn = rt.get('quantity')
    sup = rt.get('supplier')
    nt = Instock.objects.create(N_name=nm,N_price=pr,N_quantity=qn,N_supplier_name=sup)
    nt.save()
    return HttpResponseRedirect('/')


def updateData_page(request):
    h_file = 'UpdateItems/Find_update.html'
    d1 = order.objects.all()
    return render (request,h_file,{'D1':d1})


def find_and_update(request):
    h_file = 'UpdateItems/Find_update.html'
    sr = request.POST.get('Search')
    if(request.method == 'POST'):
        dt = order.objects.filter(M_name__iexact=sr)
        print(dt)
        print(sr)
        return render(request,h_file,{'data':dt},{'res':sr})
    else:
        return render(request,h_file,{'res':sr})


def report_page(request):
    h_file = 'Bill_Report/report.html'
    # dt = order.objects.all()
    return render(request,h_file)


def get_report_page(request):
    h_file = 'Bill_Report/report.html'
    if(request.method == 'POST'):
        st = request.POST.get('start_date')
        et = request.POST.get('end_date')

        print(st)
        print(et)


        dt = order.objects.filter(M_date__gte=st,M_date__lte=et)
        print(dt)
        print(st)
        print(et)
        # order.objects.M_date
        return render(request,h_file,{'data':dt})
    else:
        return HttpResponseRedirect('/')
