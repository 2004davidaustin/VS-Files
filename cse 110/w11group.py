#name id_number job_title salary

with open("hr_system.txt") as hr_system : 
    for person in hr_system : 
         person = person.strip()
         person = person.split(" ")

         print(f"Name: {person[0]}, Title: {person[2]}")
