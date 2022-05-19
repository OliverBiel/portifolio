from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from experiences.api.viewsets import ExperienceViewSet
from academics.api.viewsets import AcademicViewSet
from tools.api.viewsets import ToolViewSet
from projects.api.viewsets import ProjectViewSet
from main import views


router = routers.DefaultRouter()
router.register(r'experiences', ExperienceViewSet)
router.register(r'academics', AcademicViewSet)
router.register(r'tools', ToolViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
