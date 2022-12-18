from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import views


urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search_topic, name="search"),
    path("search_results/<topic>/<geo>/<time>/", views.search_results, name="search_results"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
