import json        
import sys
import random

   
def read(file_name):
    """
    (str) -> (dict)
    
    This function will read a JSON file into a dictionary then return
    the dictionary. This function also catches a fileNotFoundError
    and exits with error code 1

    """
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        
    except FileNotFoundError:
        print ("File does not exist")
        sys.exit(1)
    return data
    
    
def global_stats(dictionary):
    
    """
    (dict) -> (dict)
    
    This function will take the whole dictionary of data for the
    cellular base station and calculate any necessary statistics. It will then return a
    dictionary of all the stats
    """
    
    min_lat = dictionary['min_lat']
    max_lat = dictionary['max_lat']
    min_lon = dictionary['min_lon']
    max_lon = dictionary['max_lon']
    step = dictionary['step']
    
    points_in_area = round((((max_lat - min_lat) + 0.01) / step) * (((max_lon - min_lon) + 0.01) / step)) #calculating the point coverage
    total_baseStation = len(dictionary["baseStations"]) 
    
    
    num_antennas = 0
    coverage = {} #dictionary of all the points covered by an antenna 
    for base in dictionary["baseStations"]:
        for antenna in base['ants']:
            num_antennas += 1
            for point in antenna["pts"]:
                iteam = (point[0], point[1])
                if iteam not in coverage:
                    coverage[iteam] = [] #adding new point to coverage 
                coverage[iteam].append((base["id"], antenna["id"], point[2]))
    
    #calculating how many points are covered by one antenna then by multiple antennas 
    coverage_one = sum(1 for iteam, value in coverage.items() if len(value) == 1)
    coverage_more_than_one = sum(1 for iteam, value in coverage.items() if len(value) > 1)
    uncovered = points_in_area - len(coverage)
    
    
    max_coverage = max(len(value) for value in coverage.values()) #the maximum numer of antennas that cover one point 
    avg_coverage = round(sum(len(value) for value in coverage.values()) / len(coverage),2) #average number of antennas covering one point
    coverage_area_percentage = round(100 * len(coverage) / points_in_area, 2)
    
    max_baseStation_id = None
    max_antenna_id = None
    min_ants =0
    for base in dictionary["baseStations"]:
        for antenna in base["ants"]:
            hold = len(antenna["pts"])
            if (hold > min_ants):
                min_ants = hold
                max_baseStation_id = base["id"] #calculating the baseStation ID that covers the most points 
                max_antenna_id = antenna["id"]#calculating the antenna ID with the most points covered
    
    #dictionary of all calculated values
    statistics = {
        "total_base_stations": total_baseStation,
        "total_num_antennas": num_antennas,
        "max_antennas_per_bs": max(len(base['ants']) for base in dictionary["baseStations"]),
        "min_antennas_per_bs": min(len(base['ants']) for base in dictionary["baseStations"]),
        "avg_antennas_per_bs": num_antennas / total_baseStation,
        "point_coverage_one": coverage_one,
        "point_coverage_more_than_one": coverage_more_than_one,
        "uncovered_points": uncovered,
        "max_antennas_coverage": max_coverage,
        "avg_antennas_coverage": avg_coverage,
        "covered_area_percentage": coverage_area_percentage,
        "max_coverage_antenna": (max_baseStation_id, max_antenna_id)}
    
    return statistics

def base_stats(base,dictionary):
    """
    (dict)(dict)->(dict)
    
    This function will take in a dictionary of data and calculate any
    necessary statistics for a specific base station given. It will then
    return the dictionary of stats 

    """
    
    min_lat = dictionary['min_lat']
    max_lat = dictionary['max_lat']
    min_lon = dictionary['min_lon']
    max_lon = dictionary['max_lon']
    step = dictionary['step']
    
    points_in_area = round((((max_lat - min_lat) + 0.01) / step) * (((max_lon - min_lon) + 0.01) / step))
    num_antennas = len(base["ants"])

    
    coverage = {}
    for antenna in base["ants"]:
        for point in antenna["pts"]:
            iteam = (point[0], point[1])
            if iteam not in coverage:
                coverage[iteam] = []
            coverage[iteam].append((antenna['id'], point[2]))
    
    coverage_one = sum(1 for key, value in coverage.items() if len(value) == 1)
    coverage_more_than_one = sum(1 for key, value in coverage.items() if len(value) > 1)
    uncovered = points_in_area - len(coverage)
    
    max_coverage = max(len(value) for value in coverage.values())
    avg_coverage = round(sum(len(value) for value in coverage.values()) / len(coverage),2)
    coverage_area_percentage = round(100 * len(coverage) / points_in_area,2)
      
    max_baseStation_id = None
    max_antenna_id = None
    min_ants =0
    for antenna in base["ants"]:
        hold = len(antenna["pts"])
        if (hold > min_ants):
            min_ants = hold
            max_baseStation_id = base["id"]
            max_antenna_id = antenna["id"]
    
    statistics = {
        "total_num_antennas": num_antennas,
        "point_coverage_one": coverage_one,
        "point_coverage_more_than_one": coverage_more_than_one,
        "uncovered_points": uncovered,
        "max_antennas_coverage": max_coverage,
        "avg_antennas_coverage": avg_coverage,
        "covered_area_percentage": coverage_area_percentage,
        "max_coverage_antenna": max_antenna_id}
    
    return statistics


