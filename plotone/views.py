from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pollution.models import *

def barchart(request):
    template = "plotone.html"
    citydata = City.objects.all()
    prompt = {"citydata": citydata}

    if request.method == "GET":
        return render(request, template, prompt)

    if (request.POST.getlist) != 0:

        Cities=request.POST.getlist('states[]')

    else:
        fail = {'fail': 'please select one or more cities to see'}
        return render(request, template, fail)

    Co_Per_Cities = []
    for city in Cities:
        pollution = PollutionData.objects.filter(city = city)
        recent_year = 0
        for item in pollution:
            if item.date > recent_year:
                recent_year = item.date
                temp = item
        Co_Per_Cities.append(temp.co)

    csfont = {'fontname':'Comic Sans MS'}
    hfont = {'fontname':'Helvetica'}
    plt.bar(Cities, Co_Per_Cities,width = 0.2)
    plt.title('Cities Vs levels of CO ', **csfont)    
    plt.xlabel('Cities', **hfont)
    plt.ylabel('levels of CO', **hfont)
    plt.savefig('media/barchart.png')
    plt.close()
    return render(request, template, {"citydata": citydata, "barchart": True})