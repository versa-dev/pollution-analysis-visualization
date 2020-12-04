from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def dotchart(request):
    template = "plottwo.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata, "plotseven": True}
    if request.method == "GET":
        return render(request, template, prompt)

    CurrentCity=request.POST['currentcity']
    pollution = PollutionData.objects.filter(city = CurrentCity)
    data_to_plot = []
    winddirection = []
    for item in pollution:
        data_to_plot.append(float(item.pm25))
        winddirection.append(float(item.wind_direction))
    plt.plot(winddirection,data_to_plot, 'ro')
    plt.axis([0, 360, 0, 500])
    plt.ylabel('PM2.5')
    plt.xlabel('Angle (0 - 360)')
    plt.legend() 
    plt.savefig('media/dotchart.png', bbox_inches='tight')
    plt.close()
    return render(request, template, {"citydata": citydata, 'dotchart': True})