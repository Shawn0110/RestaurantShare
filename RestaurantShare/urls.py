from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendEmail/', include('sendEmail.urls')),
    path('admin/', admin.site.urls),
]
