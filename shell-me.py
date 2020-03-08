import simpy
import time
import logging
logging.basicConfig(filename="shell-history.log", level=logging.DEBUG, format='%(asctime)s:%(message)s')

from agents import *
from instances import *


def main():
    env = simpy.Environment()
    env.process(scenario(env, attaquant=attaquant, speed=2))
    env.run(until=100)


def scenario(env, attaquant, speed):

    while True:
        x = input("{}> ".format(attaquant.name))
        L = x.split()

        if ('help' in L) or ('h' in L):

            print("\nLes commandes disponibles sont :\n\nlist_subnet_machines -> lister toutes les machines de votre subnet.\n\nlist_software <ip_machine> -> lister les logiciels ouverts sur machine.\n\nget_version <software> <ip_machine> -> récupérer la version du logiciel.\n\nwhoami <ip> -> afficher les droits\n\nip <machine> -> ip de machine. -> pour quitter.\n\nos <ip_machine> -> os de machine. -> pour quitter.\n\nhelp ou h -> afficher ce menu\n\nexit ou q -> pour quitter.\n\nboot <machine> -> démarrer machine.\n\nshutdown <machine> -> arrêter machine.\n\nreboot <machine> -> redémarrer machine.\n\nroot <software> <ip_machine> -> changer les droits à root.\n\nuser <software> <ip_machine> -> changer les droits à user.\n\nrouter -i -> point de départ du routeur.\n\nrouter -o -> point d'arrivée du routeur.\n\nlist_machines <subnet_name> -> lister les machines d'un réseau.\n\nssh username@ip_address\n\nexploit <software_name> <ip>")

        if 'router' in L:
            if "i" in L[1]:
                print("{};{}".format(attaquant.Attacking_Machine.subnet.router.subnetin.name, attaquant.Attacking_Machine.IP_address))
            if "o" in L[1]:
                print("{};{}".format(attaquant.Attacking_Machine.subnet.router.subnetout.name, VictimeExterne.IP_address))

        if 'ssh' in L and '@' in L[1]:
            for subnet in subnets:
                for machine in subnet.components:
                    for software in machine.installed_software:
                        if 'SSH' in software.name:
                            if machine.IP_address in L[1] and machine.name in L[1] and machine.booted == True:
                                password = input("password:")
                                if software.token1 == password:
                                    rules = subnet.parfeu.rules.split(',')
                                    print("Essai de connexion ssh à {}...".format(machine.IP_address))
                                    time.sleep(3)
                                    yield env.timeout(speed)
                                    for rule in rules:
                                        Rule = rule.split()
                                        if ('i' in Rule[1] and 'SSH' in Rule[2] and 'ACCEPT' in Rule[3]) or ('ANY' in Rule[1] and 'SSH' in Rule[2] and 'ACCEPT' in Rule[3]):
                                            print("Connexion ssh réussie à {}".format(machine.IP_address))
                                            while True:
                                                shell_ssh = input("{}$".format(machine.name))
                                                H = shell_ssh.split()
                                                if ('exit' in H) or ('q' in H):
                                                    break
                                                if 'boot' in H:
                                                    machine.boot()
                                                if 'reboot' in H:
                                                    machine.reboot()
                                                if 'shutdown' in H:
                                                    machine.shutdown()
                                                    break

                                                if 'list_machines' in H:
                                                    for node in machine.subnet.components:
                                                        time.sleep(1)
                                                        yield env.timeout(speed)
                                                        print("{}:{}".format(node.name, node.IP_address))
                                                if 'ssh' in H[0] and '@' in H[1]:
                                                    for submachine in machine.subnet.components:
                                                        if submachine.IP_address in H[1] and submachine.name in H[1] and submachine.booted == True:
                                                            for subsoftware in submachine.installed_software:
                                                                if 'SSH' in subsoftware.name:
                                                                    password = input("password:")
                                                                    if subsoftware.token1 == password:
                                                                        print("Connexion ssh réussie à {}".format(submachine.IP_address))
                                                                        while True:
                                                                            subshell_ssh = input("{}$".format(submachine.name))
                                                                            S = subshell_ssh.split()
                                                                            if ('exit' in S) or ('q' in S):
                                                                                break
                                                                            if 'shutdown' in S:
                                                                                submachine.shutdown()
                                                                                break
                                                                            if 'reboot' in S:
                                                                                submachine.reboot()
                                                                    else:
                                                                        print("mot de passe érroné.")

                                        if 'i' in Rule[1] and 'SSH' in Rule[2] and 'REJECT' in Rule[3]:
                                            print("Connexion ssh non permise à {}".format(machine.IP_address))
                                else:
                                    print("mot de passe érroné.")

        if 'list_software' in L:
            H = []
            for subnet in subnets:
                for node in subnet.components:
                    if node.IP_address == L[1]:
                        for software in node.installed_software:
                            time.sleep(1)
                            yield env.timeout(speed)
                            print(software.name)
                            H.append(software.name)

            logging.debug("La liste des softwares pour la machine {} trouvée est : {}".format(L[1], H))
        if 'exploit' in L:
            for subnet in subnets:
                for node in subnet.components:
                    if node.IP_address == L[2]:
                        for software in node.installed_software:
                            time.sleep(1)
                            yield env.timeout(speed)
                            if software.name == L[1]:
                                for vuln in node.vulnerabilities:
                                    if vuln.software == software.name:
                                        print("action : {}".format(vuln.action))
                                        node.rights = software.accessRight
                                        logging.debug("Les droits sur la machine {} sont : {}".format(node.name, node.rights))
        if 'root' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            time.sleep(1)
                            yield env.timeout(speed)
                            software.root_only()

        if 'user' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            time.sleep(1)
                            yield env.timeout(speed)
                            software.any_user()

        if 'list_subnet_machines' in L:
            H = []
            for node in attaquant.Attacking_Machine.subnet.components:
                time.sleep(1)
                yield env.timeout(speed)
                print(node.name)
                H.append(node.name)

            logging.debug("Les machines de votre sous-réseau sont {}".format(H))

        if 'list_machines' in L:
            H = []
            for subnet in subnets:
                if subnet.IP_range == L[1]:
                    for node in subnet.components:
                        yield env.timeout(speed)
                        print(node.name)
                        H.append(node.name)
            logging.debug("Les machines du sous-réseau {} sont {}".format(subnet.IP_range, H))

        if 'get_version' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            time.sleep(1)
                            yield env.timeout(speed)
                            print(software.version)
                            logging.debug("La version de {} du {} est : {}".format(software.name, node.name, software.version))

        if 'ip' in L:
            if len(L) == 1:
                print(attaquant.Attacking_Machine.IP_address)
            else:
                for node in attaquant.Attacking_Machine.subnet.components:
                    if node.name == L[1]:
                        time.sleep(1)
                        yield env.timeout(speed)
                        print(node.IP_address)
                        logging.debug("ip de {} est : {}".format(node.name, node.IP_address))

        if 'os' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[1]:
                    time.sleep(1)
                    print(node.os)
                    logging.debug("os de {} est : {}".format(node.name, node.os))

        if 'boot' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.name == L[1]:
                    node.boot()

        if 'whoami' in L:
            if len(L) == 1:
                print(attaquant.Attacking_Machine.rights)
            else:
                for subnet in subnets:
                    for node in subnet.components:
                        if node.IP_address == L[1]:
                            print(node.rights)

        if 'shutdown' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.name == L[1]:
                    node.shutdown()
        if 'reboot' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.name == L[1]:
                    node.reboot()
        if ('exit' in L) or ('q' in L):
            break
            exit()


if __name__ == "__main__":
    main()
