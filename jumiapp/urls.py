
from django.contrib import admin
from django.urls import path
from jumiapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home ),
    path('about/',views.about ),
]
