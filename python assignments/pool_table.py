#
from datetime import datetime

pool_tables = []

def creating_tables():
    for index in range(1,13):
      pool_table= PoolTable(index)
      pool_tables.append(pool_table)
      print(pool_tables)

def view_all_tables():
    for p in pool_tables:
        print(f'Table number:{p.table_no}')

class PoolTable:
    def __init__(self, number):
        self.number = number
        self.availabilty = True
        self.start_time = datetime.now()
        self.end_time = datetime.now()

    def checking_in(self):
       view_all_tables()
       self.availabilty = True
       start.start_time = datetime.now()

def menu():
    print("Press 1 t check-in." )
    print("Press 2 to check-out. ")
    print("Press 3 to exit. ")
print ('Welcome to U of H Pool Table Check-in and Check -out App!')
menu()
user_input = ""
while user_input != "3":
    if user_input == "1" :
      checking_in()
    if user_input == "2" :
      checking_out()
# for index in range(0,len(pool_tables)):
   #pool_table= PoolTable(index)
  # pool_tables.append(pool_table)
  # print(f"{index+1} - {pool_table.number}")
 #for item in pool_table:
  # print(f"{pool_table.number} - {pool_table.availabilty}")
