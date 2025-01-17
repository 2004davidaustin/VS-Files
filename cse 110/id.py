import re
import datetime


print("\n\n" + "Welcome to IMPORTANT JOB.co, please fill out the following to receive your ID card.")
firstname = input("Your first name: ")
lastname = input("Your last name? ")
email = input("Your email address? ")
phone = input("Your phone number? ")
job = input("Your job title? ")
id = input("Your ID number? ")
hair = input("Your hair color? ")
eyes = input("Your eye color? ")
training = input("Have you completed the training? ")
cookie = input("Have you filled out the required forms to be eligible for free cookies? ")


#Code from google
month = datetime.datetime.now().strftime("%B")
phoneclean = re.sub(r'[^0-9]', '', phone)


print("\n\n" + "YOUR ID CARD:\n-----------------------------------------------")

print(f"{lastname.upper()}, {firstname.capitalize()}")
print(job.title())
print(f"ID: {id}")

print("\n" + email.lower())

#More code with help from google
print(f"({phoneclean[:3]}) {phoneclean[3:6]}-{phoneclean[6:]}")

#Code with help from stack overflow
print("\n" + f"{'Hair: ' + hair.upper():<28} Eyes: {eyes.upper()}")
print(f"{'Month of Sign up: ' + month.upper():<28} Is Trained? [{training.upper()}]")

print("\n" + f"Deserves a cookie? [{cookie.upper()}]")

print("-----------------------------------------------" + "\n\n")