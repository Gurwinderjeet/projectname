from django.shortcuts import render,HttpResponse
from firstapp.forms import UserRoleForm,UserInfoForm

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def testresponse(request):
    return HttpResponse("<h1>Hello,First response</h1>")
def userhome(request):
    return HttpResponse("<h1>Welcome user</h1>")
def addroles(request):
    form=UserRoleForm()
    if(request.method=="POST"):
        form = UserRoleForm(request.POST)
        form.save()
        return render(request,"addroles.html",{'form':form,
                    'inserted':True})
    return render(request,"addroles.html", {'form':form})
#to send data from views.py to page, create dictionary.
def excluderole(request):
    if request.method=="POST":
        form=UserInfoForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.name=request.POST['name']
            f.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("It is not valid")
    return render(request,"excluderole.html")
