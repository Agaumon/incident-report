import os, time

def clear():
    time.sleep(.5)
    os.system('clear')

def create_report():
    clear()
    number_of_incidents = int(input("Number of incidents: "))
    clear()

    # Create empty list
    incidents = []

    # Loop through number of incidents to create an incident report for each
    for number in range(number_of_incidents):
        print(f'===== INCIDENT REPORT {number + 1} =====')
        print()

        # Inputs
        incident_type = input("Type: ")
        location = input("Location: ")
        severity = input("Severity: ")
        description = input("Description: ")

        # Create dictionary using inputs
        incident_report = {
            "incident": incident_type,
            "location": location,
            "severity": severity,
            "description": description
        }
        incidents.append(incident_report)
    clear()
    return incidents

def display_report(incidents, filtered_list, search):
    if search == True:
        for number, i in enumerate(filtered_list, start = 1):
            print(f'INCIDENT REPORT #{number}')
            print(f'Type: {i["incident"]}')
            print(f'Location: {i["location"]}')
            print(f'Severity: {i["severity"]}')
            print(f'Description: {i["description"]}')
            print()
    else:
        # Loop through each incident and print
        for number, i in enumerate(incidents, start = 1):
            print(f'INCIDENT REPORT #{number}')
            print(f'Type: {i["incident"]}')
            print(f'Location: {i["location"]}')
            print(f'Severity: {i["severity"]}')
            print(f'Description: {i["description"]}')
            print()

search = False

def search_report(incidents):
    ask_search = input('Would you like to search for specific incident(s)? ').lower()

    if ask_search == 'yes':
        search = True
        # Create empty list
        filter_list = []

        # Search filter query
        search_filter = input("Search filter: ").lower()

        # Search conditionals
        if search_filter == "incident type":
            key = "incident"
        elif search_filter == "location":
            key = "location"
        elif search_filter == "severity":
            key = "severity"
        else:
            print("Invalid search filter.")

        search_parameter = input(f'Enter {search_filter}: ').lower()
        
        for item in incidents:
            if search_parameter == item[key].lower():
                filter_list.append(item)
        clear()
        
        return filter_list, search
    else:
        clear()

def add_incident(incidents):
    incident_add = input("Would you like to add any additional incidents? ").lower()
    clear()

    # Loop conditionally
    while incident_add == "yes":
        # Create new report
        print(f'===== ADDITIONAL INCIDENT REPORT =====')
        incident_type = input("Type: ")
        location = input("Location: ")
        severity = input("Severity: ")
        description = input("Description: ")

        # Create dictionary using inputs
        incident_report = {
            "incident": incident_type,
            "location": location,
            "severity": severity,
            "description": description
        }
        clear()
        incident_add = input("Would you like to add any additional incidents? ").lower()
        clear()
        
        incidents.append(incident_report)




incidents = create_report()

add_incident(incidents)

filtered_list, search = search_report(incidents)

display_report(incidents, filtered_list, search)