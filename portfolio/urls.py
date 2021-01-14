"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importing the "settings" file where, down at the bottom we declared the media dir's :
from django.conf import settings

# importing the whole "static" app (declared in "settings.py" too: 'django.contrib.staticfiles' :
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# DJANGO ver >=1.7 : Serving files uploaded by a user during development (https://docs.djangoproject.com/en/2.2/howto/static-files/)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # DJANGO ver >=1.7 : Serving static files during development
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # DJANGO ver >=1.7 : Serving files uploaded by a user during development

# if settings.DEBUG is False and settings.SANDBOX is True:
#     urlpatterns += patterns('',
#                             # files living in /static/, which can be collected or non-collected assets
#                             (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
#                             # files living in /media/, which is where uploaded files etc should go
#                             (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
#                             )
