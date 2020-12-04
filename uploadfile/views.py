import csv, io
from django.shortcuts import render
from django.contrib import messages
from pollution.models import *

def csv_upload(request):
    template = "csv_upload.html"
    prompt = {
        'pollution_data': 'typeid, so2, no2, pm10, co, o3_8, pm25, receptor, wind_direction, wind_speed, humidity, temperature, date',
        }
    if request.method == "GET":
        return render(request, template, prompt)
    if len(request.FILES) != 0:
        uploaded_data = request.FILES['file']
    else:
        fail = {'fail': 'please select the file to upload'}
        return render(request, template, fail)
    if uploaded_data.name.endswith('.csv'):
        data_set = uploaded_data.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = PollutionData.objects.update_or_create(
                typeid=column[0],
                so2=column[1],
                no2=column[2],
                pm10=column[3],
                co=column[4],
                o3_8=column[5],
                pm25=column[6],
                receptor=column[7],
                wind_direction=column[8],
                wind_speed=column[9],
                humidity = column[10],
                temperature = column[11],
                date = column[12],
                city = column[17]
            )  
            _, vehicle_created = Vehicle.objects.update_or_create(
                engine_family= column[13],
                manufacturer=column[14],
                engine_code=column[15],
                engine_model=column[16]
            )
            if not City.objects.filter(name=column[17]).exists():
                _, city_created = City.objects.update_or_create(
                    name=column[17],
                    latitude=column[18],
                    longitude=column[19],
                    state=column[20]
                )
        context = {'success': 'uploaded successfully'}
        return render(request, template, context)   
    else:
        fail = {'fail': 'please select the CSV file only'}
        return render(request, template, fail)
    
