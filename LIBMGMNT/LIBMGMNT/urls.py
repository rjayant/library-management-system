from django.conf.urls import patterns, include, url
import LibraryManagement.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^mine/', include(LibraryManagement.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
