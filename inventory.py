#Import tabulate to use later on.
#Create a class "Shoes" and add country, code, product, cost and quantity.
#Create a function in the class that will return the cost, return the quantity and return the components in a string.
#Create an empty list. Create a function that reads the data of the shoes and call this function just before the menu has to run.

from tabulate import tabulate
#AskPython.com, 2023.

class Shoes():

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"   


shoe_list = []  

def read_shoes_data():
    file = None
    
    try:
        num = 0
        with open("inventory.txt", "r") as text:
            for x in text:
                if num != 0:
                    line = x.strip().split(",")                    
                    shoe_list.append(Shoes(line[0], line[1], line[2], float(line[3]), int(line[4])))
                num+=1
                    
    except FileNotFoundError as error:
        print("We are sorry, this file could not be found.")

#Request user input for each of the characteristics of the shoe and append to the shoe_list.
#Print the new product to show the user that it has been added.

def capture_shoes():
    country = input("Please enter the country where the shoes are: ")
    code = input("Please enter the code of the shoe: ")
    product = input("Please enter the product name: ")
    cost = input("Please enter the cost of a pair of shoes: ")
    quantity = input("Please enter the quantity of shoes in stock: ")

    new_product = Shoes(country, code, product, cost, quantity)
    shoe_list.append(new_product)
    print(f"New product {country}, {code}, {product}, {cost}, {quantity} has been added.")

#Create an empty list and create the names for the headers.
#Create a for loop for the shoe_list and append the different characteristics to the empty list.
#Tabulate the new list with the headers and use fancy_grid, print the table.

def view_all():
    data1 = []
    headers = ("Country", "Code", "Product", "Cost", "Quantity")

    for y in shoe_list:
        data1.append([y.country, y.code, y.product, y.cost, y.quantity])

    table = tabulate(data1, headers=headers, tablefmt="fancy_grid")
    return print(table)

#Determine the minimum amount of shoes in the text and print the product name with the current quantity.
#Request user input and ask if they would like to put in an order.
#If yes, request user input for an order for more stock, add the new stock to current stock.
#Open the text file on write and use a for loop to re-write the code.
#Elif print "No new orders made."

def re_stock():
    
    low = min(shoe_list, key = Shoes.get_quantity)
    print(f"You have the lowest stock of the {low.product} with a stock level of {low.quantity}")
    restock = input(f"Would you like to restock the {low.product}?  Enter Yes or No: ").lower()
  
    if restock == "yes":
        more_quantity = int(input("Please enter the amount of shoes you would like to order: "))
        low.quantity = low.quantity + more_quantity

        with open('inventory.txt', 'w') as lines:
            for z in shoe_list:
                lines.write(f"{z.country},{z.code},{z.product},{z.cost},{z.quantity}\n")

        print("Your Purchase Order for more stock has been made successfully.\n")

    elif restock == "no":
        print("No new orders made.\n")

#Request user input for the code of the shoe which they are looking for.
#Use a for loop and if the code is in the text, print the product information.
#Else print that the code does not exist and request code input.

def search_shoe():
    code_search = input("Please enter the code of the shoes which you are looking for: ")
    for x in shoe_list:
        if x.code == code_search:
            print(x)
        else:
            print("Sorry, that code does not exist.")
            input("Please enter the code of the shoes which you are looking for: ")

#Use a for loop and multiply the cost and the quantity with one another.
#Print the product name and value of the stock.

def value_per_item():
    for x in shoe_list:
        value = round((x.cost * x.quantity), 2)
        print(f"Product: {x.product}; Value: R{value}")        

#Determine the highest number in the shoe_list and use the get_quantity function to get that.
#Print the name of the product as a product on sale.

def highest_qty():
 
    high = max(shoe_list, key = Shoes.get_quantity)

    print(f"{high.product} is on Sale!\n")

read_shoes_data()

#Create a while loop as True where the user is requested to pick a number on a menu list.
#For each of the menu options, call one of the functions.
#Exit on 8 and request new input when wrong input has been given.

while True:
    menu = input('''Please select an option by typing in a number from the menu below:
1- Read Shoes Data
2- Add a New Shoe
3- View All Data
4- Restock Shoes
5- Search for a Shoe
6- Value per Item
7- Highest Quantity Shoe
8- Exit
:''')
    
    if menu == "1":
        for x in shoe_list:
            print(x, "\n")

    elif menu == "2":
        capture_shoes()

    elif menu == "3":
        view_all()

    elif menu == "4":
        re_stock()

    elif menu == "5":
        search_shoe()

    elif menu == "6":
        value_per_item()


    elif menu == "7":
        highest_qty()

    elif menu == "8":
        break

    else:
        print("This is not a valid option.  Please try again.\n")

#AskPython.com. 2023. Python Tabulate Module: How to Easily Create Tables in Python? Reviewed on 7 May 2023. https://www.askpython.com/python-modules/tabulate-tables-in-python
#Hyperion Development. 2018. Capstone Project IV- Object-Orientated programming. Reviewed on 7 May 2023. https://www.dropbox.com/s/5o0nvcjxnez37yq/DS%20L1T30%20-%20Capstone%20Project%20IV%20-%20OOP.pdf?dl=0
#Hyperion Development. 2023. Video: Capstone Project IV- OOP. Reviewed on 7 May 2023. https://www.hyperiondev.com/portal/#
#Phiri, S. 2023. Mentor Session. (My Python wasn't downloaded correctly and he helped me to install pip so I can use tabulate.)
#Tshananda, S. 2023. Mentor Session. (My list kept throwing a index error.)