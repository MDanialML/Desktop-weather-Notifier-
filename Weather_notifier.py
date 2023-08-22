# Requaired libraries
# beautiful soap is used to extracte requaired data from html and xml file
from bs4 import BeautifulSoup
# this library is used to show desktop notifications
from win10toast import ToastNotifier
import requests  # request are used to send http request

# creating an object from ToastNotifier class
t_obj = ToastNotifier()

# Function to get data from given url


def get_data(url):
    data = requests.get(url)
    return data.text


# now passing url to get_data function to get html data
html_data = get_data(
    "https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())
'''
# list_html_data = soup.split(',')
print(type(soup))
html_data = soup.prettify()
print(type(html_data))
list_html_data = html_data.split(',')
print(type(list_html_data))
with open('weather_scrapped.text', 'w') as file:
    for x in list_html_data:
        file.writelines(x)
'''
# finding the requaired details and filter them
current_teprature = soup.find_all(
    "span", class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chance_of_rain = soup.find_all(
    "div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = str(current_teprature)
temp_rain = str(chance_of_rain)
# print(temp)
# print(temp_rain)
results = "Current_Temprature : " + \
    temp[128:-9] + "Chance of Rain : " + temp_rain[131:-14]
# print(results)
# now pass the result into notification object
t_obj.show_toast("Weathen Update : ", results, duration=10)
