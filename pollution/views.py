from django.shortcuts import render

from .models import *

def pollution_table(request):

    if q := request.GET.get('q'):
        try:
            int(q)
            pollution_data = PollutionData.objects.filter(id=q)
        except:
            pollution_data = None
    else:
        pollution_data = PollutionData.objects.all()

    labels = []

    for field in PollutionData._meta.fields:
        labels.append(field.verbose_name.capitalize())

    context = {
        # 'vehicle_data': vehicle_data,
        'pollution_data': pollution_data,
        'labels': labels,
    }
    return render(request, 'pollution/pollution_table.html', context)


def vehicle_table(request):
    
    # Get search terms from GET request if available.
    if q := request.GET.get('q'):
        try:
            int(q)
            vehicle_data = Vehicle.objects.filter(id=q)
        except:
            vehicle_data = None
    else:
        vehicle_data = Vehicle.objects.all()
    
    labels = []

    for field in Vehicle._meta.fields:
        labels.append(field.verbose_name.capitalize())

    context = {
        'vehicle_data': vehicle_data,
        'labels': labels,
    }
    return render(request, 'pollution/vehicle_table.html', context)

def city_table(request):
    
    # Get search terms from GET request if available.
    if q := request.GET.get('q'):
        try:
            int(q)
            city_data = City.objects.filter(id=q)
        except:
            city_data = None
    else:
        city_data = City.objects.all()
    
    labels = []

    for field in City._meta.fields:
        labels.append(field.verbose_name.capitalize())

    context = {
        'city_data': city_data,
        'labels': labels,
    }
    return render(request, 'pollution/city_table.html', context)
