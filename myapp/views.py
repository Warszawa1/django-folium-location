from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
import folium
import requests 
import json
import os
import twilio
from twilio.rest import Client



# Create your views here.
def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    lat = location_data['lat']
    lon = location_data['lon']
    city = location_data['city']
   
    if lat == None or lon == None:
        # address.delete()
        return HttpResponse('Your address is invalid')
    # #Create Map Object
    m = folium.Map(location=[lat, lon], zoom_start=2)
    
    folium.Marker([lat, lon], tooltip='Here I am', popup=city).add_to(m)
    # # Get HTML Representation of the Map Object
    m = m._repr_html_()
    context={
        'm': m,
        # 'form': form,
        'datalat': location_data['lat'],
        'datalon': location_data['lon'],
        'datacity': location_data['city'],
        'datacountry': location_data['country'],
    }

    return render(request, 'index.html', context)



def send_sms():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC489ed68069cbf0d82f44e9c035201b8f'
    auth_token = '43f246fa138fb72fbf801c698be2002e'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Trying this twilio stuff, hope you get this sms 📍",
                        from_='+34633409911',
                        to=['+34633409911']
                 )

    print(message.sid)

    # return render(request, 'index.html', context=message)
     
# send_sms()

def run_function():
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    lat = location_data['lat']
    lon = location_data['lon']
    result = location_data['city']

    message_body = lat, lon, result
    

    return result

run_function()

def button_click_view(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/' + ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    lat = location_data['lat']
    lon = location_data['lon']
    city = location_data['city']
    # Your view logic here
    message = f"Button Clicked! your city is {city}"
    return render(request, 'about.html', {'message':message})

    
