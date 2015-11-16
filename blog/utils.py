import json
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request, item, items_per_page):
    p = Paginator(item, items_per_page)
    page = request.GET.get('p')
    try:
        page = p.page(page)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = None

    if request.GET.get('json'):
        data = []
        if page is not None:
            for i in page.object_list:
                item = {
                    'id': i.id,
                    'title': i.title,
                    'get_excerpt': i.get_excerpt(),
                    'get_absolute_url': i.get_absolute_url(),
                    'date': i.date.strftime("%d.%m.%Y"),
                    'viewed': i.viewed,
                    'preview_image': i.get_preview_thumb()
                }
                data.append(item)
        return HttpResponse(json.dumps(data), content_type="application/json")

    return page
