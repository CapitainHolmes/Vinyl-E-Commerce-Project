from django.shortcuts import render
from productsVinyls.models import Vinyl

# Create your views here.

# A view for the searching of vinyls funnctionality

def do_search(request):
    vinyls = Vinyl.objects.filter(artist__icontains=request.GET['q'])
    return render(request, "vinyls.html", {"vinyls": vinyls})