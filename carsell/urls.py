from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index,name = 'index'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'^rate/(\d+)/$',views.rate,name='rate'),
    url(r'^index/(?P<pk>\d+)/rating', views.rating, name='rating'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)