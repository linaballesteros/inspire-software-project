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
from challenges import views as challenges_views
from accounts import views as accounts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', challenges_views.home2),
    # path('my_profile', challenges_views.my_profile, name='my_profile'),
    path('ranking', challenges_views.ranking, name='ranking'),
    path('challenges', challenges_views.challenges, name='challenges'),
    path('create_challenge', challenges_views.create_challenge, name='create_challenge'),
    path('create_challenge_', challenges_views.create_challenge_, name='create_challenge_'),
    path('edit_challenge/<int:reto_id>/', challenges_views.edit_challenge, name='edit_challenge'),
    path('view_challenges', challenges_views.view_challenges, name='view_challenges'),
    path('login', challenges_views.login, name='login'),
    path('sign_up', challenges_views.sign_up, name='sign_up'),
    path('home2', challenges_views.home2, name='home2'),
    
    path('profile', accounts_views.profile, name='profile'),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
