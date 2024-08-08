from django.shortcuts import redirect, render

def home(request):
    return render(request,"pages/index.html" , content_type="text/html")
