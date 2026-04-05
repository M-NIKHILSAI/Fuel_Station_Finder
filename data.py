import math
import uuid

# Initial mock data centered roughly around New Delhi, India
mock_stations = [
    {
        "id": str(uuid.uuid4()),
        "name": "Indian Oil Petrol Pump",
        "lat": 28.6315,
        "lng": 77.2167,
        "petrol_price": 118.50,
        "diesel_price": 113.40,
        "available": True,
        "wait_time": 5,
        "address": "Connaught Place, New Delhi 110001",
        "hours": "24 Hours",
        "amenities": ["Convenience Store", "ATM", "Air/Water"]
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Bharat Petroleum",
        "lat": 28.6139,
        "lng": 77.2090,
        "petrol_price": 112.40,
        "diesel_price": 107.50,
        "available": True,
        "wait_time": 2,
        "address": "Sansad Marg, New Delhi 110001",
        "hours": "6:00 AM - 11:00 PM",
        "amenities": ["Car Wash", "Mechanic"]
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Hindustan Petroleum (HP)",
        "lat": 28.6448,
        "lng": 77.2167,
        "petrol_price": 119.80,
        "diesel_price": 114.90,
        "available": True,
        "wait_time": 15,
        "address": "Paharganj, New Delhi 110055",
        "hours": "24 Hours",
        "amenities": ["Toilets", "Hot Food", "ATM"]
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Reliance Petroleum",
        "lat": 28.5921,
        "lng": 77.2250,
        "petrol_price": 113.90,
        "diesel_price": 108.90,
        "available": False,
        "wait_time": 0,
        "address": "Lodhi Colony, New Delhi 110003",
        "hours": "7:00 AM - 10:00 PM",
        "amenities": ["Convenience Store"]
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Nayara Energy",
        "lat": 28.6505,
        "lng": 77.2303,
        "petrol_price": 116.50,
        "diesel_price": 111.40,
        "available": True,
        "wait_time": 8,
        "address": "Chandni Chowk, New Delhi 110006",
        "hours": "24 Hours",
        "amenities": ["Air/Water", "Deli"]
    },
    {
        "id": str(uuid.uuid4()),
        "name": "Indian Oil (COCO)",
        "lat": 28.5800,
        "lng": 77.2000,
        "petrol_price": 111.10,
        "diesel_price": 106.10,
        "available": True,
        "wait_time": 3,
        "address": "Safdarjung Enclave, New Delhi 110029",
        "hours": "5:00 AM - 12:00 AM",
        "amenities": ["Car Wash", "ATM", "Coffee"]
    }
]

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r

def get_nearby_stations(user_lat, user_lng, max_radius_km=10.0, sort_by="distance", filter_by="all"):
    results = []
    for station in mock_stations:
        dist = haversine(user_lat, user_lng, station["lat"], station["lng"])
        if dist <= max_radius_km:
            station_data = station.copy()
            station_data["distance"] = round(dist, 2)
            results.append(station_data)
            
    # Apply filtering
    if filter_by == "available":
        results = [s for s in results if s["available"]]
    elif filter_by == "cheap":
        results = [s for s in results if s["petrol_price"] <= 114.0]

    # Apply sorting
    if sort_by == "price":
        results.sort(key=lambda x: x["petrol_price"])
    elif sort_by == "wait_time":
        results.sort(key=lambda x: x["wait_time"])
    else: # default to distance
        results.sort(key=lambda x: x["distance"])
        
    return results
