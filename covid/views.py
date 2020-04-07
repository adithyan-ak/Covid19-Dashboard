from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
from bs4 import BeautifulSoup

def index(request):
  
  response = requests.get('https://api.covid19india.org/data.json')

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


  # Daily cases chart

  daily_cases = resp['cases_time_series']
  tot_length = len(daily_cases)

  today_case = int(resp['statewise'][0]['deltaconfirmed'])

  sterday_confirmed = int(daily_cases[tot_length-1]['dailyconfirmed'])

  sterday1_confirmed = int(daily_cases[tot_length-2]['dailyconfirmed'])

  sterday2_confirmed = int(daily_cases[tot_length-3]['dailyconfirmed'])

  sterday3_confirmed = int(daily_cases[tot_length-4]['dailyconfirmed'])

  sterday4_confirmed = int(daily_cases[tot_length-5]['dailyconfirmed'])

# Time calculation 

  tdy = datetime.datetime.today()
  today = (tdy.strftime("%d")+' '+(tdy.strftime("%B")))

  ster = datetime.datetime.today() - datetime.timedelta(days=1)
  yesterday = (ster.strftime("%d")+' '+(ster.strftime("%B")))

  ster1 = datetime.datetime.today() - datetime.timedelta(days=2)
  yesterday1 = (ster1.strftime("%d")+' '+(ster1.strftime("%B")))

  ster2 = datetime.datetime.today() - datetime.timedelta(days=3)
  yesterday2 = (ster2.strftime("%d")+' '+(ster2.strftime("%B")))

  ster3 = datetime.datetime.today() - datetime.timedelta(days=4)
  yesterday3 = (ster3.strftime("%d")+' '+(ster3.strftime("%B")))

  ster4 = datetime.datetime.today() - datetime.timedelta(days=5)
  yesterday4 = (ster4.strftime("%d")+' '+(ster4.strftime("%B")))


  # Tamilnadu district wise

  districtwise = requests.get('https://api.covid19india.org/state_district_wise.json')

  districtwise = districtwise.json()

  tn_districts = districtwise['Tamil Nadu']['districtData']
  
  tot_districts = len(tn_districts)
  t=tn_districts
  key=0
  final={}
  ar=list(t.keys())
  temp=0
  while(len(list(t.keys()))!=0):
	  key=0
	  ar=list(t.keys())
	  temp=0
	  for i in range(len(ar)-1):
		  for j in range(i+1,len(ar)):
			  #print(t[ar[i]]['confirmed'])
			  if t[ar[i]]['confirmed']>temp:
				  temp=t[ar[i]]['confirmed']
				  key=i
	  final[ar[key]]=t[ar[key]]
	  del t[ar[key]]
	
  tn_districts=final

  return render(request, 'index.html',{'total_india':total_india,'active_india':active_india,'recovered_india':recovered_india,'dead_india':dead_india,'updated_time_india':updated_time_india, 'total_tamilnadu':total_tamilnadu,'active_tamilnadu':active_tamilnadu,'recovered_tamilnadu':recovered_tamilnadu,'dead_tamilnadu':dead_tamilnadu, 'total_world':total_world, 'world_active_cases':world_active_cases, 'total_world_death':total_world_death,'total_world_recovered':total_world_recovered,'today':today,'yesterday':yesterday,'yesterday1':yesterday1,'yesterday2':yesterday2,'yesterday3':yesterday3,'yesterday4':yesterday4,'today_case':today_case,'sterday_confirmed':sterday_confirmed,'sterday1_confirmed':sterday1_confirmed,'sterday2_confirmed':sterday2_confirmed,'sterday3_confirmed':sterday3_confirmed,'sterday4_confirmed':sterday4_confirmed,'tn_districts':tn_districts,'tot_districts':tot_districts})

