from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def graphchart(request):
    template = "plottwo.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata, "plotthree": True}
    if request.method == "GET":
        return render(request, template, prompt)

    CurrentCity=request.POST['currentcity']
    pollution = PollutionData.objects.filter(city = CurrentCity)
    print(pollution)
    x = []
    y = []
    for item in pollution:
        y.append(item.pm25)
        x.append(item.date)
    plt.plot(x, y, label = "PM2.5 per Year Curve") 
    print(CurrentCity)
    print(y)
    plt.xlabel('year - axis') 
    plt.ylabel('PM2.5 - axis') 
    plt.title('concentration of PM2.5 (or other pollutants) with years ') 
    plt.legend() 
    plt.savefig('media/graphchart.png')
    plt.close()
    return render(request, template, {"citydata": citydata, 'graphchart': True})