import os
import time


def clear_terminal():
  '''
  Clear the terminal
  '''
  os.system('cls' if os.name == 'nt' else 'clear')


class Member:

  def __init__(self, id, first_name, last_name, status):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.status = status

  def display(self):
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")
    print(f"Membership ID: {self.id}")
    print(f"Membership status: {self.status}")
    print("-" * 20)


def create_member():
  """
  Creat objects by using the inputs of the user
  """
  f_name = input("Enter your first name: ")
  l_name = input("Enter your last name: ")
  while True:
    member_id = input("Enter your membership ID: ") # unique
    if not member_id.isdigit():
      print("Invalid input.")
      continue
    break
  status = input("Enter membership status, or click enter: ")
  if not status:
    status = 'inactive'

  return Member(member_id, f_name, l_name, status) # object

def searching(members):
  '''
  search for a member in data base by Name, ID or Status
  '''
  found = False
  print("Search by:")
  print("""
1: Membership ID
2: Fisrt name
3: Membership status
  """)
  choice = input("Enter your choice: ")
  if choice == '1':
    id = input("Enter the membership ID to search: ")
    print("\n Waiting.....")
    time.sleep(2)
    clear_terminal()
    for member in members:
      if member.id == id:
        print("Member found:\n")
        member.display()
        found = True

  elif choice == '2':
    first_name = input("Enter the first name for search: ")
    print("\n Waiting.....")
    time.sleep(2)
    clear_terminal()
    for member in members:
      if member.first_name.lower() == first_name.lower():
        print("Member found:\n")
        member.display()
        found = True
  elif choice == '3':
    status = input("Enter the membership status t search (active/inactive): ")
    print("\n Waiting.....")
    time.sleep(2)
    clear_terminal()
    for member in members:
      if member.status.lower() == status.lower():
        print("Member found:\n")
        member.display()
        found = True
  else:
    print("Invalid input.")
    found = True

  if not found:
    print("this member isn't found.") # معدله من الحل


# def searching(members):
#   '''
#   search for a member in data base by Name, ID or Status
#   '''
#   print("Search by:")
#   print("""
# 1: Membership ID
# 2: Fisrt name
# 3: Membership status
#   """)
#   found_member = []
#   choice = input("Enter your choice: ")
#   if choice == '1':
#     id = input("Enter the membership ID to search: ")
#     for member in members:
#       if member.id == id:
#         found_member.append(member)
#         break  # unque ID
#   elif choice == '2':
#     first_name = input("Enter the first name for search: ")
#     for member in members:
#       if member.first_name.lower() == first_name.lower():
#         found_member.append(member)
#   elif choice == '3':
#     status = input("Enter the membership status to search (active/inactive): ")
#     for member in members:
#       if member.status.lower() == status.lower():
#         found_member.append(member)
#   else:
#     print("Invalid input.")
#   if found_member:
#     print("\n Waiting.....")
#     time.sleep(2)
#     clear_terminal()
#     print("Found member:\n")
#     for x in found_member:
#       x.display()
#   else:
#     print("this member isn't found.")


# data base of members
members_data = []


def menu():
  """
  It displays the main menu
  """
  while True:
    print("\nWelcome to Gym Membership management...\n")
    print("Choose an Action:\n")
    print("1: Add new member")
    print("2: Display all members")
    print("3: Search for member")
    print("4: Exit")
    choice = input("Enter your choice: ")
    clear_terminal()
    time.sleep(1)
    # Adding member
    if choice == "1":
      members_data.append(create_member())
      print("Loading....")
      time.sleep(2)
      print("\n  Member added successfully!")
      time.sleep(2)
      clear_terminal()
      # Displaying the members
    elif choice == "2":
      if members_data:
        print("Displaying all members\n")
        time.sleep(1)
        for member in members_data:
          member.display()
      else:
        print("There aren't members in data base.")
    # Searching
    elif choice == "3":
      if members_data:
        searching(members_data)
      else:
        print("No members to search!")
    elif choice == "4":
      print("Exiting...")
      break
    else:
      print("Invalid choice, Pls try agian.")
    time.sleep(3)


# Start of the code
menu()
