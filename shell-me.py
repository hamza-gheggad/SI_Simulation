import logging
logging.basicConfig(filename="shell-history.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

from agents import *
from instances import *


machineNULL = Machine("NULL", "NULL", "NULL", "NULL")


while True:
    x = input("{}> ".format(attaquant.name))
    L = x.split()

    if ('help' in L) or ('h' in L):
        print("\nLes commandes disponibles sont :\n\nlist_subnet_machines -> lister toutes les machines de votre subnet.\n\nlist_software <ip_machine> -> lister les logiciels ouverts sur machine.\n\nget_version <software> <ip_machine> -> récupérer la version du logiciel.\n\nip <machine> -> ip de machine. -> pour quitter.\n\nos <ip_machine> -> os de machine. -> pour quitter.\n\nexec <attack_name> <software_vulnerable> <ip_destination> -> execute attack.\n\nhelp ou h -> afficher ce menu\n\nexit ou q -> pour quitter.\n\nboot <machine> -> démarrer machine.\n\nshutdown <machine> -> arrêter machine.\n")

    if 'list_software' in L:
        H = []
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.IP_address == L[1]:
                for software in node.installed_software:
                    print(software.name)
                    H.append(software.name)

        logging.debug("La liste des softwares pour la machine {} trouvée est : {}".format(L[1], H))

    if 'list_subnet_machines' in L:
        H = []
        for node in attaquant.Attacking_Machine.subnet.components:
            print(node.name)
            H.append(node.name)

        logging.debug("Les machines du même sous-réseau sont {}".format(H))

    if 'get_version' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.IP_address == L[2]:
                for software in node.installed_software:
                    if software.name == L[1]:
                        print(software.version)
                        logging.debug("La version de {} du {} est : {}".format(software.name, node.name, software.version))

    if 'ip' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.name == L[1]:
                print(node.IP_address)
                logging.debug("ip de {} est : {}".format(node.name, node.IP_address))

    if 'os' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.IP_address == L[1]:
                print(node.os)
                logging.debug("os de {} est : {}".format(node.name, node.os))

    if 'exec' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.IP_address == L[3] and L[1] == "memory-attack" and L[2] == "Apache2":
                for software in node.installed_software:
                    if software.name == L[2] and software.version=="2.2":
                        attaquant.execAttack(L[1], L[3])

    if 'boot' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.name == L[1]:
                node.boot()
    if 'shutdown' in L:
        for node in attaquant.Attacking_Machine.subnet.components:
            if node.name == L[1]:
                node.shutdown()
    if ('exit' in L) or ('q' in L):
        break
        exit()
