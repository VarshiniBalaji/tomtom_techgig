from math import sin, cos, sqrt, atan2, radians
import tsp
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
# import mpld3
import mpld3, mpld3.plugins as plugins
from label import lab


def km(lat1,lon1,lat2,lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    distance=round(distance,2)
#     print("Result:", distance)
    return distance

def path(st_ll):
    df=pd.read_csv('db/datall.csv')
    df=df[1:]
    name=list(df['name'])
    lat=list(df['latitude'])
    lon=list(df['longitude'])
    name.insert(0, 'truck_starting_point')
    lat.insert(0,st_ll[0])
    lon.insert(0,st_ll[1])
    print(name,lat,lon)
    a=[]
    a1=[]
    for i in range(len(name)):
        b=[]
        for j in range(len(name)):
            b.append(name[i]+name[j])
            if(name[j]==name[-1]):
                a.append(b)
                break
    print(a)
    for i in range(len(lat)):
        b1=[]
        for j in range(len(lat)):
            k=km(lat1=lat[i],lon1=lon[i],lat2=lat[j],lon2=lon[j])
            b1.append(k)
            if(j==len(lat)-1):
                a1.append(b1)
                break
    print(a1)

    r = range(len(a1))
    dist = {(i, j): a1[i][j] for i in r for j in r}
    print(tsp.tsp(r, dist))
    path=tsp.tsp(r, dist)
    path_length=path[0]+a1[len(name)-1][0]
    path_f=[path_length,path[1]]
    graph1(lat=lat,lon=lon,name=name)
    graph2(lat=lat,lon=lon,name=name,path=path)
    return path_f


def graph2(lat,lon,name,path):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(lat, lon)
    # n=['way-1','way-2','way-3','way-4']

    for i, txt in enumerate(name):
        ax.annotate(txt, (lat[i], lon[i]),fontsize=17)
    for i in range(len(path[1])):
        print(i)
        if(i!=len(path[1])-1):
            ax.plot([lat[int(path[1][i])],lat[int(path[1][i+1])]],[lon[int(path[1][i])],lon[int(path[1][i+1])]])
    #         ax.annotate(name[i]+name[i+1],
            a=lat[int(path[1][i])]+lat[int(path[1][i+1])]
            a=a/2
            b=lon[int(path[1][i])]+lon[int(path[1][i+1])]
            b=b/2
            k=km(lat1=lat[int(path[1][i])],lon1=lon[int(path[1][i])],lat2=lat[int(path[1][i+1])],lon2=lon[int(path[1][i+1])])
            plt.text(a,b,str(k)+'km',fontsize=10)
    #         mpld3.show()
    #         break
        else:
            ax.plot([lat[int(path[1][i])],lat[int(path[1][0])]],[lon[int(path[1][i])],lon[int(path[1][0])]])
            a=lat[int(path[1][i])]+lat[int(path[1][0])]
            a=a/2
            b=lon[int(path[1][i])]+lon[int(path[1][0])]
            b=b/2
            k=km(lat1=lat[int(path[1][i])],lon1=lon[int(path[1][i])],lat2=lat[int(path[1][0])],lon2=lon[int(path[1][0])])
            plt.text(a,b,str(k)+'km',fontsize=15)
    plt.title("The optimized route to collect garbage",fontsize=20)
    plt.xlabel("Latitude",fontsize=20)
    plt.ylabel("Longitude",fontsize=20)
    print('-----------------------')
    # l=lab(lat=lat,lon=lon)
    # tooltip=mpld3.plugins.PointLabelTooltip(ax, labels=l)
    # mpld3.plugins.connect(fig, tooltip)
    # mpld3.plugins.connect(fig,TopToolbar())
    mpld3.save_html(fig,'templates/fig2.html')

def start_point(data):
    api_token = 'oyq2afLK8q9KJG8yDiojI3gldjCBkkN0'
    tomtomgeo = 'https://api.tomtom.com/search/2/geocode/{}.json?countrySet=IN&lat=20.5937&lon=78.9629&key=oyq2afLK8q9KJG8yDiojI3gldjCBkkN0'.format(data)
    req = requests.get(tomtomgeo)
    req.status_code
    a=req.json()
    lat=a['results'][0]['position']['lat']
    lon=a['results'][0]['position']['lon']
    # print(lat,lon)
    start_ll=[lat,lon]
    print(start_ll)
    return start_ll


def graph1(lat,lon,name):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(lat, lon)
    for i, txt in enumerate(name):
        ax.annotate(txt, (lat[i], lon[i]),fontsize=17)
    for i in range(len(lat)):
        for j in range(len(lon)):
            ax.plot([lat[i],lat[j]],[lon[i],lon[j]])
            a=lat[i]+lat[j]
            b=lon[i]+lon[j]
            k=km(lat1=lat[i],lon1=lon[i],lat2=lat[j],lon2=lon[j])
            if(k!=0):
                plt.text(a/2,b/2,str(k)+'km',fontsize=20)
    plt.title("The possible routes to collect garbage",fontsize=15)
    plt.xlabel("Latitude",fontsize=20)
    plt.ylabel("Longitude",fontsize=20)
    print('-----------------------')
    # l=lab(lat=lat,lon=lon)
    # tooltip=mpld3.plugins.PointLabelTooltip(ax, labels=l)
    # mpld3.plugins.connect(fig, tooltip)
    # mpld3.plugins.connect(fig,TopToolbar())
    mpld3.save_html(fig,'templates/fig1.html')

