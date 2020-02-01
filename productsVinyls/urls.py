from django.conf.urls import url, include
from .views import all_vinyls

urlpatterns = [
    url(r'^$', all_vinyls, name='vinyls'),
    
]