
from django.contrib import admin
from django.urls import path, include
from core.views import chat

urlpatterns = [
    path("", chat, name="chat"),
    path('api/', include('core.urls')),
    # path("admin/", admin.site.urls),
]
