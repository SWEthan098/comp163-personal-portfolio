Full_name = "Jordan Smith" 
Student_email = "jsmith@ncat.edu"
Hometown = "Charlotte, NC"
Graduation_semester = "Spring 2028"
Major = "Computer Science"

Current_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
Complete_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
Credit_hours = [3, 3, 3, 3]
GPA_history = [3.2, 3.6, 3.4, 3.7]
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
Home_address = ("456 Oak Street", "Charlotte", "NC", "28202")

Instagram_info = ("Instagram", "@jordan_codes", 312)
Twitter_info = ("Twitter", "@jordandev", 127)
Birthday_tuple = ("Birthday", "5", "22", "2006")
Current_skills = {"Time management", "Photography", "Problem solving", "HTML", "Python basics"}
Skills_to_learn = {'Data structures', 'Web design', 'JavaScript', 'Git', 'Public speaking'}
Career_interests = {"Software development", "Web development", "Data science", "Game development"}
Hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
Entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

course_credits = {
    "COMP 163": 3,
    "MATH 150": 3,
    "ENG 101": 3,
    "HIS 105": 3
}

course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}

course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210",
}

Monthly_budget = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
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
print(f"{Current_list[1]} - {Credit_hours[1]} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(f"{Current_list[2]} - {Credit_hours[2]} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(f"{Current_list[3]} - {Credit_hours[3]} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
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
