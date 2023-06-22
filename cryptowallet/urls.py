
from django.contrib import admin
from django.urls import path, include
from crypto_addresses.urls import urlpatterns


urlpatterns = [
    path("", include(urlpatterns)),
    path('admin/', admin.site.urls),
]
