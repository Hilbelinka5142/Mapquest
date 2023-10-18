import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"

dest = "Baltimore, Md"
key = "fjc5tKjwiUxqW8Q9pFKodCjtbhop5j9s"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Miles: " + str(json_data["route"]["distance"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
             print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

def get_current_location():
    try:
        # Usibg a service like ipinfo.io to get the user's IP address
        response = requests.get('https://ipinfo.io')
        data = response.json()
        ip = data['ip']

        
        url = f'https://api.opencagedata.com/geocode/v1/json?q={ip}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        if data['status']['code'] == 200:
            location = data['results'][0]
            print(f"Your current location is: {location['formatted']}")
        else:
            print(f"Error: {data['status']['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_current_location()



