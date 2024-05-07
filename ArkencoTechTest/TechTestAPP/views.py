from django.shortcuts import render

# Create your views here.

def home_view(request):
    print(request.user.is_staff)
    return render(request,'index.html')