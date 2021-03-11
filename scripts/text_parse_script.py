import json

# grab the response text
airquality_info = op('text_data_dump').text

# make a json object out of the text part of the request
airquality_info_json = json.loads(airquality_info)

#clear table data
op('table_point_data').clear(keepFirstRow=True)

# get longitude of the first result returned for the postcode
no2_current = airquality_info_json['PointResult']['@NO2']
no2_index = airquality_info_json['PointResult']['@NO2_Index']
no2_annual = airquality_info_json['PointResult']['@NO2_Annual']
op('table_point_data').appendRow(['NO2', no2_annual, no2_current, no2_index])

o3_current = airquality_info_json['PointResult']['@O3']
o3_index = airquality_info_json['PointResult']['@O3_Index']
o3_annual = airquality_info_json['PointResult']['@O3_Annual']
op('table_point_data').appendRow(['O3', o3_annual, o3_current, o3_index])

pm10_current = airquality_info_json['PointResult']['@PM10']
pm10_index = airquality_info_json['PointResult']['@PM10_Index']
pm10_annual = airquality_info_json['PointResult']['@PM10_Annual']
op('table_point_data').appendRow(['PM10', pm10_annual, pm10_current, pm10_index])

pm25_current = airquality_info_json['PointResult']['@PM25']
pm25_index = airquality_info_json['PointResult']['@PM25_Index']
pm25_annual = airquality_info_json['PointResult']['@PM25_Annual']
op('table_point_data').appendRow(['PM25', pm25_annual, pm25_current, pm25_index])

op('switch1').par.index = 1
