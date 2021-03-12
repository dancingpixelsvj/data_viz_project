#parsing json data structure of the type https://api.erg.ic.ac.uk/AirQuality/Data/Nowcast/lat=51.510357/lon=-0.116773/Json
import json

# grab the response text
airquality_info = op('text_data_dump').text

# make a json object out of the text part of the request
airquality_info_json = json.loads(airquality_info)

#clear table data
op('table_point_data').clear(keepFirstRow=True)

#populate data table with each pollutant name, its annual concentration,
#its current concentration and its concentration level
pollutants = ['NO2', 'O3', 'PM10', 'PM25']

for i in pollutants:
	pollutant_current = airquality_info_json['PointResult']['@'+i]
	pollutant_index = airquality_info_json['PointResult']['@'+i+'_Index']
	pollutant_annual = airquality_info_json['PointResult']['@'+i+'_Annual']
	op('table_point_data').appendRow([i, pollutant_annual, pollutant_current, pollutant_index])

#switch to populated data table
#parse script will not be run if air quality request was not successful
#in which case the switch will remain pointing to the empty data table as set in the fetch script
op('switch_data_no_data').par.index = 1
