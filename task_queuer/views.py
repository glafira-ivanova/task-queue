import json
from datetime import datetime

from django.http import HttpResponse
from django.template import loader

from .models import Task


def task_list(request):
    template = loader.get_template("task_list.html")
    return HttpResponse(template.render(template))


def task_query(request):
    serialized_object_list = []
    for task in Task.objects.all():
        serialized_object_list.append({
            'id': task.pk,
            'create_time': task.create_time.isoformat(),
            'finish_time': '' if not task.finish_time else task.finish_time.isoformat(),
            'status': task.get_status()
        })
    return HttpResponse(json.dumps(serialized_object_list))


def add_task(request):
    Task.objects.create(create_time=datetime.now())
    return HttpResponse(status=201)
