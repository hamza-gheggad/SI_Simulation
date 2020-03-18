import logging


class Router:
    def __init__(self, name, subnetin="NULL", subnetout="NULL"):
        self.name = name
        self.subnetin = subnetin
        self.subnet = subnetout
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
    def __init__(self, name="NULL", sonde="NULL", IP_range='0.0.0.0/24', components=[], router="NULL", parfeu='NULL'):
        self.name = name
        self.components = components
        self.sonde = sonde
        self.router = router
        self.parfeu = parfeu
        self.IP_range = IP_range

    def add_node(self, new_node):
        self.components.append(new_node)
        logging.debug("Le noeud {} a été ajouté au sous-réseau {}.".format(new_node.name, self.name))

    def remove_node(self, node):
        self.components.remove(node)
        logging.debug("Le noeud {} a été supprimé du sous-réseau {}.".format(node.name, self.name))


class File_System:
    def __init__(self, Repositories=[], Files=[]):
        self.Repositories = Repositories
        self.Files = Files


class vulnerability:
    def __init__(self, name="NULL", software="NULL", trigger="NULL", action="NULL"):
        self.name = name
        self.software = software
        self.trigger = trigger
        self.action = action


class Machine:
    def __init__(self, name, os, IP_address, installed_software=[], rights='user', subnet=subnet(), filesystem=File_System(), booted=False, host_sonde="NULL"):
        self.name = name
        self.booted = booted
        self.os = os
        self.rights = rights
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.subnet = subnet
        self.host_sonde = host_sonde
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

    def to_root(self):
        if self.rights == 'user':
            self.rights = 'root'
            logging.debug("Les droits sur la machine {} sont désormais root.".format(self.name))
        else:
            print("Vous êtes déjà root")

    def to_user(self):
        if self.rights == 'root':
            self.rights = 'user'
            logging.debug("Les droits sur la machine {} sont désormais user.".format(self.name))
        else:
            print("Vous êtes déjà user")


class Victim_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, rights='user', vulnerabilities=[], defense_actions=[], subnet=subnet(), filesystem=File_System([], []), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.vulnerabilities = vulnerabilities
        self.defense_actions = defense_actions
        self.subnet = subnet
        self.filesystem = filesystem
        self.host_sonde = host_sonde
        self.booted = booted


class Attacking_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, rights='user', attack_actions=[], subnet=subnet(), filesystem=File_System(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.attack_actions = attack_actions
        self.subnet = subnet
        self.filesystem = filesystem
        self.host_sonde = host_sonde
        self.booted = booted


class parfeu(Machine):
    def __init__(self, name="NULL", os="NULL", IP_address="NULL", installed_software=[], rights='user', rules="NULL", subnet=subnet(), filesystem=File_System(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.rules = rules
        self.subnet = subnet
        self.filesystem = filesystem
        self.host_sonde = host_sonde
        self.booted = booted

    def add_rule(self, rule):
        logging.debug("La règle <{}> est ajoutée au parfeu de {}.".format(rule, self.name))

    def remove_rule(self):
        logging.debug("La règle <{}> est ajoutée au parfeu de {}.".format(rule, self.name))


class Server(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software=[], rights='user', subnet=subnet(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.host_sonde = host_sonde
        self.booted = booted


class Client(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software=[], rights='user', subnet=subnet(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.host_sonde = host_sonde
        self.booted = booted


class web_server(Server):
    def __init__(self, name, os, IP_address, installed_software=[], rights='user', subnet=subnet(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.host_sonde = host_sonde
        self.booted = booted


class mail_server(Server):
    def __init__(self, name, os, IP_address, installed_software=[], rights='user', subnet=subnet(), booted=False, host_sonde="NULL"):
        self.name = name
        self.os = os
        self.subnet = subnet
        self.IP_address = IP_address
        self.rights = rights
        self.installed_software = installed_software
        self.host_sonde = host_sonde
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


class HIDS(Software):
    def __init__(self, name, version="NULL", accessRight="user", rules="NULL"):
        self.name = name
        self.version = version
        self.rules = rules
        self.accessRight = accessRight

    def alert(self, message="NULL"):
        print('alerte HIDS : {}'.format(message))
        logging.debug("alerte HIDS : {}".format(message))


class NIDS:
    def __init__(self, name="NULL", subnet="NULL", rules="NULL"):
        self.name = name
        self.subnet = subnet
        self.rules = rules

    def alert(self, message="NULL"):
        print('alerte : {}'.format(message))
        logging.debug("alerte NIDS du sous-réseau {} : {}".format(self.subnet.name, message))
