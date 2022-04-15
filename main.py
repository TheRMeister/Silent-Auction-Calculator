from replit import clear
import art

#print display
print(art.logo)
print("Welcome to the silent auction.")

#Initialize variables

running = True
bidders = {}
bids = []
names = []
#define a function to add the names and bids to the dictionary

def add_to_bidders(name,bid):
  bidders[name] = bid
#create loop to keep the menu up and get user inputs
while running == True:
  name = input("What is your name?\n")
  bid = int(input("What is your bid amount?\n$"))
  other_bidders = input("Are there any other bidders? Enter 'yes' or 'no.'\n").lower()
  # Calling the function to add the user inputs
  add_to_bidders(name,bid)
  # Clear the menu after each input is taken
  clear()
  if other_bidders == "yes":
    running = True
  elif other_bidders == "no":
    running = False
    clear()
