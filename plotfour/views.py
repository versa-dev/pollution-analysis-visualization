from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def boxchart(request):
    template = "plottwo.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata, "plotfour": True}
    if request.method == "GET":
        return render(request, template, prompt)

    CurrentCity=request.POST['currentcity']
    pollution = PollutionData.objects.filter(city = CurrentCity)
    data_to_plot = []
    for item in pollution:
        data_to_plot.append(float(item.pm25))
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    ax.set_title('PM2.5 boxplot')
    ax.set_xticklabels(['PM2.5'])
    bp = ax.boxplot(data_to_plot)
    plt.legend() 
    plt.savefig('media/boxchart.png', bbox_inches='tight')
    plt.close()
    return render(request, template, {"citydata": citydata, 'boxchart': True})