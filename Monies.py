def MakeChange(money):

   qur = int(money/25)
   money-=(qur*25)
   print ("Qurters: ", qur)

   dim = int(money/10)
   money-=(dim*10)
   print("Dimes: ", dim)

   Nic = int(money/5)
   money-=(Nic*5)
   print("Nickles: ", Nic)

   pen = money
   print("Pennys: ", pen)

print("How much change you need??")
MakeChange(int(input()))
