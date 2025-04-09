num = int(input("Digite um número: "))
if num>=1:
    for x in range(1,num+1,1):
        print(x, end=" ")
else:
    print("Número inválido")