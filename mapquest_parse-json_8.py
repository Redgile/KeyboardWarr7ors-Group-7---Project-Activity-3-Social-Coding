import urllib.parse
import requests
import PySimpleGUI as sg    # Install PySimpleGUi by typing the command:
                            # python3 -m pip install PySimpleGUI
# Ito po documentation niya: 
# https://www.pysimplegui.org/en/latest/call%20reference/
# Pa-help na lang po, thanks
# API Key
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rGUVl7RdGKEVUFAOmTYMkX1pAcfISqaZ"

#bg color
sg.theme("LightPurple")

layout = [

   
    [sg.Text('Get to your destination!')],
    [sg.Text('Starting Location:'), sg.InputText()],
    [sg.Text('Destination'), sg.InputText()],
    [sg.Submit("Start"), sg.Cancel()]

]

window = sg.Window('Direction', layout)
event, values = window.read()
url = main_api + urllib.parse.urlencode({"key":key, "from":values[0], "to":values[1]})
window.close()

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
     print("API Status: " + str(json_status) + " = A successful route call.\n")
     
     sg.popup( 

    
        "Directions from: " + values[0] + " to " + values[1],
        "Trip Duration: " + (json_data["route"]["formattedTime"]),
        "Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)),
        "Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)),
        title = "Travel Details"

        )  

elif json_status == 402:
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        
        sg.popup(
            
            "Invalid user inputs for one or both locations.",
            title = "ERROR"
            
            )

elif json_status == 611:
        print("Status Code: " + str(json_status) + "; NO INPUT FOR ONE OR TWO LOCATIONS")
        
        sg.popup(
            
            "NO INPUT FOR ONE OR TWO LOCATIONS",
            title = "ERROR"
            
            )

else:
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        
        sg.popup(

            "Staus Code: " + str(json_status),
            "Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes",
            title = "Something went wrong"

            )
