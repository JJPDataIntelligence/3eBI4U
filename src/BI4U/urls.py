"""BI4U URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=False), name='homeredirect'),
    path('home/', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('funcionario/', include('Funcionario.urls'), name = 'funcionario'),
    path('financeiro/', include('Financeiro.urls'), name='financeiro'),
    path('cliente/', include('Cliente.urls'), name='cliente'),
    path('notification/', include('Notificacao.urls'), name='notification'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
