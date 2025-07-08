import os 
import random
import time
members_numbers = 1
members_list = {}
class Member:
    def __init__(self,first,last,id,status):
        self.first = first
        self.last = last
        self.id = id
        self.status = status
def Add_member():
  global members_numbers
  first = input('Type your first name: ')
  last = input ('Type your last name: ')
  id = random.randint(111111,999999)
  status = input ('type the status of this member or press enter ')
  if status.strip() == "":
      status = 'unavailable'
      time.sleep(0.5)
      print('opration prossing......')
      time.sleep(0.5)
      print('member added Successfully....')
      time.sleep(0.5)
      print (f'your ID is {id}')
      time.sleep(0.5)
      print('return in 5......')
      time.sleep(1)
      print('return in 4......')
      time.sleep(1)
      print('return in 3......')
      time.sleep(1)
      print('return in 2......')
      time.sleep(1)
      print('return in 1......')
      time.sleep(1)
      members_list[members_numbers] = {'first' : first , 'last':last ,'ID': id,'status' : status}
      members_numbers +=1
      return Member(first,last,id,status)
def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')
def View():
  clear()
  global members_list
  print("\n📋 Members List:\n" + "-" * 40)
  for member_id, info in members_list.items():
    print(f'''
👤 ID : {info['ID']}
   First name : {info['first']}
   Last name  : {info['last']}
   Status     : {info['status']}
----------------------
    ''')
    time.sleep(6)
    clear()
def search():
  global members_list
  print('''
Search by:
  1. ID
  2. First name
  3. Last name
  4. Status
  ''')
  choice = input("Enter the number of the field to search by: ").strip()
  field_map = {
    "1": "ID",
    "2": "first",
    "3": "last",
    "4": "status"
  }

  if choice in field_map:
    search_field = field_map[choice]
    search_value = input(f"Enter the {search_field} to search for: ").strip()
    found = False
    for member_id, info in members_list.items():
      if str(info.get(search_field, "")).lower() == search_value.lower():
        print(f'''
👤 ID : {info['ID']}
   First name : {info['first']}
   Last name  : {info['last']}
   Status     : {info['status']}
----------------------
        ''')
        found = True
    if not found:
      print("⚠️ Member not found.")
  else:
    print("❌ Invalid choice.")
  time.sleep(6)
  clear()
while True:
    print ('            Welcome at Gym Membership ')
    choice = int(input('''
Please make your choice 
1-Add member
2- View members
3-search on a member
4-Exiting
 : '''))
    print( 'Prepering....')
    time.sleep(0.5)
    print( '3')
    time.sleep(1)
    print( '2')
    time.sleep(1)
    print( '1')
    time.sleep(1)
    clear()
    if choice == 1:
        member1 = Add_member()
    elif choice == 2:
        View()
    elif choice == 3:
        search()
    elif choice == 4:
        print ('Exiting..........')
        time.sleep(1)
        break
    else:
        print('❌️Invalid choice')
    replay = input('are you want to continue yes/no: ')
    if replay == 'yes':
        print('return to mian menu')
        time.sleep(1)
        clear()
    else:
        print('thank you for using our app')
 