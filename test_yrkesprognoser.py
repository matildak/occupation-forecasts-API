#!/usr/bin/python3

import requests

rootUrl = 'http://api.arbetsformedlingen.se:80/af/v2/'

apiVersionReq = requests.get(rootUrl + 'forecasts/version')
forecastsListReq = requests.get(rootUrl + 'forecasts/occupationalArea/forcastsRefs/list')

#Check tjat its alive and no change
def test_apiVersion():
    assert apiVersionReq.status_code == 200
    assert apiVersionReq.text == '1.0.70'


#Get any OccupationalAreaId and return json object
def getOccupationalAreaId(id):
    return requests.get(rootUrl + 'forecasts/occupationalArea/forcastsRefs/list/' + str(id))


#Verify first object in list
def test_occupationalAreaId():
    occupationalAreaIdList = []
    occupationalAreaIdObj = getOccupationalAreaId(5).json()
    for element in occupationalAreaIdObj[0]['occupationPrognosisRefs']: #use to improve test
            occupationalAreaIdList.append(element)
    assert occupationalAreaIdObj[0]['occupationPrognosisRefs'][0]['heading'] == 'Marknadsanalytiker och marknadsförare'
    assert (occupationalAreaIdList[0]['heading']) == 'Marknadsanalytiker och marknadsförare' #same but make more tests

