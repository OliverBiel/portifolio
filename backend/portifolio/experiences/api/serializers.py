from rest_framework.serializers import ModelSerializer
from experiences.models import Experience


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company', 'start_date', 'end_date', 'description']