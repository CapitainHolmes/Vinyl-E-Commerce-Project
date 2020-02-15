from django.shortcuts import render
from .models import Vinyl
# Create your views here.

# A view to return all vinyls within the database
def all_vinyls(request):
    vinyls = Vinyl.objects.all()
    return render(request, "vinyls.html", {'vinyls': vinyls})