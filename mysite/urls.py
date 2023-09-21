
from django.contrib import admin
from django.urls import path,include

# path and include  add manually 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('food.urls')),
]
