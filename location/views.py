from django.shortcuts import render

#1
from .models import locationinfo

# Create your views here.
def location(request):
    if request.method == 'POST':
        a = request.POST['Latitude']
        b = request.POST['Longitude']
        info = locationinfo(latitude=a, longitude=b)
        info.save()
        return render(request,'aprilfool.html')       
    else:
        return render(request,'homepage.html')


def update(request):
    if request.method == 'POST':
        a = request.POST['Latitude']
        b = request.POST['Longitude']
        info = locationinfo(latitude=a, longitude=b)
        info.save()
    return render(request,'homepage.html')
    
