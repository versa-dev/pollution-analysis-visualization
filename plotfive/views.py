from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def barchart(request):
    template = "plotthree.html"
    citydata = City.objects.all()
    yeardata = ["2017", "2018", "2019", "2020"]
    prompt = {"citydata": citydata, "yeardata": yeardata}
    if request.method == "GET":
        return render(request, template, prompt)
    if (request.POST['city'] and request.POST['year']):
        city=request.POST['city']
        year=request.POST['year']
    else:
        fail = {'fail': 'please select one or more cities to see'}
        return render(request, template, fail)
    pollution = PollutionData.objects.filter(city = city).filter(date = year)[0]
    Pollution_Per_Year = [pollution.so2,pollution.no2,pollution.pm10,pollution.co,pollution.o3_8,pollution.pm25]
    Elements = ["So2", "No2", "Pm10", "Co", "O3 8", "Pm25"]
    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    plt.bar(Elements, Pollution_Per_Year,width = 0.2)
    plt.title('Elements Vs Pollution', **csfont)    
    plt.xlabel('Elements', **hfont)
    plt.ylabel('levels of Pollution', **hfont)
    plt.savefig('media/multibarchart.png')
    plt.close()
    return render(request, template, {"citydata": citydata,"yeardata": yeardata, "multibarchart": True})