from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'javascript.practice.views.index', name='index'),
    url(r'^base$', 'javascript.practice.views.base', name='base'),
    url(r'^register$', 'javascript.practice.views.register', name='register'),
    url(r'^get_image', 'javascript.practice.views.get_image', name='get_image'),
    url(r'^user_validation', 'javascript.practice.views.user_validation', name='user_validation'),
    url(r'movies$', 'javascript.practice.views.movies', name='movies'),                      
    # url(r'^javascript/', include('javascript.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns += patterns('',
#           url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name='static'),
#)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
		 url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT_TEST,
        },name='static'),
    )  
