"""
URL configuration for PNC_2_0_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *
from .controller.TestController import *
from .controller.EntiteController import *
from back.controller.AuthController import getUserConnected

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world, name='hello_world'),
    path('allEntity/<int:nbPage>/', getAllEntitePaginate, name='all_entity_paginate'),
    path('allProfil/<int:nbPage>/', getAllProfilPaginate, name='all_profil_paginate'),
    path('allEntity/', getAllEntite, name='all_entity_paginate'),
    path('allProfil/', getAllProfil, name='all_profil_paginate'),
    path('allProfil/', getAllProfil, name='all_profil'),
    path('auth/', include('back.url.AuthUrl')),
    path('allUser/', getAllUtilisateur, name="all_user"),
    path('nbPageUser/', getNbPagesUtilisateur, name="nb_pages_user"),
    path('allUser/<int:nbPage>', getAllUtilisateurPaginate, name="all_user_paginate"),
    path('userConnected/', getUserConnected, name="user_connected")
]
