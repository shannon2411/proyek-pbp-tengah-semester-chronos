from django.shortcuts import render, redirect
from apotik_app.models import Apotik
from .forms import ApotikForm
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    apotek = Apotik.objects.all().values()  # TODO Implement this
    response = {'apotik': apotek}
    return render(request, 'apotik_index.html', response)

def search(request):
        if 'inputan' in request.GET:
            q=request.GET['inputan']
            apotek=Apotik.objects.filter(daerah__icontains=q)
        else:
            apotek=Apotik.objects.all()
        html = render_to_string(template_name="apotik_list.html", context={"apotek": apotek})
        print(apotek)
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

def search_json(request):
    if 'inputan' in request.GET:
        inputan = request.GET['inputan']
        apotik = Apotik.objects.filter(daerah__icontains=inputan).order_by('id')
    else:
        apotik = Apotik.objects.all().order_by('id')
    data = serializers.serialize('json', apotik)
    return HttpResponse(data, content_type="application/json")