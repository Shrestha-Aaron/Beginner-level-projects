#Simple Quiz game of 5 Questions(Easy)

print("HI This is quiz game! ")
marks=0
print("LETS GET STARTED!")
ans=int(input("How many countries are there? "))
if ans == 195:
    marks+=1

ans=input("which continent is the largest? ")
if ans.lower()=="asia":
    marks+=1
    
ans=input("Who is the father of science? ").lower()
if ans=="galileo galilei" or ans=="galileo":
    marks+=1 

ans=input("Who is the ceo of Nividia? ").lower()
if ans=="jensen huang" or ans=="jensen":
    marks+=1
    
ans=int(input("What is the height of the Mount Everest(in meters)? "))
if ans==8848:
    marks+=1

if marks==0:
    print("You lost but nice try :)")
elif marks==5:
    print("SPLENDID! A PERFECT SCORE OF 5 ( ˶°ㅁ°) !!")
else:
    print(f"Good job, you got {marks}")
