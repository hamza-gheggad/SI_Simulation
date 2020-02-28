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

            print("\nLes commandes disponibles sont :\n\nlist_subnet_machines -> lister toutes les machines de votre subnet.\n\nlist_software <ip_machine> -> lister les logiciels ouverts sur machine.\n\nget_version <software> <ip_machine> -> récupérer la version du logiciel.\n\nip <machine> -> ip de machine. -> pour quitter.\n\nos <ip_machine> -> os de machine. -> pour quitter.\n\nexec <attack_name> <software_vulnerable> <ip_destination> -> execute attack.\n\nhelp ou h -> afficher ce menu\n\nexit ou q -> pour quitter.\n\nboot <machine> -> démarrer machine.\n\nshutdown <machine> -> arrêter machine.\n\nreboot <machine> -> redémarrer machine.\n\nroot <software> <ip_machine> -> changer les droits à root.\n\nuser <software> <ip_machine> -> changer les droits à user.\n\nrouter -i -> point de départ du routeur.\n\nrouter -o -> point d'arrivée du routeur.\n\nlist_machines <subnet_name> -> lister les machines d'un réseau.\n")

        if 'router' in L:
            if "i" in L[1]:
                print(attaquant.Attacking_Machine.subnet.router.subnetin.name)
            if "o" in L[1]:
                print(attaquant.Attacking_Machine.subnet.router.subnetout.name)

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

                                        if 'i' in Rule[1] and 'SSH' in Rule[2] and 'REJECT' in Rule[3]:
                                            print("Connexion ssh non permise à {}".format(machine.IP_address))
                                else:
                                    print("mot de passe érroné.")

        if 'list_machines' in L:
            for subnet in subnets:
                if subnet.name == L[1]:
                    for machine in subnet.components:
                        print("{}:{}".format(machine.name, machine.IP_address))

        if 'list_software' in L:
            H = []
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[1]:
                    for software in node.installed_software:
                        # time.sleep(1)
                        yield env.timeout(speed)
                        print(software.name)
                        H.append(software.name)

            logging.debug("La liste des softwares pour la machine {} trouvée est : {}".format(L[1], H))

        if 'root' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            # time.sleep(1)
                            yield env.timeout(speed)
                            software.root_only()

        if 'user' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            # time.sleep(1)
                            yield env.timeout(speed)
                            software.any_user()

        if 'list_subnet_machines' in L:
            H = []
            for node in attaquant.Attacking_Machine.subnet.components:
                # time.sleep(1)
                yield env.timeout(speed)
                print(node.name)
                H.append(node.name)

            logging.debug("Les machines du même sous-réseau sont {}".format(H))

        if 'get_version' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[2]:
                    for software in node.installed_software:
                        if software.name == L[1]:
                            # time.sleep(1)
                            yield env.timeout(speed)
                            print(software.version)
                            logging.debug("La version de {} du {} est : {}".format(software.name, node.name, software.version))

        if 'ip' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.name == L[1]:
                    # time.sleep(1)
                    yield env.timeout(speed)
                    print(node.IP_address)
                    logging.debug("ip de {} est : {}".format(node.name, node.IP_address))

        if 'os' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[1]:
                    time.sleep(1)
                    print(node.os)
                    logging.debug("os de {} est : {}".format(node.name, node.os))

        if 'exec' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.IP_address == L[3] and L[1] == "memory-attack" and L[2] == "Apache2":
                    for software in node.installed_software:
                        if software.name == L[2] and software.version == "2.2":
                            time.sleep(3)
                            attaquant.execAttack(L[1], L[3])

        if 'boot' in L:
            for node in attaquant.Attacking_Machine.subnet.components:
                if node.name == L[1]:
                    node.boot()
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
