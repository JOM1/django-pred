from django.http import Http404

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import UploadImageForm
from django.conf import settings
from .botoClient import upload_image, get_image
import urllib3

def upload_file(request):
    session_id = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
    result = ''
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image(request.FILES['image'], session_id)
            http = urllib3.PoolManager()
            response = http.request('GET', 'http://127.0.0.1:5000/pred/%s/%s' % ('images', session_id))
            result = response.data.decode('utf-8')

    else:
        form = UploadImageForm()
    return render(request, 'smartg/upload.html', {'form': form, 'result': result})
