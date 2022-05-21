from django.shortcuts import render
from django.views import View
from academics.models import Academic
from experiences.models import Experience
from projects.models import Project
from tools.models import Tool
import pyautogui


class Index(View):
    template = 'index.html'

    def get(self, request):
        experiences = Experience.objects.all()
        academics = Academic.objects.all()
        projects = Project.objects.all()
        tools = Tool.objects.all()
        width, height = pyautogui.size()

        return render(request, self.template, {'academics': academics, 'experiences': experiences, 'projects': projects, 'tools': tools, 'width': width})