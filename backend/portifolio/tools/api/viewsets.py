from rest_framework.viewsets import ModelViewSet
from tools.models import Tool
from tools.api.serializers import ToolSerializer


class ToolViewSet(ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer