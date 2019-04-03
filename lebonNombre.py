print("Let's play a little game ")
print("Essayer de deviner le bon nombre en 3 essais ... le bon nombre se trouvera entre 1 et 25 ")
import time
import random as r
import sys

nombre_a_deviner = r.randint(1,25)
essai = range(3)

for choix in essai:
	choix = input("Quel est le nombre de votre choix ? ")
	if int(choix) > nombre_a_deviner :
		print("Le nombre {0} est superieur au bon nombre ...".format(choix))
	elif int(choix) < nombre_a_deviner :
		print("Le nombre {0} est inferieur au bon nombre ...".format(choix))
	else:
		print("Bravo, vous avez trouve au bout de {0} essai(s)".format(essai))
		break

# un temps de suspense
time.sleep(1.5)
if choix != nombre_a_deviner :
	print("Desole vous avez perdu, le bon nombre etait {0} !".format(nombre_a_deviner))
	print('Retentez votre chance')

