from django.shortcuts import render
from vaccine.models import Vaccine
from django.core import serializers
from vaccine.forms import VaccineSearchForm
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    vaccines = Vaccine.objects.all().values()
    response = {'vaccines' : vaccines}
    return render(request, 'vaccine_index.html', response)

# add view to handle search vaccine through form
def search(request):
    context = {}

    # create object of form
    search_form = VaccineSearchForm(request.GET or None, request.FILES or None)

    # check if form data is valid
    try:
        if search_form.is_valid():
            form_value = search_form['vaccine_name'].value()
            raw_data = serializers.serialize('python', Vaccine.objects.filter(
            vaccine_name__icontains = form_value))
            actual_data = [d['fields'] for d in raw_data]
            return JsonResponse(actual_data[0], safe=False)
    except:
        return JsonResponse({}, safe=False)
        
    context['search_form']= search_form
    return render(request, "vaccine_form.html", context)