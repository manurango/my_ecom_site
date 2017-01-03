"""frobshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from mpesa.app import application as mpesa_application
from oscar.app import application

#from oscar.app import Shop
#from mpesa.app import MpesaApp
#import mpesa
#from mpesa.app import application
#from paypal.express.dashboard.app import application

urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/', include(admin.site.urls)),
    (r'', include(application.urls)),
    (r'', include(mpesa_application.urls)),
    #(r'', include(Shop.urls)),
     #(r'', include(MpesaApp.urls)),

    (r'^checkout/paypal/', include('paypal.express.urls')),
    
    # Optional
    #(r'^dashboard/paypal/express/', include(application.urls)),
)#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
