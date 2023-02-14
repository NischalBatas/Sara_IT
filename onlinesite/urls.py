from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name="services"),
    path('contact', views.contact, name='contact'),
    path('prices', views.prices, name='prices'),
    path('cap', views.cap, name='cap'),
    path('demos',views.demos,name='demos')
    
]


urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
