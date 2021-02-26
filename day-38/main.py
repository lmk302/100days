# 

import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 63
HEIGHT_CM = 173
AGE = 34

APP_ID = "52d55efb"
API_KEY = "8b856f3cce9ad395b04b7b531659c1b8"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/960ebd6c241323be5829befe4bbde048/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    auth=(
        "mark", 
        "bnVsbDpudWxs",
        )
    )

    print(sheet_response.text)

    