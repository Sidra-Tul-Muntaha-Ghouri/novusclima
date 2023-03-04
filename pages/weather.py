import streamlit as st
import requests
import json


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"



#City One 
sity = st.text_input("Escribe la ciudad que deseas revisar su temperatura en este instante")
#CITY = "Bogota"
#API key 
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
# upadting the URL
#URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
#URL_london = "api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=146090ad17fa8843bc9eca97c53926b4"
URL1 = BASE_URL + "q=" + sity + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL1)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
  # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   st.write(f"{sity:-^30}")
   st.write(f"Temperature: {temperature}")
   st.write(f"Humidity: {humidity}")
   st.write(f"Pressure: {pressure}")
   st.write(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   st.write("Error in the HTTP request")

   
if sity: st.write('El pronóstico para las próximas semanas para ', sity, 'te lo regalamos con tu suscripción a Novus Clima ⛅')