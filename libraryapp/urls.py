from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.urls import path


# This file will define all of the URLs that your library application will respond to. Place the following code in it.

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
    url(r'^librarians$', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    url(r'^librarian/form$', librarian_form, name='librarian_form'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^libraries$', list_libraries, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    url(r'^libraries/(?P<library_id>[0-9]+)/form$', library_edit_form, name='library_edit_form'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),







]