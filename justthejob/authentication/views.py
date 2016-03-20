from django.shortcuts import render     #Required to render our HTML (As in replace the python part in HTML with actual
from django.http import HttpResponse,HttpResponseRedirect   #Required to send HTTPResponse. A View should return one of these
# Create your views here.
from django.template import loader      #Required for loading our html
from django.views.decorators.csrf import csrf_exempt    #Needed . Don't exactly know why yet
from django.contrib.auth.models import User             #Need the default user model.
from django.contrib.auth import authenticate, login     #Needed to work with default user model.
from django.shortcuts import redirect                   #Needed to redirect
from chatbot.views import personalinfo
from mainapp.views import mainView
from .models import UserContact




@csrf_exempt
def homepage(request):
    if( request.session.get('user',None)):
        return redirect(mainView)
    if(request.method=="POST"):
        data=request.POST
        name=data['name']
        email=data['email']
        message=data['message']
        u=UserContact(name=name,email=email,message=message)
        u.save()
        template = loader.get_template('authentication/index1.html')
        context={'message':1}
        return HttpResponse(template.render(context,request))

    template = loader.get_template('authentication/index1.html')    #Load the page
    context={'message':0}                                         #No error. THis is used when he enters bad data in forms
    return HttpResponse(template.render(context,request))


@csrf_exempt
def login_user(request):
    if(request.method=="POST"): #Means it is a post request
        data=request.POST       #Obtain data which was sent in the body. This is a dictionary
        if(data['title'])=='LOGIN': #I've 2 forms on same page.I've given diff values to same key title to distinguish
            username=data['username']
            password=data['password']
            user=authenticate(username=username,password=password)  #Check if the username-password is valid
            if(user is not None):  #Yes. It is valid. So log the user in
                login(request,user) #Login . From this point. Can use request.user to get the user
                request.session['user']=user.username
                return redirect(personalinfo)   #Important. Use this for redirecting him to different page after login
            else:   #He has entered wrong username/password. Load the login page itself again.
                template = loader.get_template('authentication/login.html')
                context={'error':2} #I'm doing {{ if error==2}} alert("Wrong username/passsword") in HTML.So I need this
                return HttpResponse(template.render(context,request))   #Show him the login page again
        elif(data['title'])=='REGISTER':    #The title is for register. Which means submit on register was clicked
            username=data['username']
            password=data['password']
            email=data['email']
            try:        #Throws exception if something goes wrong in creating. Typically username taken
                u=User.objects.create_user(username,email,password)
            except Exception as e:
                print(e)
                template = loader.get_template('authentication/login.html')
                context={'error':1} #I'm doing {{ if error==1}} alert("Wrong username taken")
                return HttpResponse(template.render(context,request))   #Render back the login page
            else:   #No exception. User was created sucessfully
                u.save()    #Important. Save to database
                user=authenticate(username=username,password=password)  #Authenticate the new user in
                login(request,user)#Login the new user. ^We know authenticate will work. But login needs auth to be called
                request.session['user']=user.username
                return redirect(personalinfo)   #redirect him to the next page you intend to show
    else:   #GET request. Means he has loaded this url from browser. Show him our page
        template = loader.get_template('authentication/login.html')    #Load the page
        context={'error':0}                                         #No error. THis is used when he enters bad data in forms
        return HttpResponse(template.render(context,request))       #Render the HTML page

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

@csrf_exempt
def fp(request):
    if(request.method=="POST"):
        f=request.FILES['myfile']
        for s in f.chunks():
            print(s)
        return HttpResponse("HI")
    else:
        template = loader.get_template('authentication/fp.html')
        context={}
        return HttpResponse(template.render(context,request),status=200)




