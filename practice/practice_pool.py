
from datetime import datetime, timedelta

pool_tables = []

class PoolTable:
  def __init__(self,table_no):
    self.table_no = table_no
    self.start_time = ""
    self.end_time = ""
    self.total_time = 0

  def as_dictionary(self):
      return self.__dict__


  def checkout(self):
    self.is_available = False
    self.total_time = datetime.now()

for index in range(1,13):
  pool_table = PoolTable(index)
  pool_tables.append(pool_table)


pool_table = pool_tables[10]
pool_table.checkout()




def menu():
    print("Press 1 t check-in." )
    print("Press 2 to check-out. ")
    print("Press 3 to exit. ")
print ('Welcome to U of H Pool Table Check-in and Check -out App!')
menu()
user_input = ""
while user_input != "3":
    if user_input == "1" :
      print(pool_tables)

    if user_input == "2" :
      checking_out()
