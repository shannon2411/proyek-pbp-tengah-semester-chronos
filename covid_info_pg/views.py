from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Data
import requests as req
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

def index(request):
    datas = Data.objects.all().values()
    response = {'data': datas}
    return render(request, 'covid_info_pg/covinfo.html', response)


def get_covid_ind(request):
    fetch_data = req.get("https://data.covid19.go.id/public/api/update.json")
    data_raw = fetch_data.json()['update']['harian'][-7:]
    labels = []
    dataMeninggal = []
    dataPositif = []
    dataRecovery = []
    
    for i in range(len(data_raw)):
        labels.append(data_raw[i]['key_as_string'][:10])
        dataMeninggal.append(data_raw[i]['jumlah_meninggal']['value'])
        dataPositif.append(data_raw[i]['jumlah_positif']['value'])
        dataRecovery.append(data_raw[i]['jumlah_sembuh']['value'])
    
    return JsonResponse(data = {
        "labels": labels,
        "dataMeninggal" : dataMeninggal,
        "dataPositif" : dataPositif,
        "dataRecovery" : dataRecovery
    }, safe=False)

@csrf_exempt
def fetch_data_prov(request):
    context = {}
    if 'query' in request.GET:
        q=request.GET['query']
        temp=Data.objects.filter(provinsi__iexact=str(q)).first()
        if (temp == None):
            errors = "Data tidak ditemukan"
        else : 
            data = temp
            response = {'provinsi': data.provinsi, 'positif': data.positive, 'meninggal': data.death, 'sembuh': data.recovered}
            return JsonResponse(data=response, safe=False)
    else:
        errors="Tidak ada query"
    context["errors"] = errors
    return JsonResponse(data=context, safe=False)

def get_covid_prov(request):
    context = {}
    if 'query' in request.GET:
        q=request.GET['query']
        data=Data.objects.filter(provinsi__iexact=q).first()
    else:
        data=Data.objects.all().values()
    context["data"] = data
    html = render_to_string(template_name="covid_info_pg/covcontent.html", context=context)
    data_render = {"html_from_view": html}
    return JsonResponse(data=data_render, safe=False)