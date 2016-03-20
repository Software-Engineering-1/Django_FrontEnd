from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#Just a placeholder to redirect to after login process is done
def mainView(request):

    return HttpResponse("Placeholer page.Things are working,"+str(request.session.get('user','NO')),status=200)