#Open user.txt and set to read, create to empty libraries and with a for loop strip and split the data.
#Request the user to input their username and then their password and save each under a different variance name.
#Create a while loop for the input name in the name list, ask to enter the name again until correct.
#Once an option has been chosen by the user in the while loop, write different code for each option.

#=====importing libraries===========
import datetime #geeksforgeeks.org, 2023


#====Login Section====
#I put the login into a definition
def start_up():

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
    return in_name, password, name


#Definition Time:

#Create a definition for the registration of a new user.  It the current user is admin, they can register new users, otherwise a message is relayed the the user does not have clearance.
#There must be a check if the username or password already exists and if the password is correct.

def reg_user(in_name):
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

    elif in_name != "admin":
            print("Sorry, you do not have clearance for registering new users.")

#Create a definition for the addition of a new task.  Create a variable for each of the components and request input for each.
#Use the import statistics to add the date on which the task has been made.
#Add the components in one line to the tasks.txt file.

#I added a description for the format of the date
def add_task():
    assign = input("Please type in who you would like to assign the task to: ")
    title = input("Please type in the name of the task: ")
    describe = input("Please type in the description of the task which you have typed in: ")
    due_date = input("Please type in the date which the task is due in the format (DD MMM YYY): ")
    current = datetime.datetime.now()
    date = current.strftime("%d %b %Y ") #tutorialspoint.com, 2022.

    task_complete = "No"

    login = open("tasks.txt", "a")
    login.write(f"\n{assign}, {title}, {describe}, {date}, {due_date}, {task_complete}")
    login.close()

#Create an empty list for each of the components of a task.  Open the text for reading and strip and split the data.
#Append the components to each list and print individually.

def view_all():
    '''who = []
    title = []
    description = []
    made = []
    due = []
    completed = []'''

    with open("tasks.txt", "r") as view:
        for x in view:
            view_task = x.strip()
            view_task = view_task.split(", ")

            '''who.append(view_task[0])
            title.append(view_task[1])
            description.append(view_task[2])
            made.append(view_task[3])
            due.append(view_task[4])
            completed.append(view_task[5])'''

            print(f"Assigned to: {view_task[0]}")
            print(f"Task Title: {view_task[1]}")
            print(f"Task Description: {view_task[2]}")
            print(f"Date Task was Created: {view_task[3]}")
            print(f"Task Due Date: {view_task[4]}")
            print(f"Completion Status of Task: {view_task[5]}\n")
        #Changed format in which it is printed, runs well.

    view.close()

#Create view_mine definition.
#Add a variable that counts the number of tasks in the for loop and add to the line that is printed.
#
def view_mine():
    number = 0
    with open("tasks.txt", "r") as mark:
        for y in mark:
            mark_task = y.strip()
            mark_task = mark_task.split(", ")
            number = number + 1

            task_name = mark_task[1]
            task_describe = mark_task[2]
            deadline = mark_task[4]
            done = mark_task[5]
            
            if in_name == mark_task[0]:
                fun = (f"Number {number}. {task_name}:\n {task_describe}\n (Due date: {deadline})\n Completed: {done}\n ")
                print(fun)
        chance = input("Would you like to edit a task?  Please type in 'edit' or '-1' to exit: ").lower()

        if chance == "edit":
        
            option = input('''Please select one of the options below to edit:
            n - The name of the user to which the task is written to
            d - The date on which the task is due
            c - The completion status of the task
            : ''').lower()


            if option == "n":
                change = int(input("Please type in the number of the task that you would like to edit: "))

                change = change - 1

                who = input("Type in the user who must take the task responsibility: ")

                with open('tasks.txt', 'r') as mad:
                    fine = [x.strip().split(",") for x in mad.readlines()]

                fine[change][0] = who

                #print(fine)
                
                mad.close()

                with open('tasks.txt', 'w') as tasks:
                    for z in fine:
                        new_var = ",".join(z)
                        tasks.write(new_var + "\n")

          
            elif option == "d":
                new_date = input("Please enter the new due date for the task: ")
                change = int(input("Please type in the number of the task that you would like to edit: "))
                change = change -1

                with open('tasks.txt', 'r+') as lines:
                    lines2 = [y.strip().split(",") for y in lines.readlines()]

                lines2[change][4] = new_date

                lines.close()

                with open('tasks.txt', 'w') as tasks:
                    for q in lines2:
                        lines2_var = ",".join(q)
                        tasks.write(lines2_var + "\n")
                
            elif option == "c":
                change = int(input("Please type in the number of the task that you would like to edit: "))
                change = change - 1
                
                with open('tasks.txt', 'r') as lines:
                    lines2 = [y.strip().split(",") for y in lines.readlines()]

                if "Yes" in lines2[change]:
                    print("This task is already updated as completed.")
                    exit()

                elif "No" in lines2[change]:
                    lines2[change][5] = "Yes"

                lines.close()

                with open('tasks.txt', 'w') as tasks:
                    for q in lines2:
                        var = ",".join(q)
                        tasks.write(var + "\n")

            elif chance == "-1":
                print("Enjoy your day!")

