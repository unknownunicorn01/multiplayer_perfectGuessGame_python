import random
import os

def fun(player):
  computerNumber=random.randint(1,100)
  # print(computerNumber)
  yourGuess=-1
  moves=0
  while (yourGuess!=computerNumber):
    yourGuess=int(input("Enter you guess number: "))
    if(yourGuess>computerNumber):
      print("Lower number please!!")
    elif (yourGuess<computerNumber):
      print("Higher number please")
    moves+=1
  print(f"\n{player} got correct guess in {moves} chances\n")
  return moves

numberOfPlayers=int(input("enter the number of players: "))
names=[]
for i in range(numberOfPlayers):
  name=input(f"enter the name of player{i+1}")
  names.append(name)
l2=[]
for i in range(len(names)):
  print(f"{names[i]} chance to play")
  l2.append(fun(names[i]))

chances=list(zip(l2,names))
chances.sort()

position, positionName=zip(*chances)
# print(position,positionName)
result=""
for i in range(len(positionName)):
  r=f"{i+1} position : {positionName[i]} with chances, {position[i]}\n"
  result+=r
print(result)

save=input("Do you want to save this in saperate file? : (Yes/No) ").lower()

if save!="yes" and save!="no":
  k=1
  while save!="yes" and save!="no":
    print("Please answer in Yes or No only!")
    save=input("Do you want to save this file? : (Yes/No) ").lower()
    k+=1
if save=="yes":
  fname=input("What would you like to name you file? : ")
  fileName=f"{fname}.txt"
  if fname=="Result":
    print("You can't name file Result because it is a default file to save all data.\nTry another name")
  else:
    if os.path.exists(f"result/{fileName}"):
      save2=input("File name already exist, do you want to replace this file? : (Yes/No)").lower()
      if(save2=="no"):
        choice=input("Do you want to append in file? : (Yes/No): ").lower()
        if(choice=="yes"):
          with open(f"result/{fileName}","a") as f:
            f.write(f"\n{result}\n")
          with open(f"result/Result.txt","a") as f:
            f.write(f"\n{result}\n")
        elif(choice=="no"):
          new_name=input("What would you like to name you file? : ")
          with open(f"result/{new_name}.txt","a") as f2:
            f2.write(f"\n{result}\n")
          with open(f"result/Result.txt","a") as f:
            f.write(f"\n{result}\n")
    else:
      with open(f"result/{fileName}","a") as f:
        f.write(f"\n{result}\n")
elif(save=="no"):
  with open(f"result/Result.txt","a") as f:
    f.write(f"\n{result}\n")