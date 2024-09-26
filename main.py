# How can we clear the screen?
# IS there a better way to transition?

print("Registration: Please enter and respond with correct credentials")
print(" ") #this creates a space between the lines on the output
print(" ")

first_name= input("Please enter your first name: ") #'first_name is the variable'
print(" ")
middle_inital= input("Please enter your middle inital; if none, enter a space: ")
print(" ")
last_name= input("Please enter your last name: ")
print(" ")
print(f"Hello, {first_name} {middle_inital} {last_name}!") #the f string is like instruction for it to go back to a past variables input
print(" ")

while True:
  user_input = input("Do you know your billing address? (yes/no): ")

  if user_input in ["yes", "Yes", "Y", "y", "YES"]: 
      print("Stellar!")
      break  # Exit the loop since the user knows their address
  elif user_input in ["no", "No", "N", "n", "NO"]:
      print("Please figure it out.. then re-run this page!")
      exit()  # Exit the program or you could use `break` or `continue` to restart the loop
  else:
      print("Invalid input. Please enter 'yes'or 'no'.")

# Proceed to collect address details
street_address = input(f"Now {first_name}, please enter your Street Address: ")
print(" ")

city = input("Great! Now enter your current City: ")
print(" ")

print("Awesome!")
state = input("Enter your state abbreviation: ")
print("That seems about right!")
print(" ")
zip_code = input("Please enter your zip code: ")
print(" ")

print("Sweeeeeet ;)")
print(" ")

phone_number = input(f"We need to know how to contact you, {first_name}. What is your phone number?: ")
print(f"I'll give you a call later {first_name}.")
print(" ")
print("ONE LAST question, what is your email address?")
email_address = input("Email address: ")
print("Thanks!")

# Display the information back to the user
print(f"\nYou entered the following information:") #You put a '\n' into a string to quickly and easily create a newline. This happens automatically after a print-statement, as you probably know.
print(f"{first_name}")
print(f"{middle_inital}")
print(f"{last_name}")
print(f"{street_address}")
print(f"{city}")
print(f"{state}")
print(f"{zip_code}")
print(f"{phone_number}")
print(f"{email_address}")



# Ask the user if the information is correct
confirmation = input("\nIs this information correct? (yes/no): ")
  
# Check the user's response
if confirmation.lower() in ['yes', 'y']:
    print("Thank you! Your information has been saved.")
    exit()
else:
    print("Please re-enter your information.")
    exit()
