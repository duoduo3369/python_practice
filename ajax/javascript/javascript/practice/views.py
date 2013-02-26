from django.shortcuts import render_to_response
from django.template import RequestContext
from image_data import IMAGES
from django.http import HttpResponse

from json_ import *
def index(request):
    return render_to_response("index.html")

def base(request):
    return render_to_response("javascript.html")



def get_image(request):
    if request.method == 'GET':
        imgId = request.GET.get('ImageID',None)
        if imgId is None:
            print 'imgId is None'
            return index(request)
        return HttpResponse(IMAGES[imgId])

def movies(request):
    return render_to_response("registration.html")

def user_validation(request):
    if request.method == 'GET':
        username = request.GET.get('username',None)
        if username is None:
            print 'username is None'
            return index(request)

        if not is_register(username):
            print username+' okay'
            return HttpResponse('okay')
        print username+'not okay'
        return HttpResponse('not okay')
