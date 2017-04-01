from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'ˆadmin/', admin.site.urls),
    url(r'', include('blog.urls'))
]
