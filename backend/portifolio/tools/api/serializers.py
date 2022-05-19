from rest_framework.serializers import ModelSerializer
from tools.models import Tool


class ToolSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = ['name', 'logo']
