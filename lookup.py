import sqlite3
import json
import xml.etree.ElementTree as ET


try:
    conn = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

cur = conn.cursor()

def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

#If the user chose to store data in a json file, the file will be created and the data iterated thorugh with a for loop.
def store_data_as_json(data, filename):
    records = [x[0] for x in data]

    with open(filename, "w") as jsonfile:
        json.dump(records, jsonfile, indent=2)
    print("Data has been saved.")

#If the user chose to store data in a xml file, the file will be created and the data iterated through with a for loop.
#The root element and tree element must be created to store data.
def store_data_as_xml(data, filename):   
        
    root = ET.Element('data')

    for x in data:                         
        record_element = ET.Element('record')
        for key, value in x.items():
            data_element = ET.Element(key)
            data_element.text = str(value)
                
        root.append(record_element)

    tree = ET.ElementTree(root)
    tree.write(filename)
    print("Data has been saved.")


def offer_to_store(data):  #User has option to choose if they want to save the data and under what name
    while True:
        print("Would you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                store_data_as_xml(data, filename)
                break
            elif ext == 'json':
                store_data_as_json(data, filename)
                break
            else:
                print("Invalid file extension. Please use .xml or .json")


        elif choice == 'n':
            break

        else:
            print("Invalid choice")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()

    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]

    if command == 'd': # this prints all student names and surnames
        data = cur.execute("SELECT * FROM Student")
        for _, firstname, surname, _, _ in data:
            print(f"{firstname} {surname}")
        
    elif command == 'vs': # view subjects by student_id
        if usage_is_incorrect(user_input, 1):
            student_id = args[0]
            student_id = ''.join(student_id)

        data = cur.execute('''SELECT course_code FROM StudentCourse WHERE student_id = ?''', (student_id,))
        print(f"Subjects taken by student {student_id} are:")

        for x in data:
            print(x)

        offer_to_store(data)

    elif command == 'la':# list address by name and surname
        if usage_is_incorrect(user_input, 2):
            firstname, surname = args[0], args[1]
            data = cur.execute(f'''SELECT Address.street, Address.city FROM Address INNER JOIN Student
            ON Address.address_id = Student.address_id 
            WHERE Student.first_name = {firstname} AND Student.last_name = {surname} ''') #Can I do this?

        # Run SQL query and store in data

        print(f"The address for {firstname} {surname} is: ")

        for x in data:
            print(x)

        offer_to_store(data)
    
    elif command == 'lr':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            student_id = args[0]
            data = cur.execute('''SELECT review_text, completeness, efficiency, style, document
            FROM Review WHERE student_id = ?''', (student_id,))

        # Run SQL query and store in data

        print(f"The reviews written by the student are as follows: ")

        for x in data:
            print(x)

        offer_to_store(data)
    
    elif command == 'lc': #List all the courses given by the teacher
        if usage_is_incorrect(user_input, 1):
            teacher_id = args[0]
            data = cur.execute('''SELECT course_name FROM Course WHERE teacher_id = ?''', (teacher_id,))

        print(f"The courses given by the teacher {teacher_id} are as follows: ")

        for x in data:
            print(x)

        offer_to_store(data)


    elif command == 'lnc': # list all students who haven't completed their course
        data = cur.execute('''SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name
        FROM Student 
        INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
        INNER JOIN Course ON StudentCourse.course_code = Course.course_code
        WHERE StudentCourse.is_complete = 0''')

        # Run SQL query and store in data

        print("All the students who have not completed their courses:")
        for x in data:
            print(x)

        offer_to_store(data)

    elif command == 'lf':# list all students who have completed their course and got a mark <= 30
        data = cur.execute('''SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name, StudentCourse.mark
        FROM Student
        INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
        INNER JOIN Course ON StudentCourse.course_code = Course.course_code
        WHERE StudentCourse.is_complete = 1 AND StudentCourse.mark <= 30''')

        # Run SQL query and store in data

        print("All the students who have completed their course and got a mark above 30: ")

        for x in data:
            print(x)

        offer_to_store(data)
    
    elif command == 'e':
        print("Programme exited successfully!")
        break
    
    else:
        print(f"Incorrect command: '{command}'")
    
conn.close()
    
