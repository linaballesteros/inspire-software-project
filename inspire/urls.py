"""
URL configuration for inspire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from inspire_app1 import views as app1_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', app1_views.home2),
    path('my_profile', app1_views.my_profile, name='my_profile'),
    path('ranking', app1_views.ranking, name='ranking'),
    path('challenges', app1_views.challenges, name='challenges'),
    path('create_challenge', app1_views.create_challenge, name='create_challenge'),
    path('create_challenge_', app1_views.create_challenge_, name='create_challenge_'),
    path('edit_challenge/<int:reto_id>/', app1_views.edit_challenge, name='edit_challenge'),
    path('view_challenges', app1_views.view_challenges, name='view_challenges'),
    path('login', app1_views.login, name='login'),
    path('sign_up', app1_views.sign_up, name='sign_up'),
    path('home2', app1_views.home2, name='home2'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
