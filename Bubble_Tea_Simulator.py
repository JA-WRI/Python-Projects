#Jaden Wright-Maurais
#261176273
#This program will allow users to create their own bubble tea drink. 
#If the user enters invalid choices the program will end. 
#If the enter correct choices the program will display their final 
#drink order with their chosen ingredients.

SMALL_CUP = 355  
MEDIUM_CUP = 473
LARGE_CUP = 621
C = 4.184 #heat capacity of liquid water
base = 1
FUSION = 334 #Heat of fusion for water at 0°C
GRAMS_PER_ICE = 5 #amount og grams per ice cube
        

print("Welcome to the DIY Tea & Juice Maker!")



drink_base = (input("What kind of base do you want?"

" Please enter 1 for milk or 2 for fruit: "))


#if user choses milk as their base the following parameters will happen

if drink_base == "1" : 

    lactose_intolerance = input("Do you have lactose intolerance?"
    "y for yes, n for no: ")
    

    if lactose_intolerance == "y" :
    
        base = input("Do you want soy milk or oat milk?" 
        " Please type in your choice [soy/oat]: ")
    
        #assigning the variable 'base' the type of milk they inputed

        if base == "soy" :
            base = "soy milk"

        if base == "oat" :
            base = "oat milk"
            
    #if user is not lactose then 'base' is regular milk

    if lactose_intolerance == "n" :
        
        lactose_intolerance = base
        base = "regular milk"
        
        
        
#if user wants juice as their base the following parameters will happen 

if drink_base== "2" :
    

    base= input ("Which fruit do you want?"
    " Please type in your choice [mango/strawberry]: ")
    

    #assigning varible 'base' to the type of juice they imputed 

    if base == "mango" :
            base = "mango juice"


    if base == "strawberry" :
            base = "strawberry juice"
    
    

#asking user which type of tea they would like 

tea_type = input("From the following tea type:\n- No Tea\n- Black Tea\n"
"- Green Tea\n- Matcha\nPlease choose a tea type: ")
    

#if the user combines a juice base with matcha 
#the entry will be invalid and the program will end

if tea_type == "Matcha" and drink_base == "2" :
       
     print("Invalid choice! End of the program")
        


#any other combination of base and tea type will be valid 
#and the program will continue 

else :
    
    toppings = input("From the following toppings:\n- No Topping\n- Bobas\n"
    "- Coconut Jelly\nPlease enter your choice for toppings: ")

    drink_size= input("Please enter your desired size of cup"
    "(Please enter s for small, m for medium, or l for large): ")


    #Assigning users drink size to corresponding mass of the drink in grams/ 
    #(masses in defined varibles  )

    if  drink_size == "s" :
            drink_size = SMALL_CUP

    elif drink_size == "m" :
            drink_size= MEDIUM_CUP

    elif drink_size == "l" :
            drink_size = LARGE_CUP


    temperature_of_drink = float(input("Please enter your desired temperature"
    "of your beverage (between 1 and 4 degrees): "))



    #if temperature is between 1-3 degrees,
    #the following calculations will happen 
    #where the temperature of the drink is the inputed value from the user 

    if temperature_of_drink >=1 and temperature_of_drink <=3 :
                
        change_in_temp_ice = temperature_of_drink
        change_in_temp_drink = (25 - temperature_of_drink)
        ice_in_grams = ((drink_size) * (C) * (change_in_temp_drink)
        ) / ((FUSION) + (C)*(change_in_temp_ice))
        
        amount_of_ice = (ice_in_grams // GRAMS_PER_ICE)
                
                
        #displaying final drink order to user, with all ingredients chosen
        #and temperature of the drink and the amount of ice cubes needed

        print("Your drink is a", base, "and", tea_type, "with", toppings +".")
                
        print("The temperature of your beverage will be", temperature_of_drink
        , "Celcius degree after all", 
        round(amount_of_ice), "ice cubes melted.")
                
        print("Have a nice day!")
    

    #if temperature is between 4-10 degrees, 
    #the following calculations happen
    #where the temperature of the drink will be computed to 4 degrees
    

    elif temperature_of_drink >= 4 and temperature_of_drink <= 10 :
    
        temperature_of_drink = 4.0

        change_in_temp_drink = (25 - 4)
                
        change_in_temp_of_ice = (4) 

        ice_in_grams = ((drink_size) * (C) * (change_in_temp_drink)
        ) / ((FUSION) + (C) * (change_in_temp_of_ice))

        amount_of_ice = (ice_in_grams // GRAMS_PER_ICE) 


        print("Your drink is a", base, "and", tea_type, "with", 

        toppings + ".")


        print("The temperature of your beverage will be", 

        temperature_of_drink, "Celcius degree after all",

        round(amount_of_ice), "ice cubes melted.")


        print("Have a nice day!")



    #if user wants their drink below 1 degrees or higher than
    #10 degrees the program will read it as invalid and end 
    
    else:
        
        print("Invalid choice! End of the program")