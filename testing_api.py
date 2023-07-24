import requests 

query = "New York"
api_key = '7984d743b5094cd6e05a6650b8585015'
params = {"q": query, "appid" : api_key,"units": "metric"}
weather_response = requests.get('https://api.openweathermap.org/data/2.5/weather', params = params)
print(weather_response.status_code)
data = weather_response.json()
print(data)
print (data['main']['temp'])