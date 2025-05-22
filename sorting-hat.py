
Grf = 0
Rav = 0
Huf = 0
Sly = 0

ans1 = int(input("Q1) Do you like Dawn or Dusk \n 1) Dawn\n 2) Dusk\n"))
if ans1 == 1:
  Grf += 1
  Rav += 1
elif ans1 == 2:
  Huf += 1 
  Sly += 1
else:
  print("Wrong Input")

ans2 = int(input("Q2) When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))
if ans2 == 1:
  Huf += 2
elif ans2 ==2:
  Sly += 2
elif ans2 ==3:
  Rav += 2
elif ans2 ==4:
  Grf += 2
else:
  print("Wrong input.")

ans3 = int(input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if ans3 == 1:
  Sly += 4 
elif ans3 ==2:
  Huf += 4
elif ans3 ==3:
  Rav += 4
elif ans3 ==4:
  Grf += 2
else:
  print("Wrong input.")

print("Slytherin: ",Sly)
print("Gryffindor: ",Grf)
print("Hufflepuff: ",Huf) 
print("Ravenclaw: " ,Rav, "\n")

if Grf > Sly and Grf > Rav and Grf > Huf:
  print("You belong to Gryffindor!")
elif Sly > Grf and Sly > Rav and Sly > Huf:
  print("You belong to Slytherin!")
elif Rav > Grf and Rav > Sly and Rav > Huf:
  print("You belong to Ravenclaw!")
elif Huf > Rav and Huf > Grf and Huf > Sly:
  print("You belong to Hufflepuff!")
else:
  print("wrong input")