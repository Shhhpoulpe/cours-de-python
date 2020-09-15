# # Exo 1

# a = 5
# b = 10

# c=a
# a=b
# b=c

# print("a = " , a , ", b =" , b)

# # Exo 2

# entree = int(input("Veuillez entrer une valeur"))
# print(entree*entree)

# # Exo 3

# entree = int(input("Veuillez entrer une valeur"))

# if entree > 0:
#     print("Positif")
# else:
#     print("négatif")

# # Exo 4

# entree = int(input("Veuillez entrer une valeur"))
# entree2 = int(input("Veuillez entrer une autre valeur"))

# if entree + entree2 > 0:
#     print("Positif")
# else:
#     print("négatif")

# # Exo 5

# entree = int(input("Veuillez entrer une valeur"))

# for i in range(10):
#     print(entree + i + 1)

# # Exo 6

# entree = int(input("Veuillez entrer une valeur"))
# res = 0
# for i in range(entree):
#     res += i + 1
# print(res)

# Exo 2.1

tab = [1,2,3,4,5]
res = 0
for i in tab:
    res += i
print(res)

# Exo 2.2

tab = [1,2,3,4,5]
tab2 = [11,12,13,14,15]
res = [None]*5

for i in range(len(tab)):
    res[i] = tab[i] + tab2[i]
print(res)

# Exo 2.3

tab = [1,2,3,4,5]
tab2 = [1,2,3,4,5]
res2 = 0

for i in range(len(tab)):
    res2 += tab[i] * tab2[i]
print(res2)

# Exp 2.4

tab = [5,4,9,8,1,0,2]
res3 = 0
res4 = 0

for i in range(len(tab)):
    if tab[i] > res3:
        res3 = tab[i]
        res4 = i
print(res3 , "qui est a la case n°" , res4)