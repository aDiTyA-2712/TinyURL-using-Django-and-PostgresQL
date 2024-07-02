from django.shortcuts import render,redirect ,get_object_or_404

from django.urls import reverse
from . import service
from .models import Linker
from django.http import Http404

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def shorten_post(request):
    return shorten(request,request.POST['url'])

def shorten(request,url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'main/link.html', {'shortened_url': shortened_url})

def redirect_hash(request, url_hash):
    try:
        original_url = service.load_url(url_hash).original_url
        return redirect(original_url)
    except Linker.DoesNotExist:
        raise Http404("Linker matching Query Doesn't exists")
    