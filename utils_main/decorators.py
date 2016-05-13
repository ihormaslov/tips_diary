# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.shortcuts import render


def render_to(template_path, allow_ajax=False):
    """
    Decorate the django view.

    Wrap view that return dict of variables, that should be used for
    rendering the template.
    Dict returned from view could contain special keys:
    * MIME_TYPE: mimetype of response
    * TEMPLATE: template that should be used instead one that was
                specified in decorator argument
    """

    def decorator(func):
        def wrapper(request, *args, **kwargs):
            output = func(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output

            if allow_ajax and request.is_ajax():
                return HttpResponse(json.dumps(output), 'application/json')

            if 'MIME_TYPE' in output:
                kwargs['mimetype'] = output.pop('MIME_TYPE')
            template = template_path
            if 'TEMPLATE' in output:
                template = output.pop('TEMPLATE')
            return render(request, template, output, content_type="text/html")
        return wrapper
    return decorator
