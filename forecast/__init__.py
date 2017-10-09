# coding=utf-8
import urllib.request
import json


class Client(object):
    """ A client for accessing Propeller Health's Asthma Forecasting Service """

    def __init__(self):
        """
        Initializes the Forecasting Client

        :returns: Forecasting Client
        :rtype: forecast.Client
        """

        self._api_endpoint = "https://open.propellerhealth.com/prod/forecast"

    def __httpGet(self,uri):
        url = self._api_endpoint + uri
        request = urllib.request.Request(url=url,headers={"User-Agent" : "asthma-forecast-sdk-python"},method="GET")
        result = urllib.request.urlopen(request,timeout=60).read()
        return json.loads(result)

    def getForecastByZipCode(self, zip):
        return self.__httpGet("?postalCode=" + zip)

    def getForecastByLatLong(self, lat, lon):
        return self.__httpGet("?latitude="+str(lat)+"&longitude="+str(lon))

# end Client
