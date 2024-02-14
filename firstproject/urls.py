
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^firstapp/', include('firstapp.urls'), name='firstapp'),
    url(r'^secondapp/', include('secondapp.urls'), name='secondapp'),
    url(r'^thirdapp/', include('thirdapp.urls')),
    url(r'^' , include('homeapp.urls')),
]
