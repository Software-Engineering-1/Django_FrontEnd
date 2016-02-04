from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.template import loader
#View to handle personal information
@login_required
def personalinfo(request):
    #print(request.POST)
    #return HttpResponse("Test page. Yet to be designed",status=200)
    template = loader.get_template('chatbot/chat.html')
    context={}
    return HttpResponse(template.render(context,request),status=200)