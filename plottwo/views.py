from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def piechart(request):
    template = "plottwo.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata, "plottwo": True}
    if request.method == "GET":
        return render(request, template, prompt)

    CurrentCity=request.POST['currentcity']
    pollution = PollutionData.objects.filter(city = CurrentCity)
    recent_year = 0
    for item in pollution:
        if item.date > recent_year:
            recent_year = item.date
            temp = item
    slices = [temp.so2,temp.no2,temp.pm10,temp.co,temp.o3_8,temp.pm25]
    print(slices)
    labels = ['So2', 'No2', 'Pm10', 'Co', 'O3_8', 'Pm25']
    plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})
    plt.title("A Simple Pie Chart")
    plt.savefig('media/piechart.png')
    plt.close()
    return render(request, template, {"citydata": citydata, "piechart": True})