def nearest_antenna(lat, long, dictionary):
    """
    (str)(str)(dict) -> (dict)
    
    This function will go through each point in the dictionary of data and calculate
    which point is the closest to the point entered by the user. The base station ID,
    antenna ID with the closest distance will be saved in the returned dictionary 
    """
    
    min_distance = float('inf') #setting distance to infinity 
    nearestAntenna = None
    for base in dictionary['baseStations']:
        for antenna in base['ants']:
            for point in antenna['pts']:
                distance = ((lat - point[0])**2 + (long - point[1])**2)**0.5 #calculating the closest distance 
                if distance < min_distance:
                    min_distance = distance
                    nearestAntenna = {
                        "station_id": base['id'],
                        "antenna_id": antenna['id'],
                        "lat": point[0],
                        "lon": point[1],
                        "power": point[2]
                    }
    return nearestAntenna



def coverage(lat, long, dictionary):
    """
    (str)(str)(dict) -> None
    
    This function will determine if the latitudes and longitudes entered by the user
    match any of the points covered by the antenna. If the points match then the Base station ID
    and antenna Id will be printed. If the latitudes and longitudes entered by the user does not
    match then the nearest_antenna function will be called to calculate which antenna is the closest
    to the points entered by the user

    """
    
    covered = False
    for base in dictionary["baseStations"]:
        for antenna in base["ants"]:
            for point in antenna["pts"]:
                if point[0] == lat and point[1] == long:
                    print("Covered by base station ", base['id'], "and antenna ", antenna['id'], "with power ", point[2], " dBm")
                    covered = True
    if (covered == False):
        nearestAntenna = nearest_antenna(lat, long, dictionary)#finding the closest antenna
        print("Not explicitly covered. Nearest coverage by base station ", nearestAntenna['station_id'], "and antenna ", nearestAntenna['antenna_id'], "at coordinates (" , nearestAntenna['lat'], ",", nearestAntenna['lon'], ") with power ", nearestAntenna['power'], " dBm")
    
def display():
        
    data = read(file_name)
    print("\nWelcome to the cellular network provider program")
    
    
    while (True):
        option = int(input("\n\n1. Display Global Statistics\n2. Display Base Station Statistics\n   2.1 Statistics for a random station\n"
               "   2.2. Choose station by Id\n3. Check Coverage\n4. Exit\nPlease select an option from above: "))
    
        #checking for correct input 
        if (option< 1 or option> 4):
            print("Invalid input. Please enter a number between 1-4\n")
        
        #display global stats 
        elif (option == 1):
            
            stats = global_stats(data)
            print("\n\n**********************************************Global Statistics********************************************\n")
            print("The total number of base stations = ",stats["total_base_stations"])
            print("The total number of antennas = ",stats["total_num_antennas"] )
            print("The max, min and average of antennas per BS = ", stats["max_antennas_per_bs"], ",", stats["min_antennas_per_bs"], ",", stats["avg_antennas_per_bs"])
            print("The total number of points covered by exactly one antenna = ",stats["point_coverage_one"])
            print("The total number of points covered by more than one antenna = ", stats["point_coverage_more_than_one"])
            print("The total number of points not covered by any antenna = ", stats["uncovered_points"])
            print("The maximum number of antennas that cover one point =", stats["max_antennas_coverage"])
            print("The average number of antennas covering a point = ",stats["avg_antennas_coverage"])
            print("The percentage of the covered area = ", stats["covered_area_percentage"], "%")
            print("The id of the base station and antenna covering the maximum number of points = base station ",stats["max_coverage_antenna"][0],", antenna ", stats["max_coverage_antenna"][1])
            print("***********************************************************************************************************")
        
        #display station statistics
        elif (option == 2):
            option2 = input("Enter 2.1 for random station or 2.2 to choose by ID: ")
            
            if option2 == '2.1':
                base_station = random.choice(data['baseStations'])#taking random base from the BaseStations in dictionary 
                stats = base_stats(base_station, data)
            elif option2 == '2.2':
                base_id = int(input("Enter Station ID: "))
                base = next((s for s in data['baseStations'] if s['id'] == base_id), None)#getting the base station from the ID entred by the user
                if not base:
                    print(f"No base station found with ID {station_id}")
                    return
                stats = base_stats(base, data)
            else:
                print("Invalid input")
                break
            print("\n\n******************************************** Base Station Statistics**************************************\n")
            print("The total number of antennas = ",stats["total_num_antennas"] )
            print("The total number of points covered by exactly one antenna = ",stats["point_coverage_one"])
            print("The total number of points covered by more than one antenna = ", stats["point_coverage_more_than_one"])
            print("The total number of points not covered by any antenna = ", stats["uncovered_points"])
            print("The maximum number of antennas that cover one point =", stats["max_antennas_coverage"])
            print("The average number of antennas covering a point = ",stats["avg_antennas_coverage"])
            print("The percentage of the covered area = ", stats["covered_area_percentage"], "%")
            print("The id of the antenna that covers the maximum number of points = ",stats["max_coverage_antenna"])
            print("***********************************************************************************************************")
                
        elif (option == 3):
            lat = float(input("Enter Latitude: "))
            long = float(input("Enter Longitude: "))
            coverage(lat, long,data)
        
        elif (option ==4):
            break
        
    print("End of program!")

#can run on command line with this part of the code
"""if __name__ == "__main__":
    
    if (len(sys.argv)==2):
        file_name = sys.argv[1]
    else:
        print("Error, python script or JSON file not provided")
        sys.exit(1)
    display()
"""
#Displaying the project with a sample JSON file
file_name = "sample.json"
display()
