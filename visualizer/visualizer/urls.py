from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from visualize.views import entity_visualizer

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'visualizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^visualize$', entity_visualizer),
)
