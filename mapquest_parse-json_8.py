import urllib.parse
import requests
import PySimpleGUI as sg    # Install PySimpleGUi by typing the command:
                            # python3 -m pip install PySimpleGUI
# Ito po documentation niya: 
# https://www.pysimplegui.org/en/latest/call%20reference/
# Pa-help na lang po, thanks
# cath try 1
#sample branch
# API Key
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rGUVl7RdGKEVUFAOmTYMkX1pAcfISqaZ"

sg.theme("LightPurple")

# Defining the content of the window
layout =    [[sg.Text("Starting Location: ")],
            [sg.Input(key='-INPUT1-')],
            [sg.Text("Destination: ")],
            [sg.Input(key='-INPUT2-')],
            [sg.Button('Start'), sg.Button('Quit')]]

# Creating the window
window = sg.Window('KeyboardWarr7ors', layout)

sg.theme("LightPurple")

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

        route2 = " "
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print ((each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) "))
            route = (each["narrative"]) + " (" + str ("{:.2f}".format ((each["distance"])*1.61) + " km) ")
            route2 = (route2 + "\n" + route)
        print ("==============================================\n")

        # Prints the output to the GUI.
        sg.popup (
            'API Status: ' + str(json_status) + " = A successful route class.",
            '==============================================',
            'Directions from ' + values['-INPUT1-'] + ' to ' + values['-INPUT2-'],
            "Trip Duration: " + (json_data["route"]["formattedTime"]),
            "Distance (km): " + str ("{:.2f}".format((json_data["route"]["distance"])*1.61)),
            "Distance (mi): " + str ("{:.2f}".format((json_data["route"]["distance"]))),
            "Fuel Used (Ltr): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)),
            "Fuel Used (Gal): " + str ("{:.2f}".format((json_data["route"]["fuelUsed"]))),
            '==============================================',
            # Prints the route to take to get to the destination from the starting location.
            route2,
            "==============================================",
            title = 'Travel Details'
        )
        
    elif json_status == 402:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.")
        print ("**********************************************\n")

        # Prints the output to the GUI.
        sg.popup ("Status Code: " + str (json_status) + "; Invalid user inputs for one or both locations.",
        title = "Error Code: 402")
        
    elif json_status == 611:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.")
        print ("**********************************************\n")

        # Prints the output to the GUI.
        sg.popup("Status Code: " + str (json_status) + "; Missing an entry for one or both locations.",
        title = "Error Code: 611")
        
    else:
        # Prints the output to the terminal.
        # Used for debugging purposes.
        print ("**********************************************")
        print ("Status Code: " + str (json_status) + "; Refer to: ")
        print ("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print ("**********************************************\n") 

        # Prints the output to the GUI.
        sg.popup("Status Code: " + str (json_status) + "; Refer to: ",
        "https://developer.mapquest.com/documentation/directions-api/status-codes",
        title = 'An Error Has Occured')
          
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

