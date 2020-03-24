from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup

def index(request):
  
  response = requests.get('https://api.covid19india.org/data.json')

  resp = response.json()

 # India count

  statewise = resp['statewise']

  india = statewise[0]

  total_india = india['confirmed']

  active_india = india['active']

  recovered_india = india['recovered']

  dead_india = india['deaths']

  updated_time_india = india['lastupdatedtime']

  #Tamilnadu count

  i=0
  ind = ''
  for k in statewise:
      if k['state'] == 'Tamil Nadu':
          ind = i
      i = i + 1

  tamilnadu = statewise[ind]

  total_tamilnadu = tamilnadu['confirmed']

  active_tamilnadu = tamilnadu['active']

  recovered_tamilnadu = tamilnadu['recovered']

  dead_tamilnadu = tamilnadu['deaths']
 
 #world count
  
  world_response = requests.get('https://www.worldometers.info/coronavirus/')


  worldsoup = BeautifulSoup(world_response.content, 'html.parser')

  mydivs = worldsoup.findAll("div", {"class": "maincounter-number"})

  total_world = mydivs[0].text
  total_world_death = mydivs[1].text
  total_world_recovered = mydivs[2].text

  world_active = worldsoup.findAll("div", {"class": "number-table-main"})

  world_active_cases = world_active[0].text

  return render(request, 'index.html', {'total_india':total_india,'active_india':active_india,'recovered_india':recovered_india,'dead_india':dead_india,'updated_time_india':updated_time_india, 'total_tamilnadu':total_tamilnadu,'active_tamilnadu':active_tamilnadu,'recovered_tamilnadu':recovered_tamilnadu,'dead_tamilnadu':dead_tamilnadu, 'total_world':total_world, 'world_active_cases':world_active_cases, 'total_world_death':total_world_death,'total_world_recovered':total_world_recovered})


