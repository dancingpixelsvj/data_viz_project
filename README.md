## London Air Quality Visualizer
![Screenshot](https://raw.githubusercontent.com/dancingpixelsvj/data_viz_project/master/assets/screenshot.png)


This TouchDesigner project renders a GUI where the user can input a London postcode. It then sends get requests to http://api.postcodes.io/postcodes and https://api.erg.ic.ac.uk/AirQuality endpoints for the information about the air quality at this location. The JSON response is then processed to extract data on the concentration of polluting particles, which is then mapped to a 3D particle system, while the particle levels are displayed as a textual overlay. The patch handles various request errors and displays to the user how the postcode query should be amended. It updates the information every time the user inputs a new postcode but the patch can easily be supplied with a timer to fetch new data every second or at whatever interval the info at  https://api.erg.ic.ac.uk/AirQuality is updated.
