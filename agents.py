import logging


class Router:
    def __init__(self, name, subnetin, subnetout):
        self.name = name
        self.subnetin = subnetin
        self.subnetout = subnetout
        self.gateway = True

    def endrouting(self):
        if self.gateway == True:
            self.gateway = False
            logging.debug("Le routeur {} -> {} est arrêté.".format(self.subnetin.name, self.subnetout.name))
        else:
            print("Ce routeur est déjà arrêté.")

    def restartrouting(self):
        if self.gateway == False:
            self.gateway = True
            logging.debug("Le routeur {} -> {}est démarré.".format(self.subnetin, self.subnetout))
        else:
            print("Ce routeur est déjà démarré.")


class subnet:
    def __init__(self, name, components, router, parfeu='NULL'):
        self.name = name
        self.components = components
        self.router = router
        self.parfeu = parfeu

    def add_node(self, new_node):
        self.components.append(new_node)
        logging.debug("Le noeud {} a été ajouté au sous-réseau {}.".format(new_node.name, self.name))

    def remove_node(self, node):
        self.components.remove(node)
        logging.debug("Le noeud {} a été supprimé du sous-réseau {}.".format(node.name, self.name))


class File_System:
    def __init__(self, Repositories, Files):
        self.Repositories = Repositories
        self.Files = Files


class vulnerability:
    def __init__(self, name, trigger, action):
        self.name = name
        self.trigger = trigger
        self.action = action


class Machine:
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [], "NULL"), filesystem=File_System([], []), booted=False):
        self.name = name
        self.booted = booted
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.subnet = subnet
        self.filesystem = filesystem

    def boot(self):
        if self.booted == False:
            self.booted = True
            logging.debug("La machine {} a été démarrée.".format(self.name))
        else:
            print("La machine est déjà démarrée.")

    def shutdown(self):
        if self.booted == True:
            self.booted = False
            logging.debug("La machine {} a été arretée.".format(self.name))
        else:
            print("La machine est déjà arretée.")

    def reboot(self):
        if self.booted == True:
            logging.debug("La machine {} a été redémarrée.".format(self.name))
        else:
            print("La machine est déjà arretée.")


class Victim_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, vulnerabilities, defense_actions=[], subnet=subnet("NULL", [], "NULL"), filesystem=File_System([], []), booted=False):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.vulnerabilities = vulnerabilities
        self.defense_actions = defense_actions
        self.subnet = subnet
        self.filesystem = filesystem
        self.booted = booted


class Attacking_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, attack_actions, subnet=subnet("NULL", [], "NULL"), filesystem=File_System([], []), booted=False):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.attack_actions = attack_actions
        self.subnet = subnet
        self.filesystem = filesystem
        self.booted = booted


class parfeu(Machine):
    def __init__(self, name, os, IP_address, installed_software, rules, subnet=subnet("NULL", [], "NULL"), filesystem=File_System([], []), booted=False):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.rules = rules
        self.subnet = subnet
        self.filesystem = filesystem
        self.booted = booted

    def add_rule(self, rule):
        logging.debug("La règle <{}> est ajoutée au parfeu de {}.".format(rule, self.name))

    def remove_rule(self):
        logging.debug("La règle <{}> est ajoutée au parfeu de {}.".format(rule, self.name))


class Server(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [], "NULL"), booted=False):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.booted = booted


class Client(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [], "NULL"), booted=False):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.booted = booted


class web_server(Server):
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [], "NULL"), booted=False):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.booted = booted


class mail_server(Server):
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [], "NULL,"), booted=False):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.booted = booted


class Utilisateur:
    def __init__(self, name, Machine):
        self.name = name
        self.Machine = Machine

    def connect_to(self, Machine):
        print("L'utilisateur {} est connecté à {}.".format(self.name, Machine.name))


class Victime(Utilisateur):
    def __init__(self, name, Victim_Machine):
        self.name = name
        self.Victim_Machine = Victim_Machine

    def defend(self):
        pass


class Attaquant(Utilisateur):
    def __init__(self, name, Attacking_Machine):
        self.name = name
        self.Attacking_Machine = Attacking_Machine

    def execAttack(self, attaque, Destination_Machine):
        logging.debug("L'attaque {} est exécutée sur {}.".format(attaque, Destination_Machine))


class Software:
    def __init__(self, name, version, accessRight="user", token1=""):
        self.name = name
        self.version = version
        self.accessRight = accessRight
        self.token1 = token1

    def root_only(self):
        if self.accessRight == "user":
            self.accessRight = "root"
            logging.debug("Les droits d'accès pour {} sont désormais root.".format(self.name))
        else:
            print("Les droits d'accès sont déjà root only.")

    def any_user(self):
        if self.accessRight == "root":
            self.accessRight = "user"
            logging.debug("Les droits d'accès pour {} sont désormais user.".format(self.name))
        else:
            print("Les droits d'accès sont déjà user (any).")


class NIDS:
    def __init__(self, nom):
        self.name = name

    def alert(self):
        pass


class HIDS:
    def __init__(self, nom):
        self.name = name

    def alert(self):
        pass
