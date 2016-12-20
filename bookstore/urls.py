from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.default.urls import *
from social.apps.django_app.urls import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('store.urls'),name='store'),
    url(r'^store/',include('store.urls'),name='store'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('',include('social.apps.django_app.urls',namespace='social')),
]
