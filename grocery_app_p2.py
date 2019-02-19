user_input = ""
stores = []

class Store:
  def __init__(self,name):
    self.name = name
    self.grocery_items = []



class Item:
  def __init__(self,name,price,quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

def menu():
  print("Enter 1 to add a store: ")
  print("Enter 2 to add item: ")
  print("Enter 3 to view all stores: ")
  print("Enter q to quit")


def add_store():
  name = input("Enter name of store: ")
  store = Store(name)
  stores.append(store)

def view_all_stores():

  for index in range(0,len(stores)):
    store = stores[index]
    print(f"{index+1} - {store.name}")
    for item in store.grocery_items:
      print(f"{item.name} - {item.price} - {item.quantity}")


def add_grocery_item():
  view_all_stores()
  store_number = int(input("Enter store number to add an item: "))
  # get the selected shopping list
  store = stores[store_number - 1]
  name = input("Enter name of item: ")
  price = float(input("Enter price of item"))
  quantity = int(input("Enter quantity of item: "))
  item = Item(name,price,quantity)

  # adding grocery item to shopping list
  store.grocery_items.append(item)

while user_input != 'q':
  menu()
  user_input = input("Enter your choice: ")
  if user_input == "1":
    add_store()
  elif user_input == "2":
    add_grocery_item()
  elif user_input == "3":
    view_all_stores()

#create a function to add the prices of all items together
