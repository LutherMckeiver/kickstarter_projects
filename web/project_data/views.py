from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project
from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def projects_list_view(request):
    project_queries = get_list_or_404(Project)
    
    paginator = Paginator(project_queries, 20)
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects_list.html', context)


def projects_detail_view(request, pk):
    project = get_object_or_404(Project, id=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/projects_detail.html', context)


