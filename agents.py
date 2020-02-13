class Machine:
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Victim_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, vulnerabilities, defense_actions):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.vulnerabilities
        self.defense_actions = defense_actions


class Attacking_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, attack_actions):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.attack_actions = attack_actions


class Victim_Machine(Machine):
    def __init__(self, name, os, IP_address, installed_software, rules):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software
        self.rules = rules

    def add_rule(self):
        pass

    def set_rule(self):
        pass

    def remove_rule(self):
        pass


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


class Web_server(Server):
    def __init__(self, name, os, IP_address, installed_software):
        self.name = name
        self.os = os
        self.IP_address = IP_address
        self.installed_software = installed_software


class Mail_server(Server):
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
        pass


class Victime(Utilisateur):
    def __init__(self, name, Victim_Machine):
        self.name = name
        self.Victim_Machine = Victim_Machine

    def defend(self):
        pass


class Attaquant(Utilisateur):
    def __init__(self, name, Victim_Machine):
        self.name = name
        self.Victim_Machine = Victim_Machine

    def execAttack(self):
        pass


class Subnet:
    def __init__(self, name, components):
        self.name = name
        self.components = components


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
        self.nom = nom

    def alert(self):
        pass


class HIDS:
    def __init__(self, nom):
        self.nom = nom

    def alert(self):
        pass
