def Menu_Screen():
    # MENU SCREEN - Displayed when System Launches
    print("")
    print("")
    print("Type ADD for adding driver details")
    print("Type DDD for deleting")
    print("Type UDD for updating driver details")
    print("Type VCT for viewing the rally cross standings table")
    print("Type SRR for simulating a random race")
    print("Type VRL for viewing race table sorted according to the date")
    print("Type STF to save the current data to a text file")
    print("Type RFF to load data from the saved text file")
    print("Type ESC to exit the program")
    print("")

    selected_option = input(">> Function:  ").upper().strip()
    # '.upper()' to minimise errors regarding CASE SENSITIVE
    # '.strip()' is used to remove WHITE SPACES in the input

    if selected_option == "ADD":
        ADD_Function()
    elif selected_option == "DDD":
        DDD_Function()
    elif selected_option == "UDD":
        UDD_Function()
    elif selected_option == "VCT":
        VCT_Function()
    elif selected_option == "SRR":
        SRR_Function()
    elif selected_option == "VRL":
        print("VRL Works")
    elif selected_option == "STF":
        print("STF Works")
    elif selected_option == "RFF":
        print("RFF")
    elif selected_option == "ESC":
        print("Exiting Program..")
    else:
        print("WARNING - Wrong Input")
        print("ENTER the abbreviation for the required function.")

    return selected_option
def ADD_Function():
    #global record_exsisting
    print("ADD Function..")
    print("")
    while True:
        try:
            new_player_name = input("Enter Name: ").title()
            new_player_age = int(input("Enter Age: "))
            new_player_team = input("Enter Team: ").title()
            new_player_car = input("Enter Car: ").title()
            new_player_current_points = int(input("Enter Current Points: "))
            championship_data_file = open("championship_data.txt", "r+")   #opens file for read and write at the same time
            line_in_championship_data = championship_data_file.readline()
        except ValueError:
            print("WARNING - Please enter a number")
            print("")
            continue
        except FileNotFoundError:
            print("WARNING - File not found")
            print("")
            continue
        # IF Empty Document Headers are being assigned
        if line_in_championship_data == "":
            header_championship_data = '{:<22} {:<12} {:<22} {:<18} {:<12}\n'.format("NAME","AGE","TEAM","CAR","POINTS")
            championship_data_file.write(header_championship_data)
            championship_data_file.close()

        championship_data_file = open("championship_data.txt", "r+") #re - reads the file after Headers are being assigned
        line_in_championship_data = championship_data_file.readline()
        record_exsisting=False
        while line_in_championship_data != "":
            stored_data = line_in_championship_data.strip().split()    #takes in the stored record, removes white space and other formatting characters
            stored_first_name = stored_data[0]
            stored_last_name = stored_data[1] #checks whether there are drivers with same name(compares with first and last names for accuracy)
            new_name = new_player_name.strip().split()
            new_player_first_name = new_name[0]
            new_player_last_name = new_name[1]
            if (new_player_first_name == stored_first_name) and (new_player_last_name == stored_last_name):#Checks for Duplication of records - assumes no driver CAN HAVE SAME NAMES!
                record_exsisting = True
                print("'{}' Exists already".format(new_player_name))
                print("Invalid Input") #tells the user that records are being duplicated
                break
            line_in_championship_data = championship_data_file.readline() #Continues till then EOF

        if record_exsisting == False: # Skips the first line of the document-Header
            new_records = '{:<22} {:<12} {:<22} {:<18} {:<12}\n'.format(new_player_name, new_player_age, new_player_team, new_player_car,new_player_current_points)
            championship_data_file.write(new_records)#Once validated new record is entered in to the Championship table
            print("{}  has been added..".format(new_player_name))
        championship_data_file.close()
        break
def DDD_Function():
    print("Delete Function")
    print("")
    name_to_be_deleted = input("Enter the Name To be deleted: ").title()
    delete_name = name_to_be_deleted.strip().split()
    delete_firstname = delete_name[0]
    delete_lastname = delete_name[1]
    with open("championship_data.txt") as file :  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()
        found = False

        for records in range(len(lines)):
            stored_data = lines[records].split()# takes records line by line
            stored_firstname = stored_data[0]
            stored_lastname = stored_data[1]
            if stored_firstname == delete_firstname and stored_lastname == delete_lastname:#compares stored names with user input name
                found=True
                user_confirmation = input("You are about to delete '{} {}' Records (Y/N): ".format(delete_firstname,delete_lastname)).lower()
                if "y" == user_confirmation: # gets user Confirmation before deleting
                    del(lines[records]) #deletes entire record
                    print("")
                    print("{}'s data has been deleted..".format(name_to_be_deleted))
                    print("")
                    break
                elif "n" == user_confirmation: #Exits the function if user doesnt want to delete.
                    break
                else:
                    print("Enter (Y/N)") # for invalid responses
        if found == False:
            print("Driver not Found!")
            print("Try Again...")

        with open("championship_data.txt","w") as file : # rewrites the rest of the file (after removing the record)
            for line in lines:
                file.write(line)
