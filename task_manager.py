#Open user.txt and set to read, create to empty libraries and with a for loop strip and split the data.
#Request the user to input their username and then their password and save each under a different variance name.
#Create a while loop for the input name in the name list, ask to enter the name again until correct.
#Once an option has been chosen by the user in the while loop, write different code for each option.

#=====importing libraries===========
import datetime #geeksforgeeks.org, 2023

#====Login Section====

login = open('user.txt', 'r')

name = []
password = []

for x in login:
    num = x.strip()
    num = num.split(", ")

    name.append(num[0])
    password.append(num[1])

in_name = input("Please enter your username to login: ")

while in_name not in name:
    in_name = input("This username does not exist.  Please try again: ")

print(f"Welcome, {in_name}!")
print(" ")

in_passw = input("Please enter your password to login: ")

while in_passw not in password:
    in_passw = input("The password is incorrect.  Please try again: ")

print(f"Password Correct!")
print(" ")

login.close()

#Create menu option that will only be available to admin to be able to see statistics.

while True:
    if in_name != "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
as - Admin Statistics
: ''').lower()

#If r has been chosen, request the new name and check that is does not already exist in the user.txt file ad save as a new variable.
#Request the user to input a new password and check that it does not exist in the user.txt.
#Confirm that the new password is correct and then save the new username and password in the user.txt file.
#Add an if statement where only admin can register a new user.
    print(" ")
    if menu == 'r':
        if in_name == "admin":
            new_name = input("Please enter the name of the new user: ")

            while new_name in name:
                print("This username already exists.")
                new_name = input("Please type in a new username: ")

            new_password = input("Please enter the password for the new user: ")

            while new_password in password:
                print("This password already exists.")
                new_pasword = input("Please type in a new password: ")

            confirm = input("Please enter the password again to confirm: ")
               
            for x in new_password:
                if new_password != confirm:
                    confirm = input("The password does not match your first attempt.  Please type the password in again: ")
                
            login = open("user.txt", "a")
            login.write(f"\n{new_name}, {new_password}")
            login.close()
            exit()

        elif in_name != "admin":
            print("Sorry, you do not have clearance for registering new users.")
            exit()

#Create a variables for the necessary components with input required from the user.
#Import datetime and set for use of the current date.  Set the date to the same format as in the list.
#Set the completion of the task as no.  Open the tasks.txt file and add all the components in a string.        
        
    elif menu == 'a':
        assign = input("Please type in who you would like to assign the task to: ")
        title = input("Please type in the name of the task: ")
        describe = input("Please type in the description of the task which you have typed in: ")
        due_date = input("Please type in the date which the task is due: ")

        current = datetime.datetime.now()
        date = current.strftime("%d %b %Y ") #tutorialspoint.com, 2022.

        task_complete = "No"

        login = open("tasks.txt", "a")
        login.write(f"\n{assign}, {title}, {describe}, {date}, {due_date}, {task_complete}")
        login.close()
        exit()

#Give each of the components a variable and set it as zero.
#Open the file in read and use a for loop to strip and split the data into the individual components.
#Append each of the variables in the loop.  Print in lists.

    elif menu == 'va':                                     
        who = []
        title = []
        description = []
        made = []
        due = []
        completed = []

        with open("tasks.txt", "r") as view:
            for x in view:
                view_task = x.strip()
                view_task = view_task.split(", ")

                who.append(view_task[0])
                title.append(view_task[1])
                description.append(view_task[2])
                made.append(view_task[3])
                due.append(view_task[4])
                completed.append(view_task[5])

                '''value1 = view_task[0]
                value2 = view_task[1]
                value3 = view_task[2]'''

        print(f"Assigned to:\n {who}\n")
        print(f"Task Title:\n{title}\n")
        print(f"Task Description:\n{description}\n")
        print(f"Date Task was Created:\n{made}\n")
        print(f"Task Due Date:\n{due}\n")
        print(f"Completion Status of Task:\n{completed}\n")

        view.close()
        exit()

#Open the tasks file in read and create a for loop where the data is stripped and split.
# Create an if statement which allows the person who logged in to see only their own tasks.
      
    elif menu == 'vm':
        
        user = []
        with open("tasks.txt", "r") as mark:
            for y in mark:
                mark_task = y.strip()
                mark_task = mark_task.split(", ")

                task_name = mark_task[1]
                task_describe = mark_task[2]
                deadline = mark_task[4]

                if in_name == mark_task[0]:
                    print(f"{task_name}:\n {task_describe} (Due date: {deadline}\n)")

        exit()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

#Open and read the tasks.txt and user.txt file and read the lines, count the lines and print.

    elif menu == 'as':

        text = open("tasks.txt", "r")
        tasks = text.readlines()

        num_task = len(tasks)
        print(f"The total number of tasks are: {num_task}")

        text.close()

        count = open("user.txt", "r")
        count_users = count.readlines()

        num_users = len(count_users)
        print(f"The number of users in this program is: {num_users}")

        count.close()
             
        exit()

    else:
        print("You have made a wrong choice. Please Try again")

#geeksforgeeks.org. 2023. Get Current Date and Time using Python. Reviewed on 6 April 2023. https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
#Hyperiondev. 2023. Task 19, Capstone Project 2. Reviewed on 4 April 2023. https://youtu.be/0HaYhgKba9c
#tutorialspoint.com. 2022. How toGet Formatted Date and Time with Python. Reviewed on 6 April 2023. https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
