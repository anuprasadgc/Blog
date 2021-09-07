from django.shortcuts import render
from django.http import HttpResponse
from blogapp.forms import *
from blogapp.models import *
from django.db.models import Q
# Create your views here.

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def viewblog(request):
    k=Blogpost.objects.all()
    return render(request, 'viewblog.html',{'s':k})

def viewoneblog(request,pk):
    a = Blogpost.objects.get(pk=pk)
    return render(request,'viewoneblog.html',{'s':a})

def deleteblog(request,pk):
    a = Blogpost.objects.get(pk=pk)
    a.delete()
    return viewblog(request)

def createblog(request):
    form = BlogForm
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)

    return render(request,'createblog.html',{'form':form})

def editblog(request,pk):
    view = Blogpost.objects.get(pk=pk)
    form = BlogForm(instance=view)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=view)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("ERROR FORM INVALID")
    
    return render(request,'createblog.html',{'form':form})

def search(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Blogpost.objects.filter(Q(title__icontains=srch) | Q(author__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                return search(request)
        else:
            return HttpResponse("NO results Found")

    return render(request, 'search.html')