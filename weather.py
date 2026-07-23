import requests

def get_recent_floods():
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    
    params = {
        "category": "floods",
        "limit": 5,
        "status": "open"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        events = data.get('events', [])
        
        if not events:
            print("No active flood events found at the moment.")
            return

        print(f"--- Latest {len(events)} Flood Events ---")

        for event in events:
            title = event.get('title', 'N/A')
            geometry = event.get('geometry', [])

            if not geometry:
                print(f"\n📍 Event: {title}")
                print("   No location data.")
                continue

            date = geometry[0].get('date', 'N/A')
            coords = geometry[0].get('coordinates', [])

            print(f"\n📍 Event: {title}")
            print(f"   Date: {date}")

            if isinstance(coords[0], list):
                print("   Location: Area (polygon)")
            else:
                print(f"   Location: Lon {coords[0]}, Lat {coords[1]}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_recent_floods()