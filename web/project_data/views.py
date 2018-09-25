from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project


def projects_list_view(request):
    projects = get_list_or_404(Project)
    # projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects_list.html', context)


def projects_detail_view(request, pk):
    project = get_object_or_404(request, id=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/projects_detail.html', context)


