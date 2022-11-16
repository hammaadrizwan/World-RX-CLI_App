def Progress_Bar(percent, statement):
    progress_bar_length = 45
    limit = 100
    done_len = int(percent * progress_bar_length)
    bar = "{} ".format(statement) # statement
    bar += "|" #bar formatting
    bar += "█" * done_len #the progress icon- to indicate the status completed
    bar += "█"
    bar += "░" * (progress_bar_length - done_len)#removes whitespace when the progress bar increases
    bar += "| "
    bar += str(round(percent * 100)) #progress indicator - numerical form
    bar += "%"
    print("\r", end='') #prints all in one line, '\r' returns back to the same line
    print(bar + (" " * 5), end='') #space between the bar and the text
def Menu_Screen():
    # MENU SCREEN - Displayed when System Launches
    print("")
    print("Type the code for the required function")
    print("   {}      - Add driver details".format("\033[1m" + "ADD" + "\033[0m")) #("\033[1m" + string + "\033[0m") for bold letters in ansci encoding
    print("   {}      - Delete driver details".format("\033[1m" + "DDD" + "\033[0m"))
    print("   {}      - Updating a record".format("\033[1m" + "UDD" + "\033[0m"))
    print("   {}      - Displays rally cross standings table".format("\033[1m" + "VCT" + "\033[0m"))
    print("   {}      - Simulating a random race".format("\033[1m" + "SRR" + "\033[0m"))
    print("   {}      - Displays race table".format("\033[1m" + "VRL" + "\033[0m"))
    print("   {}      - Save data".format("\033[1m" + "STF" + "\033[0m"))
    print("   {}      - Load data from the saved text file".format("\033[1m" + "RFF" + "\033[0m"))
    print("   {}      - Exit Program".format("\033[1m" + "ESC" + "\033[0m"))
    print("")
    print("   {}     - For more information".format("\033[1m" + "HLP" + "\033[0m"))
    print("")

    selected_option = input("> Enter Code: ").upper().strip()[:3] #takes in the first 3 elements to consideration only
    print("")
    # '.upper()' to minimise errors regarding CASE SENSITIVE
    # '.strip()' is used to remove WHITE SPACES in the input

    if selected_option == "ADD": #Function calls
        print("")
        print(" Driver Registration ")
        print("---------------------")
        ADD_Function()
    elif selected_option == "DDD":
        print("")
        print(" Delete Records ")
        print("----------------")
        DDD_Function()
    elif selected_option == "UDD":
        print("")
        print(" Update Records ")
        print("----------------")
        UDD_Function()
    elif selected_option == "VCT":
        print("")
        print("Displaying Championship Standings..")
        print("")
        VCT_Function()
    elif selected_option == "SRR":
        for status in range(1, 100 + 1):
            percent = status / 100
            Progress_Bar(percent, "Initialising Race")
            time.sleep(0.005)
        print("Done")
        for status in range(1, 100 + 1):
            percent = status / 100
            Progress_Bar(percent, "Simulating Race  ")
            time.sleep(0.001)
        print("Done")
        print("Simulation: COMPLETE ")
        SRR_Function()
    elif selected_option == "VRL":
        print("Displaying Race Table..")
        VRL_Function()
    elif selected_option == "STF":
        STF_Function()
        for status in range(1, 101):
            percent = status / 100
            Progress_Bar(percent, "Saving Files")
            time.sleep(0.05)
        print("COMPLETE")
        print("FILES SAVED")
    elif selected_option == "RFF":
        RFF_Function()
        for status in range(1, 101):
            percent = status / 100
            Progress_Bar(percent, "Loading Files")
            time.sleep(0.01)
        print("COMPLETE")
        print("SUCCESSFUL")
    elif selected_option == "ESC":
        print("Exiting Program..")
    elif selected_option =="HLP":
        print("Choose a function from above, and type in the same format as the example given below")
        print("eg: type 'DDD' if you want to delete a driver from the system")
    elif selected_option =="":
        print("Required Input!")
        print("Input cannot be blank, please try again.")
    else:
        print("'{}' Wrong Input".format(selected_option))
        print("ENTER the code stated below for the required function.")

    return selected_option
