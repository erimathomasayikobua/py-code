class Wifi:
	def __init__(self, name, location, speed):
	    self.name = name
	    self.location = location
	    self.speed = speed

	def _display_info(self):
	    print(f"Name: {self.name}")
	    print(f"location: {self.location}")
	    print(f"speed: {self.name}")


Wifi_1 = Wifi("MTN WakaNet", "Bukoto", "100mbps")
Wifi_2 = Wifi("Rokespot", "Jinja Rd", "10mbps")
Wifi_3 = Wifi("Eduroam", "Uganda Christian University", "1000mbps")
Wifi_4 = Wifi("Liquid telecom", "Royal Palms Kampala", "100mbps")
Wifi_5 = Wifi("Simba Telecom", "High Court", "1000mbps")
Wifi_6 = Wifi("uganda Telecom", "URA", "1000mbps")

Wifi_1._display_info()
Wifi_2._display_info()
Wifi_3._display_info()
Wifi_4._display_info()
Wifi_5._display_info()
Wifi_6._display_info()