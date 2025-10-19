from django.shortcuts import render, redirect
from .models import Url
from uuid import uuid4

def index(request):
    return render(request, 'index.html', {'short_url': None})

def create(request):
    if request.method == "POST":
        link = request.POST.get('link')
        uid = str(uuid4())[:5]
        new_url = Url(link=link, uid=uid)
        new_url.save()
        return render(request, 'index.html', {
            'short_url': request.build_absolute_uri('/') + uid, 'inp': link})
    else:
        return redirect(request, index)
    
def redirect_page(request, pk):
    url_details = Url.objects.get(uid=pk)
    return redirect(url_details.link)