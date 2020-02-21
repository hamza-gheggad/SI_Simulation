class subnet:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def add_node(self, new_node):
        self.components.append(new_node)


class Machine:
    def __init__(self, name, os, IP_address, installed_software, subnet=subnet("NULL", [])):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.subnet = subnet

    def turn_on(self):
        print("{} est en marche.".format(self.name))

    def turn_off(self):
        print("{} est arretée.".format(self.name))


class Victim_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, vulnerabilities, defense_actions=[], subnet=subnet("NULL", [])):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.vulnerabilities = vulnerabilities
        self.defense_actions = defense_actions
        self.subnet = subnet


class Attacking_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, attack_actions, subnet=subnet("NULL", [])):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.attack_actions = attack_actions
        self.subnet = subnet


class parfeu(Machine):
    def __init__(self, name, os, IP_address, installed_software, rules, subnet=subnet("NULL", [])):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.rules = rules
        self.subnet = subnet

    def add_rule(self, rule):
        return "La règle {} est ajoutée au parfeu {}.".format(rule, self.name)

    def remove_rule(self):
        return "La règle {} est supprimée du parfeu {}.".format(rule, self.name)


class Server(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software


class Client(Victim_Machine):
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software


class web_server(Server):
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software


class mail_server(Server):
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software


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
        return "L'attaque {} est exécutée sur {}.".format(attaque, Destination_Machine)

    def list_software(self, Destination_Machine):
        for node in self.Attacking_Machine.subnet.components:
            if node.name == Destination_Machine:
                for software in node.installed_software:
                    print(software.name)


class Software:
    def __init__(self, name, version):
        self.name = name
        self.version = version


class File_System:
    def __init__(self, Repositories, Files):
        self.Repositories = Repositories
        self.Files = Files


class Router:
    def __init__(self, IP_address):
        self.IP_address = IP_address


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
