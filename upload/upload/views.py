#!/usr/bin/env python
# coding=utf-8

from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext,Template
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def file_upload(request):
    ip = get_client_ip(request)
    print ip
    print settings.WRITE_IP
    if ip not in settings.WRITE_IP:
        return HttpResponse(json.dumps({"retcode":-1}))
    if request.method == "POST":
        file = request.FILES.get("file")
        file_type = request.POST.get("type") or ""
        if not file:
            msg = {"retcode":-2}
            msg = json.dumps(msg)
            return HttpResponse(msg)
        file_name = request.FILES.get("filename")
        if not file_type:
            file_type = os.path.splitext(file_name)[0]

    return HttpResponse(json.dumps({"ip":ip}))

def bytes_upload(request):
    pass
