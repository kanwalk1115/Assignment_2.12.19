user_input= ""
stores = []

# Creating menu
def menu():
  print("Enter 1 to add store: ")
  print("Enter 2 to add an item to a store: ")
  print("Enter 3 to view all stores: ")
  print("Enter q to quit: ")

menu()

class Store:
    def __init__(self,name):
        self.name = name


def add_store():
    name = input("Enter store name: ")
    store = Store(name)
    stores.append(store)

class GroceryItem:
  def _init_(self, item, price, quantity):
    self.item = item
    self.price = price
    self.quantity = quantity

def add_item_store():
    item = input("Select store: " )
      if user_input == "A"
        print(index 0)



def view_all_stores():
    for store in stores:
        print({store.name})

while user_input != "q":
  user_input = input("Enter your choice: ")
  if user_input == "1":
    add_store()
  elif user_input == "2":
    add_item_store()
  elif user_input == "3":
    view_all_stores()






i1 = GroceryItem(milk, 3.25, 2)
i2 = GroceryItem(soda, 1.25, 1)
i3 = GroceryItem(fish, 8.80, 1)
i4 = GroceryItem(paper, 4.50, 2)
i5 = GroceryItem(napkins, 2.50, 1)
i6 = GroceryItem(plates, 6.78, 1)
i7 = GroceryItem(chips, 2.50, 2)
i8 = GroceryItem(chicken, 7.50, 2)
i9 = GroceryItem(beef, 9.30, 1)
i10 = GroceryItem(eggs, 2.15, 2)
i11 = GroceryItem(sugar, 2.50, 1)
i12 = GroceryItem(salt, 0.75, 2)
i13 = GroceryItem(pepper, 3.00, 1)
i14 = GroceryItem(honey, 3.75, 1)

print(i13.item)
print(i13.price)
print(i13.quantity)

class ShoppingList:
    def_init_(self, name, grocery_item)
    self.name = name
    self.grocery_item = GroceryItem
