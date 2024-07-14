import csv
from statistics import mean

def main():
    # Define the path to the CSV file
    file_path = 'C:/Users/braisonW/Desktop/G/assigment#6/lawEnforcement.csv'
    
    # Prompt the user to enter a state abbreviation and convert it to uppercase
    state_abbr = input("Enter state abbreviation: ").upper()

    # Initialize a list to store incidents for the specified state
    incidents = []

    # Open the CSV file for reading
    with open(file_path, 'r') as file:
        # Create a DictReader to read the CSV file into a dictionary
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the 'state' field matches the user-specified state abbreviation
            if row['state'] == state_abbr:
                # Add the row to the incidents list
                incidents.append(row)

    # Check if no incidents were found for the specified state
    if not incidents:
        print(f"No incidents found for state: {state_abbr}")
        return

    # Initialize variables to store ages, female and male perpetrator counts, and gun counts
    ages = []
    female_count = 0
    male_count = 0
    gun_count = 0

    # Print the header for the output
    print(f"\n{'date':<12} {'age':<5} {'weapon':<20} {'gender':<10}")
    
    # Iterate over each incident in the incidents list
    for incident in incidents:
        # Extract and store relevant fields from the incident
        date = incident['date']
        age = int(incident['age'])
        weapon = incident['weapon']
        gender = incident['gender']

        # Print the incident details in a formatted manner
        print(f"{date:<12} {age:<5} {weapon:<20} {gender:<10}")

        # Add the age to the ages list
        ages.append(age)
        
        # Count the number of female perpetrators
        if gender == 'F':
            female_count += 1
        # Count the number of male perpetrators
        elif gender == 'M':
            male_count += 1
        
        # Count the number of incidents involving guns
        if weapon.lower() == 'gun':
            gun_count += 1

    # Calculate the average age of perpetrators
    average_age = mean(ages)

    # Print the summary statistics
    print(f"\nAverage age of perpetrators in {state_abbr}: {average_age:.2f}")
    print(f"Number of female perpetrators in {state_abbr}: {female_count}")
    print(f"Number of male perpetrators in {state_abbr}: {male_count}")
    print(f"Number of perpetrators armed with guns in {state_abbr}: {gun_count}")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
