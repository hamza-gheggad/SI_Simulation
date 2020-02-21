from agents import *
from instances import *


machineNULL = Machine("NULL", "NULL", "NULL", "NULL")


while True:
    x = input("Enter a command : ")
    L = x.split()

    if 'man' in L:
        print("Les commandes disponibles sont :\n\nlist_software <name_of_machine> -> lister les logiciels ouverts sur la machine.\n\nlist_subnet_machines -> lister toutes les machines de votre subnet.\n\nexit ou q -> pour quitter. ")
    if 'list_software' in L:
        attaquant.list_software(L[1])
    if 'list_subnet_machines' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            print(node.name)
    if ('exit' in L) or ('q' in L):
        break
        exit()
