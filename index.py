import os, time

def clear():
    time.sleep(.5)
    os.system('clear')

def create_report():
    number_of_incidents = int(input("Number of incidents: "))

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
    return incidents

def display_report(filter_list):
    # Loop through each incident and print
    for number, i in enumerate(filter_list, start = 1):
        print(f'INCIDENT REPORT #{number}')
        print(f'Type: {i["incident"]}')
        print(f'Location: {i["location"]}')
        print(f'Severity: {i["severity"]}')
        print(f'Description: {i["description"]}')
        print()

def search_report(incidents):
    # Create empty list
    filter_list = []
    search_filter = input("Search filter: ").lower()
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
    
    return filter_list


incidents = create_report()
clear()

filtered_list = search_report(incidents)

display_report(filtered_list)