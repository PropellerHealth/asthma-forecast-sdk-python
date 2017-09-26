# asthma-forecast

A module for interfacing with Propeller Health's Asthma Forecasting service.

## Examples

```python
import forecast

fc = forecast.Client()

print("Get forecast by zipcode")
results = fc.getForecastByZipCode("53711")
print("\t" + results['properties']['code'] + "(" + str(results['properties']['value']) + ")")

print("Get forecast by lat/lng")
results = fc.getForecastByLatLong(43.13986,-89.3375)
print("\t" + results['properties']['code'] + "(" + str(results['properties']['value']) + ")")

