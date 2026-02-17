#This code is a simple travel planner that uses the SearchAPI.io to find flights and hotels.
#It defines two agents: one for searching flights and another for searching hotels.
#Use multi agents patterns.

import requests

SEARCHAPI_KEY="Your API key here."
class GoogleFlightsAgent:
    def search_flights(self, origin, destination, departure_date, return_date=None):
        url = "https://www.searchapi.io/api/v1/search"
        params = {"engine":"google_flights","flight_type":"round_trip", "departure_id":origin, "arrival_id":destination, "outbound_date": departure_date, "return_date": return_date, "api_key": SEARCHAPI_KEY}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            date = response.json()
            try:
                flight = date["best_flights"][0]
                info = flight["flights"][0]
                airline = info["airline"]
                departure_airport = info["departure_airport"]["name"]
                arrival_airport = info["arrival_airport"]["name"]
                return f"Flight: {airline} from {departure_airport} to {arrival_airport} at {flight["price"]}"
            except:
                return "No flights found."
        return "Flight search failed."
    

class GoogleHotelsAgent:
    def search_hotels(self, city, departure_date, return_date):
        url = "https://www.searchapi.io/api/v1/search"
        city = "Mumbai"
        params = {"engine": "google_hotels", "q": f"hotels in {city}", "check_in_date": departure_date, "check_out_date": return_date, "api_key": SEARCHAPI_KEY}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            date = response.json()
            hotel = date["properties"][0]
            try:
                hotel = date["properties"][0]
                return f"Hotel: {hotel["name"]} at {hotel["city"]} - {hotel["price_per_night"]["price"]} per night"
            except:
                return "No hotels found."
        return "Hotel serach failed."
    

class TripPlannerAgent:
    def __init__(self, origin, destination, departure_date, return_date=None):
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.flight_agent = GoogleFlightsAgent()
        self.hotel_agent = GoogleHotelsAgent()


        
            
