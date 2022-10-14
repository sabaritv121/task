from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from zf_app.forms import LoginRegister, AdminRegister, StudentRegister, AddMarks
from zf_app.models import student, marks


def home(request):
    return render(request,"home.html")


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request,"base.html")

def admindash(request):
    return render(request,"base.html")





#registration admin


def admin_reg(request):
    form1=LoginRegister()
    form2=AdminRegister()
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
         form2 = AdminRegister(request.POST,request.FILES)

         if form1.is_valid() and form2.is_valid():
                user = form1.save(commit=False)
                user.is_adm = True
                user.save()
                user1 = form2.save(commit=False)
                user1.user = user
                user1.save()
                return redirect('log')

    return render(request,'reg.html',{'form1': form1, 'form2': form2})


#registration student


def student_reg(request):
    form1=LoginRegister()
    form2=StudentRegister()
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
         form2 = StudentRegister(request.POST,request.FILES)

         if form1.is_valid() and form2.is_valid():
                user = form1.save(commit=False)
                user.is_student = True
                user.save()
                user1 = form2.save(commit=False)
                user1.user = user
                user1.save()
                return redirect('log')

    return render(request,'student_reg.html',{'form1': form1, 'form2': form2})



#login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)

            if user.is_adm:
                print(user)
                return redirect('table')
            elif user.is_student:
                return redirect('studentdash')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'index.html')

@login_required(login_url='login_view')
def studentview(request):
    data=student.objects.all()
    return render(request,'view.html',{"data":data})

@login_required(login_url='login_view')
def student_update(request,id):
    n = student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentRegister(request.POST,request.FILES or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('studentview')
    else:
        form = StudentRegister(instance=n)
    return render(request, 'student_update.html', {'form': form})

#dashboard table

#age
@login_required(login_url='login_view')
def table(request):
    w=student.objects.all
    return render(request,'admin.html',{'w':w})






#delete
@login_required(login_url='login_view')
def delete_student_view(request,id):
    wm=student.objects.get(id=id)
    wm.delete()
    return redirect('studentview')


#add marks
@login_required(login_url='login_view')
def addmark(request):
    form1 = AddMarks()
    if request.method == 'POST':
        form1 = AddMarks(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect("markview")
    return render(request,'addmark.html',{'form1':form1})


#view marks
@login_required(login_url='login_view')
def markview(request):
    data=marks.objects.all()
    return render(request,'markview.html',{'data':data})

#markupdate
@login_required(login_url='login_view')
def mark_update(request,id):
    n = marks.objects.get(id=id)
    if request.method == 'POST':
        form = AddMarks(request.POST,request.FILES or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('markview')
    else:
        form = AddMarks(instance=n)
    return render(request, 'mark_update.html', {'form': form})




#logout

def logout_view(request):
    logout(request)
    return redirect('log')