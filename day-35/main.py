import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweather.org/data/2.5/onecall"
api_key = "123123123"
account_sid = "asjdslajkfasdf"
auth_token = "ajsfdkljzxv"


weather_params = {
    "lat": 51.5,
    "lon": -0.12,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

print(response.json())
weather_data = response.json()



# for i in range(0,12): 
#     if response.json()["hourly"][i]["weather"][0]["id"] <= 800:
#         print("rain")

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")
        will_Rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = "It's going to rain today. Remember to bring an umbrella",
            from_= "+150123231",
            to = "+1823924213",
        )
    print(message.status)   



