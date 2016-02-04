from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.template import loader
from django.shortcuts import redirect
from authentication.views import auth
#View to handle personal information
def personalinfo(request):
    print(request.user)
    if(request.user.is_anonymous()):
        return redirect(auth)
    #return HttpResponse("Test page. Yet to be designed",status=200)
    template = loader.get_template('chatbot/chat.html')
    context={}
    return HttpResponse(template.render(context,request),status=200)