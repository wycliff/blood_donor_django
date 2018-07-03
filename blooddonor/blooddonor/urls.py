"""blooddonor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myrest import views
#from django.conf.urls import include
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

#DRF router configs
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'book', views.BookViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(router.urls)),
    url(r'^myrest/', include('myrest.urls', namespace = 'rest')),
    url(r'^api-token-auth/', obtain_jwt_token), # url that obtains the auth token.
    url(r'^myrest/users/', include(('myrest.api.urls','mysrest'), namespace = 'users-api')),
]
