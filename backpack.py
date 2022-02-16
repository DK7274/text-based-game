
a = 0
pickup = 0
action = 0
items = ["Sword","empty","empty", "empty"] #an array that shows the items in your backpack
while True:
  action = input("what do you do next?\n") #asks what activity you do next
  if action == "check bag":
    for a in items: 
      print(a) #lists the items in your bag
  if action == "pick up":
    pickup = input("what do you want to pick up?\n")
    for a in range(len(items)):
      if items[a] == "empty":
        print("you pick up the " + pickup)
        items[a] = pickup
        break
    else:
      action = input("your bag is full! do you want to replace an item?\n")
      if action == "yes":
        for a in items:
          print(a)
        action = input("what do you want to replace? \n")
        for a in range(len(items)):
          if items[a] == action:
            items[a] = pickup
            print("you replaced " + action + " with " + pickup)
            break
          else:
            print("you do not have " + action + " in your bag!")
      else: break