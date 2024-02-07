import requests

city = input("Saisissez la ville pour laquelle vous souhaitez voir la météo?\n")

response = requests.get("http://api.weatherapi.com/v1/current.json?key=26862aeb8fa3453ba07151949240202&q="+city+"&aqi=no")

json = response.json()

forcastDay = json.get("current")
temperature = forcastDay.get("temp_c")
cuurent_weather = forcastDay.get("condition").get("text")

print("Météo du moment est ", cuurent_weather, " et la température est de ", temperature, "°C", sep='')