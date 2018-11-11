#!/usr/bin/python3

import requests


rootUrl = 'http://api.arbetsformedlingen.se:80/af/v2/'

apiVersionReq = requests.get(rootUrl + 'forecasts/version')
forecastsListReq = requests.get(rootUrl + 'forecasts/occupationalArea/forcastsRefs/list')
occupationalAreaIdReq = requests.get(rootUrl + 'forecasts/occupationalArea/forcastsRefs/list/5')


#Version
print(apiVersionReq.status_code)
print(apiVersionReq.text)
print(apiVersionReq.headers)
print(apiVersionReq.history)

#list with forecasts
forecastsList = forecastsListReq.json()
print(forecastsList)

#get forecast with occupationalAreaId 5