def UDD_Function():
    print("Update Driver Details...")
    print("")
    driver_to_be_updated = input("Enter the Drivers Name for which details needs to be updated: ").title()
    driver_name = driver_to_be_updated.strip().split()
    driver_firstname = driver_name[0]
    driver_lastname = driver_name[1]
    update_successful = False
    with open("championship_data.txt") as file :  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()
        for records in range(len(lines)):
            stored_data = lines[records].split()# takes records line by line
            stored_firstname = stored_data[0]
            stored_lastname = stored_data[1]
            if stored_firstname == driver_firstname and stored_lastname == driver_lastname:
                print("Exsisting Record for '{}'".format(driver_to_be_updated))
                print(lines[records])
                updated_player_name = driver_to_be_updated
                updated_player_age = int(input("Enter Age: "))
                updated_player_team = input("Enter Team: ").title()
                updated_player_car = input("Enter Car: ").title()
                updated_player_current_points = int(input("Enter Current Points: "))
                updated_records = '{:<22} {:<12} {:<22} {:<18} {:<12}\n'.format(updated_player_name, updated_player_age, updated_player_team,updated_player_car, updated_player_current_points)
                lines[records] = updated_records # Values are updated
                update_successful=True
                print("")
                print("{} data has been updated..".format(driver_to_be_updated))
                print("")
    if update_successful == False:
        print("Driver not found..")
    with open("championship_data.txt","w") as file : # rewrites the file (after updating the record)
            for line in lines:
                file.write(line)
def VCT_Function():
    print("Display Championship Standings..")
    print("")
    with open("championship_data.txt") as file:  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()

    for outer_loop in range(1, len(lines)): #outer loop to make sure every element is being considered
        for records in range(1, len(lines)-1): #takes all the elements in the list except the Header.
            current_player_points = int(lines[records].strip().split()[-1]) #gets the current players points
            next_player_points = int(lines[records+1].strip().split()[-1]) #gets the next players points
            if current_player_points < next_player_points:
                temp = lines[records]  # using Bubble sort idea to display points table in descending order
                lines[records] = lines[records + 1]
                lines[records + 1] = temp
    #Formatting for the CHAMPIONSHIP STANDINGS
    print("")
    print("░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ CHAMPIONSHIP STANDINGS ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░")
    print("")

    for line in lines: #Ouput line by line..
        print(line)
def SRR_Function():
    race_data_file = open("race_data.txt", "r+")  # opens file for read and write at the same time
    line_in_race_data = race_data_file.readline()
    if line_in_race_data == "":
        header_race_data = '{:<12} {:<12} {:<22} {:<18} {:<12}\n'.format("DATE","LOCATION","DRIVER","POSITION","POINTS")
        race_data_file.write(header_race_data)

    race_locations= ["Nyirad","Holjes","Montalegre","Barcelona","Riga","Norway"]#CHARACTER ENCODING... ACII cant handle!
    random_location= random.randint(0,len(race_locations)-1)
    #Raceday
    location = race_locations[random_location]
    date = datetime.datetime.now()
    race_date=date.strftime("%D")

    driver_available = []
    with open("championship_data.txt") as file :  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()
        for records in range(len(lines)):
            stored_data = lines[records].split()# takes records line by line
            stored_firstname = stored_data[0]
            stored_lastname = stored_data[1]
            driver = (stored_firstname+" "+stored_lastname)
            driver_available.append(driver)

    contestants = driver_available[1:] #removes the "name" and "age"
    contestants_copy = contestants.copy() #copying the drivers list
    random.shuffle(contestants_copy) #simulates positions randomly using - shuffle
    #contestants copy - drivers positions from [0] which is First
    race_points = 0
    drivers_position = 0
    for position in range(len(contestants_copy)):
        if position == 0: #FIRST PLACE
            drivers_position = 1
            race_points = 10
        elif position == 1: #SECOND PLACE
            drivers_position = 2
            race_points = 7
        elif position == 2:  #THIRD PLACE
            drivers_position = 3
            race_points = 5
        else:
            race_points=0
        drivers_position=position+1
        drivers_points=race_points
        driver_name=contestants_copy[position].strip().split()
        driver_firstname=driver_name[0]
        driver_lastname=driver_name[1]
        #updates
        with open("championship_data.txt") as file:  # Reads all the lines using with command .. reduce close and Open commands
            lines = file.readlines()
            for records in range(len(lines)):
                stored_data = lines[records].split()  # takes records line by line
                stored_firstname = stored_data[0]
                stored_lastname = stored_data[1]
                if stored_firstname == driver_firstname and stored_lastname == driver_lastname:
                    updated_player_name = stored_firstname+" "+stored_lastname
                    updated_player_age = stored_data[2]
                    updated_player_team = stored_data[3]+" "+stored_data[4]
                    updated_player_car = stored_data[5]
                    updated_player_current_points = int(stored_data[-1]) + race_points
                    updated_records = '{:<22} {:<12} {:<22} {:<18} {:<12}\n'.format(updated_player_name,updated_player_age,updated_player_team,updated_player_car,updated_player_current_points)
                    lines[records] = updated_records  # Values are updated
        with open("championship_data.txt", "w") as file:  # rewrites the file (after updating the record)
            for line in lines:
                file.write(line)

        #Wrtiting to race data file (as required)
        race_data_file.write('{:<12} {:<12} {:<22} {:<18} {:<12}\n'.format(race_date,location,updated_player_name,drivers_position,drivers_points))
    race_data_file.close()

"""                                         MAIN PROGRAM STARTS FROM HERE                                           """
import random
import datetime

# Creates Two text files if it doesn't exist
race_data_file = open("race_data.txt", "a")
championship_data_file = open("championship_data.txt", "a")

exit_response = False # Checks whether user wants to Exit the program
while exit_response != True:
    response = Menu_Screen() # Initializing the program
    if response == "ESC":
        exit_response = True