def STF_Function():
    race_data_file.close()
    championship_data_file.close() #closing exsisting files will save changes made to that doc.
def RFF_Function():
    race_data_filename = "race_data.txt"
    championship_data_filename = "championship_data.txt"
    race_data_file = open(race_data_filename, "r") #Loads data in to the variable to resume capabilities
    championship_data_file = open(championship_data_filename, "r")
def ADD_Function():
    RFF_Function() #loads data from the text file
    while True: #using exception handling to minimise errors at syntax level.
        print("Enter Name:")
        try:
            new_player_name = input("> ").title()
            if any((character.isdigit() for character in new_player_name)) == True: # checks whether any numbers are being entered into the name
                raise TypeError("Name cannot contain numbers") #if so... raises TypeError
            break
        except TypeError:
            print("Name cannot contain numbers, Try Again") # until the user inputs in the correct format, program will not move ahead.
        print("")

    while True: # repeats till user enters an integer
        print("Enter Age:")
        try:
            new_player_age = int(input("> "))
            break
        except ValueError:
            print("Requires an Integer, Try Again")
    print("")

    print("Enter Team:")
    new_player_team = input("> ").title()
    print("")

    print("Enter Car:")
    new_player_car = input("> ").title()
    print("")

    while True:
        print("Enter Current Points:")
        try:
            new_player_current_points = int(input(">  "))
            break
        except ValueError:
            print("Requires an Integer, Try Again")
    print("")

    championship_data_file = open("championship_data.txt", "r+")   #opens file for read and write at the same time
    line_in_championship_data = championship_data_file.readline()

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
    STF_Function()
def DDD_Function():
    RFF_Function()
    print("Enter the Name To be deleted:")
    name_to_be_deleted = input("> ").title()
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
            print("Driver not Found!") #Tells the user if the deletion was a success or not,

        with open("championship_data.txt","w") as file : # rewrites the rest of the file (after removing the record)
            for line in lines:
                file.write(line)
    STF_Function()
