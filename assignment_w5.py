#Q1.
contact = {
    'ram' : 'ram@gmail.com' , 
    'shyam' : 'shyam@gmail.com'
}
user = str(input("Enter user name : "))

if user in contact :
    print(user, ": " , contact[user])
else:
    print("Contact not Found")



#Q2.
shoping_list = { 'milk', 'bread', 'eggs'}
bought = {'eggs', 'bread'}
unbought = shoping_list.difference(bought)
if unbought:
    print(unbought)
    
else :
    print("Shopping complete")



#Q3.

class_list = ["ram", "sita", "laxman"]
new_student = "hari" 

if new_student not in class_list:
    class_list.append(new_student)
    print(f"Confirmation: {new_student} has been added.")
else:
    print("already present")


#Q4
votes = ["Blue", "Red", "Blue", "Green", "Blue"]

blue_count = votes.count("Blue")

if blue_count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")


#Q5
grades = {"ram": 92, "sita": 88}
student_name = "Ram"  

if student_name in grades:
    print(grades[student_name])
else:
    print("grade is not available")


#Q6

applicant = { 
    "name": "Priya", 
    "skills": ["Java", "SQL"], 
    "experience_years": 1
}

required_skills = {"Python", "Java"}


has_required_skill = any(skill in required_skills for skill in applicant['skills'])

if has_required_skill and applicant['experience_years'] >= 2:
    print("priya qualifies")
else:
    print("priya does not qualify")



#Q7.

banned_items = {"scissors", "knife", "lighter"}

weight = float(input("Enter baggage weight (in kg): "))
item = input("Enter the name of the item being carried: ").lower()

if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")


#Q8.

salary = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}

salary['emp3']['salary'] = 8500
print(salary)


#Q9.

ram_items = {"apple", "banana", "orange"}
laxman_items = {"grapes", "mango"}

if ram_items.isdisjoint(laxman_items):
    print("they picked completely different items")
else:
    print("they have some common items")


#Q10.

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {40, 50}          
my_dict = {'b': 'Zone B'}  
val = 20
if (val in my_list) and (val in my_tuple):
    if ('b' in my_dict) and (val not in my_set):
        print('Path A') 
    else:
        print('Path B')  
else:
    print('Path C')     



#Q11.
# The value for a becomes 30

#Q12.
# [1,2,3]

#Q13.
# Not Found


#Q15.
# my_set.add(40)


#Q16.
menu = {"Pizza": 15, "Burger": 10, "Salad": 8}
order = 'Pizza'

if order in menu:
    print(menu[order])
else:
    print("item not found")


#Q17.

student_data = {"name": "Sam", "score": 85}

if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)


#Q18.

database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")


#Q19.

emails = ['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}
current_email = 'hari77@test.com'

if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")

#Q20.

inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', '29'}
target = 'B2'

if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")
else:
    print("invalid zone")


#Q21.

valid_courses = {"python", "robotics", "java"}
hs_grades = [9, 10, 11, 12]

name = input("Enter student name: ")
course = input("Enter requested course: ").lower()
grade = int(input("Enter high school grade level (9-12): "))

student_records = {
    "name": name,
    "course": course,
    "grade": grade
}

if student_records["course"] not in valid_courses:
    print(f"{student_records['name']} selected an invalid course.")
else:
    if student_records["grade"] < 9:
        print("grade too low")
    elif student_records["grade"] > 12:
        print("grade too high")
    else:
        if student_records["course"] == "robotics" and student_records["grade"] == 9:
            print(f"{student_records['name']} is not eligible for {student_records['course']} grade too low")
        else:
            print(f"{student_records['name']} is approved for {student_records['course']}")
