from django.conf.urls import url
from .views import do_search

# URL for the search functionality
urlpatterns = [
    url(r'^$', do_search, name='search')
]