def UDD_Function():
    RFF_Function()

    print("Enter the Driver's Name for which details needs to be updated: ")
    driver_to_be_updated = input("> ").title()
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
            if stored_firstname == driver_firstname and stored_lastname == driver_lastname: #showing exsisitng records
                print("Exsisting Record for '{}'".format(driver_to_be_updated))
                print("Name ...........:  {}".format(driver_to_be_updated))
                print("Age ............:  {}".format(stored_data[2]))
                print("Team ...........:  {}".format(str(stored_data[3]+" "+stored_data[4])))
                print("Car ............:  {}".format(stored_data[5]))
                print("Current Points .:  {}".format(stored_data[-1]))
                print("")

                updated_player_name = driver_to_be_updated
                print("Which records do you need to update? ")
                print("(type 'all' if you want to update everything)")
                update_option = input("> ").lower()#asks user whether they want to change one field or everything

                if update_option =="name":
                    while True:
                        try:
                            updated_player_name = input("Enter Name: ").title()
                            if any((character.isdigit() for character in updated_player_name)) == True:
                                raise TypeError("Name cannot contain numbers")
                            break
                        except TypeError:
                            print("Name cannot contain numbers, Try Again")
                        print("")
                    updated_player_name_split=updated_player_name.split()
                    stored_data[0]=updated_player_name_split[0]#splits the name into fname and lname(assumptions)
                    stored_data[1] = updated_player_name_split[1]
                elif update_option == "age":
                    while True:
                        try:
                            updated_player_age = int(input("Enter Age: "))
                            break
                        except ValueError:
                            print("Requires an Integer, Try Again")
                    print("")
                    stored_data[2] = updated_player_age
                elif update_option == "team":
                    updated_player_team = input("Enter Team: ").title()
                    updated_player_team_split = updated_player_team.split()
                    stored_data[3] = updated_player_team_split[0]
                    stored_data[4] = updated_player_team_split[1]
                elif update_option == "car":
                    updated_player_car = input("Enter Car: ").title()
                    stored_data[5] = updated_player_car
                elif "points" in update_option.split() or "current" in update_option.split():# checks whether 'points' or 'current' is mentioned
                    while True:
                        try:
                            updated_player_current_points = int(input("Enter Current Points: "))
                            break
                        except ValueError:
                            print("Requires an Integer, Try Again")
                    stored_data[-1] = updated_player_current_points
                elif update_option=="all": # user can update all records of the driver if they need,
                    while True:
                        try:
                            updated_player_name = input("Enter Name: ").title()
                            if any((character.isdigit() for character in updated_player_name)) == True:
                                raise TypeError("Name cannot contain numbers")
                            break
                        except TypeError:
                            print("Name cannot contain numbers, Try Again")
                    while True:
                        try:
                            updated_player_age = int(input("Enter Age: "))
                            break
                        except ValueError:
                            print("Requires an Integer, Try Again")
                    updated_player_team = input("Enter Team: ").title()
                    updated_player_car = input("Enter Car: ").title()
                    while True:
                        try:
                            updated_player_current_points = int(input("Enter Current Points: "))
                            break
                        except ValueError:
                            print("Requires an Integer, Try Again")

                    updated_player_name_split=updated_player_name.split()
                    stored_data[0]=updated_player_name_split[0]# manually assigns each update to its location in the text
                    stored_data[1] = updated_player_name_split[1]
                    stored_data[2] = updated_player_age

                    updated_player_team_split = updated_player_team.split()
                    stored_data[3] = updated_player_team_split[0]
                    stored_data[4] = updated_player_team_split[1]
                    stored_data[5] = updated_player_car
                    stored_data[-1] = updated_player_current_points
                else:
                    print("Wrong input")
                    print("Choose the correct field. eg-'Team' if the details of driver's team should be updated..")
                updated_records = '{:<22} {:<12} {:<22} {:<18} {:<12}\n'.format(updated_player_name, stored_data[2],(stored_data[3] +" "+stored_data[4]),stored_data[5],stored_data[6])
                #Left alings all the characters using .format({:<})
                lines[records] = updated_records # Values are updated
                update_successful=True
                print("")
                print("{}'s data has been updated..".format(driver_to_be_updated))
                print("")# message is being shown after records are being updated successfully
    if update_successful == False:
        print("Driver not found..")
    with open("championship_data.txt","w") as file : # rewrites the file (after updating the record)
        for line in lines:
            file.write(line)#writes entire file again with updated fields
    STF_Function()
def VCT_Function():
    RFF_Function()
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
    STF_Function()
    #Formatting for the CHAMPIONSHIP STANDINGS
    print("")
    print("░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ CHAMPIONSHIP STANDINGS ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░")#HEADER
    print("")
    rank = 0 #rank zero to start with, neglecting  the header in the championship standings
    for line in lines: #Ouput line by line..
        if rank == 0:
            print("   "+line)# since first line in the lines array is the Header, there will be no rank assigned
        else:
            print(("{}. "+line).format(rank)) #ranks assigned according to the points gained
        rank += 1

def SRR_Function():
    RFF_Function()
    race_data_file = open("race_data.txt", "r+")  # opens file for read and write at the same time
    line_in_race_data = race_data_file.readline()
    if line_in_race_data == "":
        header_race_data = '{:<12} {:<12} {:<22} {:<18} {:<12}\n'.format("DATE","LOCATION","DRIVER","POSITION","POINTS")
        race_data_file.write(header_race_data)

    # function to generate random date
    def Random_Race_location():
        race_locations= ["Nyirad","Holjes","Montalegre","Barcelona","Riga","Norway"]#CHARACTER ENCODING... ASCII cant handle!
        random_location= random.randint(0,len(race_locations)-1) #random number which will be as the index, to get a race location
        #Raceday
        location_random = race_locations[random_location]
        return location_random
    #function to generate random date
    def Random_Race_date():
        month = random.randint(1, 12) # gets a random month
        if month == 4 or month == 6 or month == 9 or month == 10: # if its one of these months such as april, there will be only 30 days
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        race_date_random = ("{}/{}/22".format(day, month)) #formats the random, day and month into date format.(where year is 2022 which us fixed-as one season can only last for a year,)
        return race_date_random
    race_location = Random_Race_location()
    race_date = Random_Race_date()
    driver_available = [] #store names of drivers available to race
    exsisting_dates = []# used to store exsisting dates

    with open("championship_data.txt") as file :  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()
        for records in range(1,len(lines)): #removes the "name" and "age" starts from next element
            stored_data = lines[records].split()# takes records line by line
            stored_firstname = stored_data[0]
            stored_lastname = stored_data[1]
            driver = (stored_firstname+" "+stored_lastname) #connects both fname and lname, and adds them to the available drivers list
            driver_available.append(driver)

    contestants = driver_available
    contestants_copy = contestants.copy() #copying the drivers list
    random.shuffle(contestants_copy) #simulates positions randomly using - shuffle
    #contestants copy - drivers positions from [0] which is First
    race_points = 0
    for position in range(len(contestants_copy)):
        if position == 0: #FIRST PLACE
            race_points = 10
        elif position == 1: #SECOND PLACE
            race_points = 7
        elif position == 2:  #THIRD PLACE
            race_points = 5
        else:
            race_points=0
        drivers_position = position+1
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

        #DUPLIACTE DATES - Validation
        with open("race_data.txt", "r") as file:  # rewrites the file (after updating the record)
            lines = file.readlines()
            occurrence = 0
            for records in range(1,len(lines)):
                stored_date = lines[records].split()[0]#takes the stored date
                occurrence = occurrence + 1 #records the number of times the date is being recorded for each contestants
                if occurrence == len(contestants_copy): #to avoid repetition of same dates being stored, once the threshold amount
                    # is met then the stored date is being appended to exsisting date array
                    exsisting_dates.append(stored_date)
                    occurrence =0# then limit is set to zero

        date_exists = True
        while date_exists == False:# checks if generated date is being already stored
            if race_date in exsisting_dates:#, if it is then new date is being generated
                date_exists = True
                race_date = Random_Race_date()

        #Wrtiting to race data file (as required)
        race_data_file.write('{:<12} {:<12} {:<22} {:<18} {:<12}\n'.format(race_date,race_location,updated_player_name,drivers_position,drivers_points))
    STF_Function()
def VRL_Function():
    print("Race Table Loading..")
    print("")
    RFF_Function()
    with open("race_data.txt") as file:  # Reads all the lines using with command .. reduce close and Open commands
        lines = file.readlines()

    for outer_loop in range(1, len(lines)):  # outer loop to make sure every element is being considered
        for records in range(1, len(lines) - 1):  # takes all the elements in the list except the Header.
            current_month = int(lines[records].split()[0].split("/")[1])  # gets the current month
            next_month = int(lines[records + 1].split()[0].split("/")[1])  # gets the next month
            current_day = int(lines[records].split()[0].split("/")[0])  # gets the current day
            next_day = int(lines[records + 1].split()[0].split("/")[0]) # gets the next day
            if current_month > next_month: #checks if current month is higher than next month(eg;is 5 is higher than 3)
                temp = lines[records]  # if true then next date records will be transfered to current date, using temporary varialble
                lines[records] = lines[records + 1]
                lines[records + 1] = temp
            if current_month == next_month: #if the months are same and if the current day is greater than the next day then the same idea of swapping takes place here
                if current_day > next_day:
                    temp = lines[records]   #same concept as above
                    lines[records] = lines[records + 1]
                    lines[records + 1] = temp
    STF_Function() #saving the file once done

    # Formatting for the CHAMPIONSHIP STANDINGS
    print("")
    print("░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ RACE TABLE ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░")
    print("")

    for line in lines: #Ouputs the sorted list line by line..
        print(line)

"""                                         MAIN PROGRAM STARTS FROM HERE                                           """
import random #needed for simulating random race
import time  #for progress bar, to limit traffic for program as many opertions take place at the same time, eg in SRR.


# Creates Two text files if it doesn't exist
race_data_filename = "race_data.txt"
championship_data_filename = "championship_data.txt"
race_data_file = open(race_data_filename, "a")
championship_data_file = open(championship_data_filename, "a")

exit_response = False # Checks whether user wants to Exit the program
while exit_response != True:
    response = Menu_Screen() # Initializing the program
    print("")
    if response == "ESC":
        exit_response = True
        break #Program terminates




