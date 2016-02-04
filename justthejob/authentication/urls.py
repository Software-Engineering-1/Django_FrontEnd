__author__ = 'KAI'
__author__ = 'KAI'
from django.conf.urls import url,include
from django.contrib import admin
from authentication import views
urlpatterns = [
    #The pages associated with chatbot
    url(r'^$',views.login_user,name='Login'),
    url(r'^$',views.register,name='Register'),
]
