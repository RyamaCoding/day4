row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Please input two numbers between 1 and 3: ")

horizontal = int(position[0])
vertical = int(position[1])

if horizontal < 1 or horizontal > 3 or vertical < 1 or vertical > 3:
  print("Please enter a valid number between 1 and 3")

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")