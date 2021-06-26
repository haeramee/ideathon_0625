from django.shortcuts import render
from .models import Userinfo

# Create your views here.
def view(request):
    userdic = Userinfo.objects.all()
    return render(request, 'view.html', {'userdic': userdic})

def write(request):
    return render(request, 'write.html')

def create(request):
    new_profile = Userinfo
    request.POST['realname']
    request.POST['nickname']
    request.POST['gender_m']
    request.POST['gender_f']
    request.POST['age']
    request.POST['major']
    request.POST['studentID']
    request.POST['introduction']
    request.POST['profile_img']
    request.POST['sleep_time']
    request.POST['cleanliness']
    request.POST['cook']
    request.POST['smoker']
    request.POST['nonsmoker']
    request.POST['rent']
    request.POST['deposit']
    request.POST['hope_area']