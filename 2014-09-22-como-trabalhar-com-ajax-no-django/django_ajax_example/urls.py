from django.conf.urls import patterns, include, url

urlpatterns = patterns('django_ajax_example.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^filtrar_cidade/$', 'filtrar_cidade', name='filtrar_cidade'),
)
