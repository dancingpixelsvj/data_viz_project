import requests
import json

op('switch1').par.index = 0
# THIS PART CONVERTS A POSTCODE TO LON AND LAT
postcode = str(op('null_postcode')[0,0])
postcodes_url = 'http://api.postcodes.io/postcodes'
postcodes_parameters = {"q":postcode}

#get a response object with info about a postcode
postcode_response = requests.get(postcodes_url, params=postcodes_parameters)

postcode_response_status = postcode_response.status_code

#make a json object
postcode_info_json = json.loads(postcode_response.text)

#HANDLE POSTCODE ERRORS

#if response is successful read the result field
if postcode_response_status == 200:
	postcode_response_result = postcode_info_json['result']

	#if result field is null, postcode is not recognized by the api
	if not postcode_response_result:
		message = 'no info found, try a different postcode'

	#we assume that if result field is not null, it consists of at least one non empty array
	#we get lat and lon fields
	else:
		longitude = postcode_response_result[0]['longitude']
		latitude = postcode_response_result[0]['latitude']

		#if latitude and longitude fields are null try a different postcode
		if not latitude or not longitude:
			message = 'no info found, try a different postcode'

		else:
			admin_ward = postcode_response_result[0]['admin_ward']
			location_text = admin_ward if admin_ward else str(latitude) + ', ' + str(longitude)

			#THIS PART GETS AIR QUALITY INFO FOR GIVEN LON AND LAT
			airquality_url = 'https://api.erg.ic.ac.uk/AirQuality/Data/Nowcast/lat='+str(latitude)+'/lon='+str(longitude)+'/Json'

			#get a response object with info about a postcode
			airquality_response = requests.get(airquality_url)
			airquality_response_status = airquality_response.status_code


			#HANDLE AIR QUALITY STATUS ERRORS
			if airquality_response_status == 400:
				message = 'Bad request: ' + location_text + ' is probably not in London'
			elif airquality_response_status == 404:
				message = 'Page not found'
			elif airquality_response_status == 500:
				message = 'Server error'
			else:

				#dump text part of the request into a separate file
				op('text_data_dump').text = airquality_response.text

				# automatically run the parse script 1 frame later
				op('text_parse_script').run(delayFrames = 1)

				#for postcodes that map to multiple locations communicate that the first location will be used
				if len(postcode_response_result) > 1:
					message = 'Several locations found, giving results for the first one: ' + location_text

				elif len(postcode_response_result) == 1:
					message = 'Air quality in ' + location_text

else:
	postcode_response_error = postcode_info_json['error']
	message = postcode_response_error

#push status message to text dat
op('text_message').text = message