from django.shortcuts import render_to_response
from django.template import RequestContext
def index(request):
    return render_to_response("javascript.html")

from image_data import IMAGES

def get_image(request):
    if request.method == 'GET':
        imgId = request.GET.get('ImageID',None)
        if imgId is None:
            print 'imgId is None'
            return index(request)
        data = dict(info=IMAGES[imgId])
        return render_to_response("imageDate.html",
                                  data, context_instance=RequestContext(request))
