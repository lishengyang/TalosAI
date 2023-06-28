import subprocess
import datetime

# Set the city name
city_name = "Beijing,China"

# Use inxi to retrieve the weather information for the city
weather_info = subprocess.check_output(["inxi", "-W", city_name]).decode("utf-8")

# Extract the temperature and weather condition from the output
temperature = weather_info.split("temperature: ")[1].split(" C")[0]
condition = weather_info.split("conditions: ")[1].split()[0] + " " + weather_info.split("conditions: ")[1].split()[1]

# Print the weather information on the terminal
print("user@raspberrypi:~/home $ inxi -W " + city_name)
print("Weather Report: temperature: " + temperature + " C conditions: " + condition)
print("Locale: current time: " + datetime.datetime.now().strftime("%a %d %b %Y %H:%M:%S"))

