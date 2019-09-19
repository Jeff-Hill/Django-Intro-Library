from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.urls import path


# This file will define all of the URLs that your library application will respond to. Place the following code in it.

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', list_libraries, name='libraries'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^library/form$', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),






]