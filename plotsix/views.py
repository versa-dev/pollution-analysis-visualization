from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def boxchart(request):
    template = "plottwo.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata, "plotsix": True}
    if request.method == "GET":
        return render(request, template, prompt)

    CurrentCity=request.POST['currentcity']
    pollution = PollutionData.objects.filter(city = CurrentCity)
    so2 = []
    no2 = []
    pm10 = [] 
    co = []
    o3_8 =[]
    pm25 = []
    for item in pollution:
        so2.append(float(item.pm25))
        no2.append(float(item.no2))
        pm10.append(float(item.pm10))
        co.append(float(item.co))
        o3_8.append(float(item.o3_8))
        pm25.append(float(item.pm25))
    data_to_plot = [so2,no2,pm10,co,o3_8,pm25]
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot()
    ax.set_title('PM2.5 boxplot by different type')
    ax.set_xticklabels(["PM2.5","NO2", "PM10", "CO", "O3_8", "PM25"])
    bp = ax.boxplot(data_to_plot)
    plt.legend() 
    plt.savefig('media/multiboxchart.png', bbox_inches='tight')
    plt.close()
    return render(request, template, {"citydata": citydata, 'multiboxchart': True})