from rest_framework.viewsets import ModelViewSet
from projects.models import Project
from projects.api.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer