#Jaden Wright-Maurais
#261176273
#This program runs vessel navigation options. Depending on the user’s 
#choice and the vessel’s gps coordinates and dimentions, the program 
#can inform the user whether the vessel is approaching a dangerous location,
#or updates the vessel’s coordinates or compute the maximum 
#occupancy of the vessel.  


#some things are still wrong in this program(update gps and gpa coordinates)


MIN_LAT = -90 #minimum latitude
MAX_LAT = 90 #maximum latitude
MIN_LONG = -180 #minimum_longitude
MAX_LONG = 180 #maximum longitude
EARTH_RADIUS = 6371
import math
import random


def meter_to_feet(num_meters):
    
    """"
    (float) -> float
    
    returns a value in feet (2 decimal places)
    from given value num_meters
    
    >>>meter_to_feet(1)
    3.28
    >>>meter_to_feet(4.67)
    15.32
    >>>meter_to_feet(1.52467)
    5.0
    """

    num_meters = round(num_meters * 3.28, 2)

    return num_meters



def degrees_to_radians(num_degrees):
    
    """
    (float) -> float
    
    returns a value in radians (2 decimal places)
    from a given value num_degrees
    
    >>>degrees_to_radians(180)
    3.14
    >>> degrees_to_radians(90)
    1.57
    >>>degrees_to_radians(10.4756)
    0.18
    """
    
    num_degrees = round(((num_degrees * math.pi) / 180), 2)

    return num_degrees



def get_vessel_dimensions():
    
    """
    () -> float,float
    
    returns two float numbers in feet from two inputed floats 
    (in meters) from user
    
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 4.67
    Enter the vessel width (in meter): 1
    (15.32, 3.28)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 100
    Enter the vessel width (in meter): 100
    (328.0, 328.0)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 5.9876
    Enter the vessel width (in meter): 3.5467
    (19.64, 11.63)
    """
    
    #asking user for dimentions 
    vessel_length = float(input("Enter the vessel length (in meter): "))
    a = meter_to_feet(vessel_length) 

    vessel_width = float(input("Enter the vessel width (in meter): "))
    b = meter_to_feet(vessel_width)
    

    return (a, b)  



def get_valid_coordinate(val_name, min_float, max_float):
    
    """
    returns a valid inputed float from user within interval 
    ]min_float,max_float[. If inputed value is not within the interval, 
    function will print invalid coordinate and continue asking 
    for a float number
    
    Parameters:
        val_name: name of coordinate (str)
        min_float: minimum value of coordinate (float)
        max_float: maximum value o coordinate (float)
    Returns:
        coordinate (float): inputed by user

    Examples:
    >>> get_valid_coordinate('latitude', -90, 90)
    What is your latitude ?-100
    Invalid latitude
    What is your latitude ?-50
    -50.0
    >>> get_valid_coordinate('longitude', -180, 180)
    What is your longitude ?-200
    Invalid longitude
    What is your longitude ?200
    Invalid longitude
    What is your longitude ?54
    54.0
    >>> get_valid_coordinate('y-coordinate', 50, 55)
    What is your y-coordinate ?49
    Invalid y-coordinate
    What is your y-coordinate ?50
    50.0
    """
    
    #getting coordinate from user 
    coordinate = float(input("What is your " +val_name + " ?"))

    while coordinate < min_float or coordinate > max_float :
        print ("Invalid", val_name)
        coordinate = float(input("What is your "+val_name+ " ?"))


    return coordinate
 
 
        
def get_gps_location():
    
    """
    returns two floats by calling the 
    get_valid_coordinates function 

    Parameters:
        None

    Returns:
        a : latitude (float) 
        b : longitude (float)
        
    Examples:
    >>> get_gps_location()
    What is your latitude ?-100
    Invalid latitude
    What is your latitude ?50
    What is your longitude ?-200
    Invalid longitude
    What is your longitude ?0
    (50.0, 0.0)
    >>> get_gps_location()
    What is your latitude ?40
    What is your longitude ?-87
    (40.0, -87.0)
    >>> get_gps_location()
    What is your latitude ?23.6789
    What is your longitude ?-200
    Invalid longitude
    What is your longitude ?-15.4356
    (23.6789, -15.4356)
    """
    
    #calling the function and storing result as a varibale 
    latitude_coor = get_valid_coordinate('latitude', MIN_LAT, MAX_LAT)
    longitude_coor = get_valid_coordinate ('longitude', MIN_LONG, MAX_LONG)
    
    return latitude_coor, longitude_coor




def distance_two_points(latitude_1, longitude_1, latitude_2, longitude_2):
    
    """
    (float, float, float, float) -> float
    
    returns the distance between latitude_1, longitude_1 and
    latitude_2, longitude_2 using the Haversine formula, where
    the four input values of longitude and latitude are convert to
    radians by calling the degrees_to_radians function

    >>> distance_two_points(45.65, -50.34, 87.24, -5.98)
    4685.07
    >>> distance_two_points(35.08, -70.45, 35.08, -70.45)
    0.0
    >>> distance_two_points(90, -180, 1, 1)
    9885.2
    """
    
    #changing values to radians by calling function
    latitude_1 = degrees_to_radians(latitude_1)
    longitude_1 = degrees_to_radians(longitude_1)
    latitude_2 = degrees_to_radians(latitude_2)
    longitude_2 = degrees_to_radians(longitude_2)

    #distance between latitude
    delta_alpha = abs(latitude_1 - latitude_2)
    
    #distance between longitude
    delta_beta = abs(longitude_1 - longitude_2)

    #applying formula 
    a = math.sin(delta_alpha / 2)** 2 + math.cos(
    latitude_1) * math.cos(latitude_2) * math.sin(delta_beta / 2)** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt (1-a))
    d = EARTH_RADIUS*c
    
    return round(d,2)



def check_safety (latitude, longitude):
    
    """
    Prints message to user based on how close their given
    longitude and latitude distance is to a restricted zone.
    This function will call the distance_two_points function
    
    Parameters:
        latitude: float
        longitude: float
        
    Prints
        Safe Navigation: When parameters are not close to or in
        a restricted zone
        Error restricted zone: if distance between two points
        is less than or equal to 400
        Warning Hazerdous area! Navigate with caution: if longitude is
        between 40 and 41 degrees and if longitude is between 
        -71 and -70 degrees
    
    Examples:
    >>> check_safety (21.804, -72.305)
    Error: Restricted zone!
    >>> check_safety (87.23, -15.34 )
    Safe navigation..
    >>> check_safety (40.985, -70.987)
    Warning: Hazerdous area! Navigate with caution.
    """
    
    restricted_zone = distance_two_points (latitude, longitude, 25, -71)
    
    if restricted_zone <= 400 :
        print("Error: Restricted zone!")

    elif (40 <= latitude <= 41)  and  (-70 >= longitude >= -71) :
        print("Warning: Hazardous area! Navigate with caution.")
    
    else :
        print("Safe navigation.")
        
        

def get_max_capacity (v_length, v_width):

    """
    (float, float) -> int
    
    returns the computated maximum number of people vessel can support
    using the v_length, v_width. Depending on the length 
    of the vessel the function use different formulas
    
    >>> get_max_capacity (18, 6)
    7
    >>> get_max_capacity (30, 6)
    24
    >>> get_max_capacity (0.7, 8)
    0
    """
    
    #for vessel lengths 26 or less 
    if v_length <= 26 :
        max_cap = (v_length*v_width)/15
        
    #for vessel length greater than 26
    if v_length >26 :
        max_cap = v_length*v_width/15 + (v_length -26)*3
    

    return int(max_cap)



def passengers_on_boat (v_length, v_width, n_passengers):

    """
    (float, float, int) -> True or False 

    This function will call the  get_max_capacity function and 
    use v_length and v_width to calculate the maximum capacity.
    This function will return False if n_passengers is greater than 
    max capacity or if passengers cannot be equally distributed 
    across 4 corners. Otherwise funtion will return True
    
    >>>passengers_on_boat (18, 6, 6)
    False
    >>>passengers_on_boat (30, 6, 12)
    True
    >>>passengers_on_boat (30, 6, 13)
    False
    """

    max_capacity = get_max_capacity (v_length, v_width)
    
    #if the remainder of n_passengers divided by 4 doesn't equal zero
    if n_passengers % 4 != 0 or n_passengers > max_capacity:
        return False 

    else :
        return True



def update_coordinate (org_pos, min_float, max_float):
    
    """
    (float, float, float) -> float
    
    This function will select a random number between -10 and 10
    using the random() function. This random value will be added
    to org_pos. If new value is not within ]min_float max float[, 
    then function will continue generating random numbers
    until a value is within the interval. Function then returns 
    the float number to 2 decimal places
    
    >>> update_coordinate (65.7546, -90, 90)
    56.8
    update_coordinate (65.7546, -90, 90)
    57.73
    >>>update_coordinate (65.7546, -90, 90)
    67.42
    """
    
    random.seed(123)
    
    #assigning random number to variable
    i = random.random()* 20 - 10

    new_pos = i + org_pos
    
    #if new position is not in the interval funtion continues 
    while  min_float > new_pos > max_float :
        i = random.random()*20 -10 
        new_pos = i + org_pos
        

    return round(new_pos,2)



def wave_hit_vessel (latitude, longitude):

    """
    (float, float) -> float, float
    
    Returns the updated latitude and longitude values
    by calling update_coordinate function twice then calling check_safety
    to check the safety of new location.
    
     >>>wave_hit_vessel (65.76, -87.34)
    Safe navigation.
    (68.73, -93.19)
    >>> wave_hit_vessel (65.76, -87.34)
    Safe navigation.
    (63.91, -78.53)
    >>> wave_hit_vessel (27.786, -70.354)
    Safe navigation.
    (20.12, -76.07)
    """

    latitude = update_coordinate (latitude, MIN_LAT, MAX_LAT)
    longitude = update_coordinate (longitude, MIN_LONG, MAX_LONG)
    
    check_safety (latitude, longitude)


    return (latitude, longitude)



def vessel_menu ():

    """
    This function is the main boat menu. Users will enter the gps
    coordinates and the dimentions of their boat. This menu shows
    4 options for the user to chose from.
    1) Users can check if they are approching a dangerous by location
    by calling the check_safety function.
    2) Users can check if it is possibe to fit a certain amount of people
    on the vessel by calling the passengers_on_boat function.
    3) Users can update their position by calling wave_hit_vessel function
    4) Users can Exit the boat menu and the program will end.
    This function will keep running until user choses to exit the boat
    menu.
    """


    print("Welcome to the boat menu!")
    

    #asking user for their gps coordinates 
    latitude, longitude = get_gps_location()
    

    print ("Your current position is at latitude", latitude, 
    "and longitude", longitude)


    #asking user for vessel dimentions 
    v_lenght, v_width = get_vessel_dimensions()
    

    print ("Your boat measures", v_lenght, "feet by", v_width, "feet")
    

    #displaying boat menu
    print ("Please select an option below: ")
    print ("1. Check the safety of your boat")
    print ("2. Check the maximum number of people that"
    " can fit on the boat")
    print ("3. Update the position of your boat")
    print ("4. Exit boat menu")
    option = input("Your selection: ")
    
    
    #while user doesn't chose 4, the function continues
    while option == "1" or option =="2" or option == "3":
        
        if option =="1":
            
            check_safety (latitude, longitude)
            
            print ("Please select an option below: ")
            print ("1. Check the safety of your boat")
            print ("2. Check the maximum number of people that"
            " can fit on the boat")
            print ("3. Update the position of your boat")
            print ("4. Exit boat menu")
            option = input("Your selection: ")
        
        
        elif option == "2":
            
            n_passengers = int(input("How many adults go on the boat? "))
            
            if passengers_on_boat (v_lenght, v_width, n_passengers):
                print("Your boat can hold", n_passengers, "adults")
           
            else:
                print("Your boat cannot hold", n_passengers, "adults")
            
            print ("Please select an option below: ")
            print ("1. Check the safety of your boat")
            print ("2. Check the maximum number of people that"
            " can fit on the boat")
            print ("3. Update the position of your boat")
            print ("4. Exit boat menu")
            option = input("Your selection: ")


        elif option == "3":
            
            latitude, longitude = wave_hit_vessel (latitude, longitude)
            
            print("Your new position is latitude of", latitude,
            "and longitude of", longitude)
            
            print ("Please select an option below: ")
            print ("1. Check the safety of your boat")
            print ("2. Check the maximum number of people that"
            " can fit on the boat")
            print ("3. Update the position of your boat")
            print ("4. Exit boat menu")
            option = input("Your selection: ")
            
    if option == "4" :
        print ("End of boat menu.")
        
vessel_menu()
