
DICTIONARY = {}

def DISPLAY():
  global DICTIONARY
  print("ALL CONTACTS\n")
  print("NAME CONTACT\n")
  print(DICTIONARY)
   

  print("Do you want to perform more"\
    " operations? (y / n)")

  choice = input().strip()
  if choice == "y":
    main()



def DELETION():
  global DICTIONARY
  print("Enter the contact"\
    " name to be deleted")

  name = input().strip()

  if name in DICTIONARY:
    del(DICTIONARY[name])
    print("Contact Deleted !\n")
  else:
    print("Contact not found !\n")

  print("Do you want to perform more"\
    " operations? (y / n)")

  choice = input().strip()
  if choice == "y":
    main()

# Function to update a contact number
def UPDATION():
  global DICTIONARY
  print("Do you want to update 1)Phone Number 2)Name")
  ONEORTWO=input().strip()
  if ONEORTWO=="1":
    print("Enter the contact name"\
        " to be updated - ")

    name = input().strip()

    if name in DICTIONARY:
        print("Enter the new"\
        " contact number - ")
        phone = int(input())

        DICTIONARY[name] = phone

        print("Contact updated\n")
    else:
        print("Contact not found !\n")
  if ONEORTWO=="2":
    print("Enter the old contact name"\
        " to be updated - ")

    name = input().strip()

    if name in DICTIONARY:
        print("Enter the new"\
        " name - ")
        newname = input().strip()

        DICTIONARY[newname] = DICTIONARY[name]
        del(DICTIONARY[name])
        print("Contact updated\n")
    else:
        print("Contact not found !\n")  

  print("Do you want to perform "\
    "more operations? (y / n)")

  choice = input().strip()
  if choice == "y":
    main()

# Function to store a contact
def INSERTION():
  print("\n\nEnter the name"\
    " and phone number"+\
    " separated by space - ")

  name, phone = map(str, \
          input().strip()\
              .split(" "))

  global DICTIONARY
  if name in DICTIONARY:
    print("Contact Already exists !\n")
  else:
    DICTIONARY[name] = phone
    print("Contact Stored !")

  print("Do you want to perform more"\
    " operations? (y / n)")

  choice = input().strip()
  if choice == "y":
    main()

def EXITNOW():
    exit()

def main():
  print("Please choose any choice"\
    " from below -\n\n\n")
  print("INSERTION (1)")
  print("UPDATION (2)")
  print("DELETION(3)")
  print("DISPLAY(4)")
  print("EXIT(5)")
  choice = int(input())

  choice_dict = {
    1: INSERTION,
    2: UPDATION,
    3: DELETION,
    4: DISPLAY,
    5: EXITNOW
  }

  choice_dict[choice]()


if __name__ == "__main__":
  print(" ***CONTACT BOOK**")

main()
