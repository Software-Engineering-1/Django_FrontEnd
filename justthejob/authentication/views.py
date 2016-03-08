from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from chatbot.views import personalinfo
from django.shortcuts import redirect
@csrf_exempt
def login_user(request):
    if(request.method=="POST"):
        data=request.POST
        if(data['title'])=='LOGIN':
            username=data['username']
            password=data['password']
            print("GOT")
            user=authenticate(username=username,password=password)
            if(user is not None):
                login(request,user)
                return redirect(personalinfo)
            else:
                template = loader.get_template('authentication/homepage.html')
                context={'error':2}
                return HttpResponse(template.render(context,request))
        elif(data['title'])=='REGISTER':
            username=data['username']
            password=data['password']
            email=data['email']
            try:
                u=User.objects.create_user(username,email,password)
            except Exception as e:
                print(e)
                template = loader.get_template('authentication/homepage.html')
                context={'error':1}
                return HttpResponse(template.render(context,request))
            else:
                u.save()
                user=authenticate(username=username,password=password)
                login(request,user)
                return redirect(personalinfo)
    else:
        template = loader.get_template('authentication/homepage.html')
        context={'error':0}
        return HttpResponse(template.render(context,request))

@csrf_exempt
def register(request):
    if(request.POST):
        data=request.POST
        username=data['username']
        password=data['password']
        email=data['email']

        try:
            u=User.objects.create_user(username,email,password)
        except Exception as e:
            print(e)
            template = loader.get_template('authentication/homepage.html')
            context={'error':1}
            return HttpResponse(template.render(context,request))
        else:
            u.save()
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(personalinfo)
    else:
        template = loader.get_template('authentication/register.html')
        context={'error':0}
        return HttpResponse(template.render(context,request),status=200)