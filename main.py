#there are three different types
#between computer and user
import random
n=random.randint(1,100)
a= -1
guesses= 1
  
while(a!=n):
    a=int(input("Guess the number: " ))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses+=1
print(f"you have guessed the number {n} correctly in {guesses} attempt")

#or (method 2) between two users,1 is decide a number and another one is guessing

# class game: 
#     def __init__(self):
#         self.guesses=0 
#     def play(self):
#         #player 1 choose a number
#         n=int(input("you choose a number=")) 
#         print("\n"*30) #screen clear jaise effect
#         #player 2 choose a number
#         a=-1
#         while(a!=n):
#             a=int(input("player2:Guess the number: " ))
#             self.guesses+=1
#             if(a>n):
#                 print("Lower number please")
#             else:
#                 print("Higher number please")
#         print(f"you have guessed the number {n} correctly in {self.guesses} attempt")



# shrishti=game()
# shrishti.play()

#between two user choose their own value
# class game: 
#     def __init__(self):
#         self.guesses1=0 
#         self.guesses2=0 
#     def play(self):
      
#         n1=int(input("player1:you choose a number=")) 
#         print("\n"*30)
#         n2=int(input("player2:you choose a number=")) 
#         print("\n"*30) #screen clear jaise effect
        
#         a=-1
#         b=-1
#         while(True):
#             a=int(input("\nplayer1: Guess the number of player2: " ))
#             self.guesses1+=1
#             if a==n2:
#                 print(f"you have guessed the number {n2} correctly in {self.guesses1} attempt.\nplayer1: congratulation,you win!😍\nplayer2:better luck next time.😊")
#                 break
#             elif a>n2:
#                 print("Lower number please")
#             else:
#                 print("Higher number please")
            
#             b=int(input("player2: Guess the number of player1: " ))
#             self.guesses2+=1
#             if b==n1:
#                 print(f"you have guessed the number {n1} correctly in {self.guesses2} attempt\nplayer2:congratulation,you win !😍\nplayer1:better luck next time.😊")
#                 break
#             elif b>n1 :
#                 print("Lower number please")
#             else:
#                 print("Higher number please")
        
                
            
# shrishti=game()
# shrishti.play()
