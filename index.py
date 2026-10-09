import os, time

def clear():
    time.sleep(.5)
    os.system('clear')

clear()

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

clear()

def display_report(incidents):
    for number, i in enumerate(incidents):
        print(f'INCIDENT REPORT #{number+1}')
        print(f'Type: {i["incident"]}')
        print(f'Location: {i["location"]}')
        print(f'Severity: {i["severity"]}')
        print(f'Description: {i["description"]}')
        print()

incidents = create_report()
clear()
display_report(incidents)