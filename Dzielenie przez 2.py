print("Insert your number: ")
while True:
   while True:
       try:
        x = input()
        x = float(x)
       except ValueError:
        print("Use numbers next time, game over!")
        break
       if True:
        print("Would you like to divide it by 2?\nyes/no")
        ans = input()
       if ans == "yes":
        y = float(x) / 2
        print("All right! Here is your result: ", y)
        break

       elif ans == "no":
         print("Ok...")
         break
       else:
        print("Wrong answer. Insert another number: ")
   print("\nDo you want to try again?\nYou can write another number: ")