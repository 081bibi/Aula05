dentro=0
fora=0
for a in range(10):
   num = int(input("Digite um número: "))
   if num >=10 and num <=20:
       dentro = dentro +1
   else:
    fora = fora + 1
print(dentro, end=" ")
print(fora, end=" ")


