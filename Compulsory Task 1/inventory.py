
#========The beginning of the class==========

# created a class called shoe that takes takes in 5 arguments
class Shoe:
     
    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code
        self.product = product
        self.cost = cost 
        self.quantity = quantity 

# This method returns the cost shoes     
    def get_cost(self):
        return self.cost 

# this method returns the quantity of the shoes   
    def get_quantity(self):
        return self.get_quantity

# this string method prints out my all the info in the text file in a nice manner 
    def __str__(self):
        return f""""
----------------------------
    country : {self.country}  
----------------------------       
    code    : {self.code}
    product : {self.product}  
    cost    : {self.cost}
    quantity: {self.quantity}"""
                        

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============

# this function reads from the file strips and splits the information.
# it also appends the shoe class into the list 
def read_shoes_data():
    
    try:
        with open("inventory.txt", "r") as text_file:
            file = text_file.readlines()
            for line in range(1, len(file)):
                country,code,product,cost,quantity = file[line].strip().split(',')
                shoes = Shoe(country,code,product,float(cost),int(quantity))
                shoe_list.append(shoes)  
                
    except FileNotFoundError:
        print("inventory file not found. Please check file name correctly")        
                    
read_shoes_data()

# this function stores new info and writes the new info into the inventory.txt
def capture_shoes(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity):
    Data_Caputed = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
    shoe_list.append(Data_Caputed)
# writes to the file 
    with open("inventory.txt","w") as file:
        for shoe in shoe_list:
            file.write(f"{shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}\n")

# prints out all the shoes  
def view_all():
    print(*shoe_list) 
       
def re_stock():
# loop through list and find lowest quantity 
    list_qty = []
    for shoe in shoe_list:
        list_qty.append(shoe.quantity)
# this is the minimum quantity    
    lowest = min(list_qty)    
    for shoe in shoe_list:
        if shoe.quantity == lowest:
            print(shoe)
            
# this variable asks the user to enter 2 options 
            re_stock_option = input(""" Please see the quantity above and advise if you will be restocking

Please choose:

Yes - for the restock
No -  for not restocking \n """).lower()

# if the user chooses yes it will update a new quantity and wirte to the file 
     
            if re_stock_option == "yes":
                    value= int(input("Please enter new quantity number: "))
                    shoe.quantity = value
                    print(shoe.quantity)
# if the se no the select no the quantity will stay the same             
            elif re_stock_option == "no":
                print("Quantity will remain the same ")
                
                break
            
# writing the new updated value into the file as it loops through the shoe list              
            with open("inventory.txt","w") as f:
                for shoe in shoe_list:  
                    f.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            
# this function interates through shoe list
# if the shoe_code.code == s_code wil   
# it will return the shoe_code 
def search_shoe(search):
    for shoe_code in shoe_list:
        if shoe_code.code == search:
            return shoe_code 
             
    return (f"The shoe code {search} is not found\n")

# this function will iterate through shoe_list 
#and calculate the values 
def value_per_item():
    for i in shoe_list:
        Price = i.cost * i.quantity
        print(f"{i}Price:{Price} \n")
        
# this function will calculate the shoe with the higest quantity in the list
# by using the max function
# created a list to append the shoe inside it to get the highest value quantity
def highest_qty():
    
    list_qty= []
    for shoe in shoe_list:
        list_qty.append(shoe.quantity)
    # this is the maximum quantity    
    maximum = max(list_qty)    
    for shoe in shoe_list:
        if shoe.quantity== maximum:
            print(shoe)

#==========Main Menu=============

print("Welcome users to the nike warehouse:")

# We create a while loop were it iterates through the menu 
while True:
 
# The menu is dispalyed asks the user to choose:
    menu = input('''\n Please view below and select the following
        C - Capture data about a shoe
        VA - This will view all the shoes
        R  - Find shoe that needs to be restocked
        FS - This will search for a shoe
        VT - Calculate the total value
        S  - Shoe on sale
        e - exit \n''').lower()

# if menu equals c a set of inputs needs to be filled in ny the user 
    if menu == "c" :
        shoe_country = input("Please enter the country of the shoes: ")
        shoe_code = input("Please enter the shoe code: ")
        shoe_name = input("Please enter product name:")
        shoe_cost = float(input("Please enter the cost of the shoe: ")) 
        shoe_quantity = int(input("Please enter the quantity of the shoes: "))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)   
        
# if 2 is selected the view all function will work 
    elif menu == "va":
        view_all()
        
# if 3 is selected the re_stock method is and prints out the lowest quantity         
    elif menu == "r":
        lowest = re_stock()
        
# if 4 is selected it will ask the user to enter the code of a specific shoe                    
    elif menu == "fs" :
        search = input("Please enter the shoe code you looking for:")
        print(f"{search_shoe(search)}")
        
# if 5 is selected it will execute the value_per_item a         
    elif menu == "vt":
        value_per_item()
    
# if 6 is selected it will execute               
    elif menu == "s":
        maximum = highest_qty()
        print(f"This is the shoe with the highest quantity from all your stocking {maximum}")
        highest_qty()

# if e is selected program shuts down      
    elif menu == "e":
        exit()
        
    
  



