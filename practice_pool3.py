from datetime import datetime
now = datetime.now()

pool_tables = []
user_input = ""

class PoolTable:
  def __init__(self,table_no):
    self.table_no = table_no
    self.is_available = "Available"
    self.start_time = now.strftime("Date: %b %d,%Y || Time: %H:%M:%S")
    self.end_time = datetime.now()
    # start time
    # end time

  def __repr__(self):
      return(f"{self.table_no} is {self.is_available}")

  def checkout(self):
    self.is_available = "Occupied"
    self.start_time = now.strftime("Date: %b %d,%Y || Time: %H:%M:%S")

for index in range(1,13):
  pool_table = PoolTable(index)
  pool_tables.append(pool_table)

for pool_table in pool_tables:
    print(f"Table: {pool_table}")

user_input = int(input("Which table would you like to use?: "))


pool_table.checkout(self)
