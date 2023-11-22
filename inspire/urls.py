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
from badges import views as badges_views
from menu import views as menu_views

from django.conf.urls.static import static
from django.conf import settings
from Recompensa import views as Tienda_views


urlpatterns = [
    path('admin', admin.site.urls),

    
    #url de recompensa
    path('Tienda',Tienda_views.Recompensas,name="Tienda"),
    path('CrearRecompensa',Tienda_views.CrearRecompensas,name="CrearRecompensa"),
    path('CrearRecompensa_',Tienda_views.CrearRecompensas_,name="CrearRecompensa_"),
    path('VisualizarRecompensas',Tienda_views.VisualizarRecompensas,name="VisualizarRecompensas"),
    
   
    # path('my_profile', challenges_views.my_profile, name='my_profile'),
    
    path('ranking', challenges_views.ranking, name='ranking'),
    path('challenges', challenges_views.challenges, name='challenges'),
    path('create_challenge', challenges_views.create_challenge, name='create_challenge'),
    path('create_challenge_', challenges_views.create_challenge_, name='create_challenge_'),
    path('edit_challenge/<int:reto_id>/', challenges_views.edit_challenge, name='edit_challenge'),
    path('start_challenge/<int:reto_id>/', challenges_views.start_challenge, name='start_challenge'),
    path('end_challenge/<int:reto_id>/', challenges_views.end_challenge, name='end_challenge'),
    path('view_challenges', challenges_views.view_challenges, name='view_challenges'),
    
    path('profile', accounts_views.profile, name='profile'),
    path('sign_up_employer', accounts_views.sign_up_employer, name='sign_up_employer'),
    path('sign_up_employee', accounts_views.sign_up_employee, name='sign_up_employee'),
    path('sign_up_type', accounts_views.sign_up_type, name='sign_up_type'),
    path('show_progress', challenges_views.show_progress, name="show_progress"),
    
    path('create_employee_', accounts_views.create_employee_, name='create_employee_'),
    path('create_employer_', accounts_views.create_employer_, name='create_employer_'),
    
    path('login/', accounts_views.login, name='login'),
    path('login_view', accounts_views.login_view, name='login_view'),

    path('badges', badges_views.main, name='main_page'),
    path('create_badge', badges_views.create_badge, name="create_badge"),
    path('edit_badge', badges_views.edit_badge, name="edit_badge"),
    path('assign_badge', badges_views.assign_badge, name="assign_badge"),
    path('delete_badge/<int:insignia_id>/', badges_views.delete_badge, name='delete_badge'),
    path('assertion/<int:insignia_id>/<int:id>', badges_views.assertion ,name='assertion'),

    path('log_out', accounts_views.log_out, name='log_out'), 
    
    path('header', menu_views.header, name='header'),
    path('', menu_views.home2),
    path('home2', menu_views.home2, name='home2'),



    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
