import urllib.parse
import requests
import PySimpleGUI as sg    # Install PySimpleGUi by typing the command:
                            # python3 -m pip install PySimpleGUI
# Ito po documentation niya: 
# https://www.pysimplegui.org/en/latest/call%20reference/
# Pa-help na lang po, thanks
# cath try 1
# API Key
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rGUVl7RdGKEVUFAOmTYMkX1pAcfISqaZ"

# Defining the content of the window
layout =    [[sg.Text("Starting Location: ")],
            [sg.Input(key='-INPUT1-')],
            [sg.Text("Destination: ")],
            [sg.Input(key='-INPUT2-')],
            [sg.Text(size=(80,1), key='-API STATUS-')],
            [sg.Text(size=(80,1), key='-BORDER-')],
            [sg.Text(size=(80,1), key='-LOCATIONS-')],
            [sg.Text(size=(80,1), key='-DURATION-')],
            [sg.Text(size=(80,1), key='-DISTANCEKM-')],
            [sg.Text(size=(80,1), key='-DISTANCEMI-')],
            [sg.Text(size=(80,1), key='-FUELLTR-')],
            [sg.Text(size=(80,1), key='-FUELGAL-')],
            [sg.Text(size=(80,1), key='-BORDER2-')],
            [sg.Text(size=(80,30), key='-ROUTE-')],
            [sg.Text(size=(80,1), key='-ERROR CODE: 402-')],
            [sg.Text(size=(80,1), key='-ERROR CODE: 611-')],
            [sg.Text(size=(80,1), key='-ERROR CODE: ETC1-')],
            [sg.Text(size=(80,1), key='-ERROR CODE: ETC2-')],
            [sg.Button('Start'), sg.Button('Reset'), sg.Button('Quit')]]

# Creating the window
window = sg.Window('KeyboardWarr7ors', layout)

# Displaying and interacting with the window
while True:
    event, values = window.read()

    # Checks if user wants to quit or if window was closed.
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Passes the input from the GUI to the variable to 
    # be used by the terminal output display.
    orig = values['-INPUT1-']
    # Exits the program if a user enters 'quit' or 'q' on the GUI.
    if orig == "quit" or orig == "q":
        break
    # Passes the input from the GUI to the variable to 
    # be used by the terminal output display.
    dest = values['-INPUT2-']
    # Exits the program if a user enters 'quit' or 'q' on the GUI.
    if dest == "quit" or dest == "q":
        break

    # Creates the curl to be used to retrieve the data from a website.
    url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("API Status: " + str(json_status) + " = A successful route class. \n")
        print ("==============================================")
        print ("Directions from " + (orig) + " to " + (dest))
        print ("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print ("Kilometers: " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print ("Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print ("==============================================")

        # Prints the output to the GUI.
        window['-API STATUS-'].update('API Status: ' + str(json_status) + " = A successful route class.")
        window['-BORDER-'].update('==============================================')
        window['-LOCATIONS-'].update('Directions from ' + values['-INPUT1-'] + ' to ' + values['-INPUT2-'])
        window['-DURATION-'].update("Trip Duration: " + (json_data["route"]["formattedTime"]))
        window['-DISTANCEKM-'].update("Distance (km): " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        window['-DISTANCEMI-'].update("Distance (mi): " + str ("{:.2f}".format((json_data["route"]["distance"]))))
        window['-FUELLTR-'].update("Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        window['-FUELGAL-'].update("Fuel Used (Gal): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"]))))
        window['-BORDER2-'].update('==============================================')

        # Prints the route to take to get to the destination from the starting location.
        route2 = " "
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print ((each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) "))
            route = (each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) ")
            route2 = (route2 + "\n" + route)
            window['-ROUTE-'].update(route2)
        print ("==============================================\n")
            

    elif json_status == 402:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        print ("**********************************************\n")

        # Prints the output to the GUI.
        window['-ERROR CODE: 402-'].update("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        
    elif json_status == 611:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        print ("**********************************************\n")

        # Prints the output to the GUI.
        window['-ERROR CODE: 611-'].update("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        
    else:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Refer to: ")
        print ("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print ("**********************************************\n") 

        # Prints the output to the GUI.
        window['-ERROR CODE: ETC1-'].update("Status Code: " + str (json_status) + "; Refer to: ")
        window['-ERROR CODE: ETC2-'].update("https://developer.mapquest.com/documentation/directions-api/status-codes")
          
window.close()

# Leave for reference purposes
#while True:
    #orig = input("Starting Location: ")
    #if orig == "quit" or orig == "q":
        #break
    #dest = input("Destination: ")
    #if dest == "quit" or dest == "q":
        #break
    #url = main_api + urllib.parse.urlencode ({"key":key, "from":orig, "to":dest})
    #print ("URL: " + (url))
    #json_data = requests.get(url).json()
    #json_status = json_data["info"]["statuscode"]
    #if json_status == 0:
        #print ("API Status: " + str(json_status) + " = A successful route class. \n")
        #print ("==============================================")
        #print ("Directions from " + (orig) + " to " + (dest))
        #print ("Trip Duration: " + (json_data["route"]["formattedTime"]))
        #print ("Kilometers: " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print ("Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        #print ("==============================================")
        #for each in json_data["route"]["legs"][0]["maneuvers"]:
            #print ((each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) "))
        #print ("==============================================\n")
    #elif json_status == 402:
        #print ("**********************************************")
        #print ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        #print ("**********************************************\n")
    #elif json_status == 611:
        #print ("**********************************************")
        #print ("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        #print ("**********************************************\n")
    #else:
        #print ("**********************************************")
        #print ("Status Code: " + str (json_status) + "; Refer to: ")
        #print ("https://developer.mapquest.com/documentation/directions-api/status-codes")
        #print ("**********************************************\n")

