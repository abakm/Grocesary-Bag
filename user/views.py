from django.shortcuts import render,redirect,HttpResponse
from table.models import *
import datetime
from django.contrib import messages
# Create your views here.
def users(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    id = request.session['id']
    u=user.objects.get(user_id=id)

    return render(request,'user/user.html',{'u':u})

def add(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    id=request.session['id']
    if request.method=='POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date= request.POST.get('date')
        t=item.objects.filter(name=name)
        if t.count()>0:
            messages.error(request, "item already exists")
            return redirect('http://127.0.0.1:8000/user/add/')

        t=item(name=name,quantity=quantity,status=status,date=date,user_id_id=id)
        t.save()
        messages.success(request, "Inserted successfully")

    u = user.objects.get(user_id=id)
    return render(request,'user/add.html',{'u': u})

def view(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    id = request.session['id']
    t=item.objects.filter(user_id_id=id)
    if request.method=="POST":
        date=request.POST.get('date')
        print(date)
        t=t.filter(date=date)

    u = user.objects.get(user_id=id)

    return render(request, 'user/view.html',{'t':t,'u': u})

def delete(request,item_id):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    id = request.session['id']
    t = item.objects.filter(id=item_id, user_id_id=id)
    if t.count() == 0:
        messages.success(request, "cannot access")
        return redirect('http://127.0.0.1:8000/user/view')

    item.objects.filter(id=item_id,user_id_id=id).delete()
    messages.success(request, "Deleted successfully")
    return redirect('http://127.0.0.1:8000/user/view')

def update(request,item_id):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')
    id = request.session['id']
    t = item.objects.filter(id=item_id,user_id_id=id)
    if t.count()==0:
        messages.success(request, "cannot access")
        return redirect('http://127.0.0.1:8000/user/view')
    t = item.objects.get(id=item_id, user_id_id=id)
    if request.method=="POST":
        #name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        item.objects.filter(id=id).update(quantity=quantity,status=status,date=date)
        messages.success(request, "Updated successfully")
        return redirect('http://127.0.0.1:8000/user/view')

    if t.date<datetime.date.today():
        min=str(datetime.date.today())
    else:
        min = str(t.date +datetime.timedelta(days=1) )
    u = user.objects.get(user_id=id)
    return render(request, 'user/update.html', {'t': t,'u':u,'min':min})


