Full_name = "Ethan Hall"
Student_email = "ehall3@aggies.ncat.edu"
Hometown = "Raleigh, NC"
Graduation_semester = "Spring 2029"
Major = "Computer Science"

Current_list = ["COMP 163", "MATH 131", "ENG 100", "HIS 106", "GEEN 111", "COMP 121"]
Complete_list = ["Math 130"]
Credit_hours = [3, 3, 3, 1, 1, 4]
GPA_history = [3.2, 3.6, 3.4, 3.6]
emergency_contact = ("Mom", "Jane Doe", "704-555-0199")
Home_address = ("456 Oak Street", "Charlotte", "NC", "28202")

Instagram_info = ("Instagram", "@kasbandit", 689)
Twitter_info = ("Twitter", "@jordandev", 127)
Birthday_tuple = ("Birthday", "5", "11", "2007")
Current_skills = {"Time management", "Photography", "Problem solving", "Python basics"}
Skills_to_learn = {'Data structures', 'Web design', 'JavaScript', 'Git', 'Public speaking'}
Career_interests = {"Software development", "Web development", "Data science", "Game development"}
Hobbies_set = {"Gaming", "Photography", "Gym", "Music"}
Entertainment_backlog_set = {"One Piece", "Snowfall", "Dr. Stone", "DanDaDan", "Kaiju No. 8"}

course_credits = {
    "COMP 163": 3,
    "MATH 131": 4,
    "ENG 100": 3,
    "HIS 106": 3,
    "GEEN 111": 1,
    "COMP 121": 1,
}

course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 131": "Dr. Lee",
    "ENG 100": "Dr. Martinez",
    "HIS 106": "Dr. Brown",
    "GEEN 111": "Dr. Parrish",
    "COMP 121": "Prof. Rhodes"
}

course_rooms = {
    "COMP 163": "Martin 300",
    "MATH 131": "Marteena 233",
    "ENG 100": "Crosby 121",
    "HIS 106": "Crosby 210",
    "COMP 121": "Graham 206",
    "GEEN 111": "Mcnair 101"
}

Monthly_budget = {
    "Food": 40,
    "Entertainment": 20,
    "Books": 0,
    "Transportation": 80
}

Study_hours_per = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}

Contact_directory = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {Full_name} |", end=" ")
print(f"Email: {Student_email}")
print(f"From: {Hometown} |", end=" ")
print(f"Graduating: {Graduation_semester}")
print(f"Major: {Major}")
print()
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {sum(Credit_hours)} credits across {len(Current_list)} courses")
print(f"Cumulative GPA: {round(sum(GPA_history)/len(GPA_history), 2)}")
print(f"Weekly Study Time: {sum(Study_hours_per.values())} hours")
print(f"Academic Investment: ${sum(Study_hours_per.values()) / 5} per study hour")
print()
print(f"Current Courses:")
print(f"{Current_list[0]} - {Credit_hours[0]} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"{Current_list[1]} - {Credit_hours[1]} credits - {course_professors['MATH 131']} - {course_rooms['MATH 131']}")
print(f"{Current_list[2]} - {Credit_hours[2]} credits - {course_professors['ENG 100']} - {course_rooms['ENG 100']}")
print(f"{Current_list[3]} - {Credit_hours[3]} credits - {course_professors['HIS 106']} - {course_rooms['HIS 106']}")
print(f"{Current_list[4]} - {Credit_hours[4]} credits - {course_professors['COMP 121']} - {course_rooms['COMP 121']}")
print(f"{Current_list[5]} - {Credit_hours[5]} credits - {course_professors['GEEN 111']} - {course_rooms['GEEN 111']}")

print()
print(f"=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {Current_skills}")
print(f"Learning Goals: {Skills_to_learn}")
print(f"Career Interests: {Career_interests}")
print(f"Skills Currently Have: {len(Current_skills)}")
print(f"Skills Want to Learn: {len(Skills_to_learn)}")
print()
print(f"=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${sum(Monthly_budget.values())}")
print(f"Food: ${Monthly_budget['Food']} (${round(Monthly_budget['Food'] / 30, 2)}/day)")
print(f"Entertainment: ${Monthly_budget['Entertainment']}")
print(f"Books: ${Monthly_budget['Books']}")
print(f"Transportation: ${Monthly_budget['Transportation']}")
print(f"Annual Projection: ${sum(Monthly_budget.values()) * 12}")
print()
print(f"=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {Home_address[0]}, {Home_address[1]}, {Home_address[2]} {Home_address[3]}")
print(f"Social Media Presence: {Instagram_info[2] + Twitter_info[2]} followers across 2 platforms")
print(f"Key Contacts: {len(Contact_directory)} people in directory")
print()
print(f"=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(Complete_list)}")
print(f"Current Academic Load: {sum(Study_hours_per.values()) + sum(course_credits.values())} weekly commitments")
print(f"Entertainment Backlog: {len(Entertainment_backlog_set)} items")
print(f"Current Hobbies: {len(Hobbies_set)} activities")

print(f"================================================================")