#Create a definition that will display information in task_overview.txt and user_overview.txt
#Information must just be an option on the menu for admin.

def display():
    text1 = open('task_overview.txt', 'w')
    text2 = open('user_overview.txt', 'w')

    text3 = open('tasks.txt', 'r')

    total_tasks = len(text3.readlines())
    text1.write(f"The total tasks that have been generated is:\n{total_tasks}\n")

    text3.close()

    with open('tasks.txt', 'r') as text3:

        yes = 0
        no= 0

        for x in text3:
            num1 = x.strip().split(", ")
            if num1[5] == "Yes":
                yes += 1

            elif num1[5] == "No":
                no += 1

        text1.write(f"The total amount of tasks completed is:\n{yes}\n")
        text1.write(f"The total amount of tasks which are not completed is:\n{no}\n")

        overdue = 0

        for x in text3:
            num3 = x.strip().split(", ")
            if num3[5] == "No" and datetime.datetime.strptime(num3[4], "%d %b %Y") > datetime.datetime.now(): 
                overdue = overdue + 1

        text1.write(f"The amount of tasks overdue is:\n{overdue}\n")

    per_incomplete = round((int(no)/total_tasks*100), 2)
    text1.write(f"The percentage of tasks incomplete is:\n{per_incomplete}%\n")

    per_overdue = round((int(overdue)/total_tasks*100), 2)
    text1.write(f"The percentage of tasks overdue is:\n{per_overdue}%\n")

    text1.close()

    text3 = open('tasks.txt', 'r')

    reading = text3.readlines()

    empty = {}
    for x in reading:
        user_info = x.strip().split(", ")

        user_name = user_info[0]

        if user_name in empty:
            empty[user_name] += 1
        else:
            empty[user_name] = 1       

    text2.write(f"The total amount of users registered is: {len(empty)}\n")

    text2.write(f"The total amount of tasks are: {total_tasks}\n") 

    for user_name, count in empty.items():
        user_tasks = count
        per_tasks = user_tasks/total_tasks*100
        #print(f"User: {user_name}\n")
        #print(f"Total number of tasks assigned to user: {user_tasks}\n")
        #print(f"Percentage of total number of tasks for user: {per_tasks}%\n")

        complete = 0
        overtime = 0
        current = datetime.datetime.now() 

        for y in reading:
            mark_task = y.strip().split(", ")
            if mark_task[0] == user_name:
                if mark_task[5]  == "Yes":
                    complete += 1
                else:
                    if datetime.datetime.strptime(mark_task[4], "%d %b %Y") < current:
                        overtime += 1

        per_complete = complete/user_tasks*100
        per_not_complete = 100 - per_complete
        per_overtime = overtime/user_tasks*100

        text2.write(f"User: {user_name}\n")
        text2.write(f"Total number of tasks assigned to user: {user_tasks}\n")
        text2.write(f"Percentage of total number of tasks for user: {per_tasks}%\n")
        text2.write(f"Percentage of user completed tasks: {per_complete}%\n")
        text2.write(f"Percentage of user incompleted tasks: {per_not_complete}%\n")
        text2.write(f"Percentage of user tasks that are overdue: {per_overtime}%\n")

    text3.close()
    text2.close()

#Create menu option that will only be available to admin to be able to see statistics.
in_name, password, name = start_up()


while True:
    if in_name != "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate Reports
e - Exit
: ''').lower()
        
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
ds - Display Statistics
e - Exit
as - Admin Statistics
: ''').lower()

    print(" ")
    if menu == 'r':
        reg_user(in_name)
        print(" ")
               
    elif menu == 'a':
        add_task()
        print(" ")

    elif menu == 'va':                                     
        view_all()
        print(" ")

#Open the tasks file in read and create a for loop where the data is stripped and split.
# Create an if statement which allows the person who logged in to see only their own tasks.
      
    elif menu == 'vm':
        view_mine()
        print(" ")

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

    elif menu == 'ds':
        display()

    else:
        print("You have made a wrong choice. Please Try again")

#geeksforgeeks.org. 2023. Get Current Date and Time using Python. Reviewed on 6 April 2023. https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
#Hyperiondev. 2023. Task 19, Capstone Project 2. Reviewed on 4 April 2023. https://youtu.be/0HaYhgKba9c
#tutorialspoint.com. 2022. How toGet Formatted Date and Time with Python. Reviewed on 6 April 2023. https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
