from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('transactions/',
         include('transactions.urls', namespace='transactions')),
    path('', include('index.urls', namespace='index')),
]
