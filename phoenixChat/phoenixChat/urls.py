from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import signup, home, log_in
from django.contrib.auth.views import LoginView as login

app_name = 'chat'
urlpatterns = [
    path(r'login/',log_in, name='login'),
    path('',signup, name='signup'),
    path('home/', home,name='home'),
    path('admin/', admin.site.urls),
    path('messages/', include('chat.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('chat.api.urls')),
]
