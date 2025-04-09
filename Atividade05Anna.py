cont=0
n=0
for a in range(4):
   n = int(input("Digite um número: "))
   if n < 0:
       cont = cont + 1
print(cont, end=" ")