import urllib.parse
import requests
import PySimpleGUI as sg    # Install PySimpleGUi by typing the command:
                            # python3 -m pip install PySimpleGUI

# API Key
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rGUVl7RdGKEVUFAOmTYMkX1pAcfISqaZ"

# Defining the content of the window
layout =    [[sg.Text("Starting Location: ")],
            [sg.Input(key='-INPUT1-')],
            [sg.Text("Destination: ")],
            [sg.Input(key='-INPUT2-')],
            [sg.Text(size=(80,1), key='-ORIGIN-')],
            [sg.Text(size=(80,1), key='-DESTINATION-')],
            [sg.Button('Start'), sg.Button('Quit')]]



# Creating the window
window = sg.Window('EZAW', layout)

# Displaying and interacting with the window
while True:
    event, values = window.read()
    # Checks if user wants to quit or if window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Outputs the result on the window
    window['-ORIGIN-'].update(values['-INPUT1-'])
    window['-DESTINATION-'].update(values['-INPUT2-'])
    # Passing values
    orig = values['-INPUT1-']
    #if orig == "quit" or orig == "q":
        #break
    dest = values['-INPUT2-']
    #if dest == "quit" or dest == "q":
        #break
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print ("API Status: " + str(json_status) + " = A successful route class. \n")
        print ("==============================================")
        print ("Directions from " + (orig) + " to " + (dest))
        print ("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print ("Kilometers: " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print ("Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print ("==============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print ((each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) "))
        print ("==============================================\n")
    elif json_status == 402:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        print ("**********************************************\n")
    elif json_status == 611:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        print ("**********************************************\n")
    else:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Refer to: ")
        print ("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print ("**********************************************\n")   


window.close()

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    print ("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print ("API Status: " + str(json_status) + " = A successful route class. \n")
        print ("==============================================")
        print ("Directions from " + (orig) + " to " + (dest))
        print ("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print ("Kilometers: " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print ("Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print ("==============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print ((each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) "))
        print ("==============================================\n")
    elif json_status == 402:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        print ("**********************************************\n")
    elif json_status == 611:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        print ("**********************************************\n")
    else:
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Refer to: ")
        print ("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print ("**********************************************\n")

