from django.shortcuts import render
from .models import Userinfo

# Create your views here.
def write(request):
    userdic = Userinfo.objects.all()
    return render(request, 'write.html', {'userdic': userdic})