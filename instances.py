from agents import *
from configparser import ConfigParser


parser = ConfigParser()
parser.read('dev.ini')


router1 = Router("router1", "NULL", "NULL")
router2 = Router("router2", "NULL", "NULL")
sous_reseau_local = subnet(parser.get('local_subnet', 'name'), parser.get('local_subnet', 'IP_range'), [], router1, parfeu=parfeu())
sous_reseau_externe = subnet(parser.get('extern_subnet', 'name'), parser.get('extern_subnet', 'IP_range'), [], router2, parfeu=parfeu())

router1.subnetin, router1.subnetout = sous_reseau_local, sous_reseau_externe

ssh_admin = Software(parser.get('ssh-admin', 'name'), parser.get('ssh-admin', 'version'), token1=parser.get('ssh-admin', 'password'))
ssh_sever = Software(parser.get('ssh-server', 'name'), parser.get('ssh-server', 'version'), token1=parser.get('ssh-server', 'password'))
apache = Software(parser.get('apache', 'name'), parser.get('apache', 'version'), accessRight=parser.get('apache', 'accessRight'))
wireshark = Software(parser.get('wireshark', 'name'), parser.get('wireshark', 'version'))
chrome = Software(parser.get('chrome', 'name'), parser.get('chrome', 'version'))

apache2_vuln = vulnerability(parser.get('apache2_vuln', 'name'), parser.get('apache2_vuln', 'software'), parser.get('apache2_vuln', 'trigger'), parser.get('apache2_vuln', 'action'))


MachineVictime = Victim_Machine(parser.get('Victim_Machine', 'name'), parser.get('Victim_Machine', 'os'), parser.get('Victim_Machine', 'IP_address'), [ssh_admin, apache], vulnerabilities=[apache2_vuln])
sous_reseau_local.add_node(MachineVictime)

VictimeExterne = Victim_Machine(parser.get('Victim_Externe', 'name'), parser.get('Victim_Externe', 'os'), parser.get('Victim_Externe', 'IP_address'), [ssh_admin, apache], vulnerabilities=[apache2_vuln], booted=True)
sous_reseau_externe.add_node(VictimeExterne)

MachineAttaquant = Attacking_Machine(parser.get('Attacking_Machine', 'name'), parser.get('Attacking_Machine', 'os'), parser.get('Attacking_Machine', 'IP_address'), [ssh_admin],rights=parser.get('Attacking_Machine', 'rights'))
sous_reseau_local.add_node(MachineAttaquant)


parfeu = parfeu(parser.get('parfeu', 'name'), parser.get('parfeu', 'os'), parser.get('parfeu', 'IP_address'), [wireshark], parser.get('parfeu', 'rules'), booted=True)
sous_reseau_externe.add_node(parfeu)
sous_reseau_externe.parfeu = parfeu

serveur_distant = web_server(parser.get('web_server', 'name'), parser.get('web_server', 'os'), parser.get('web_server', 'IP_address'), [ssh_sever, apache], booted=True)
sous_reseau_externe.add_node(serveur_distant)

parfeu.subnet = sous_reseau_externe
MachineAttaquant.subnet = sous_reseau_local
MachineVictime.subnet = sous_reseau_local
VictimeExterne.subnet = sous_reseau_externe
serveur_distant.subnet = sous_reseau_externe

Paul = Victime(parser.get('Paul', 'name'), MachineVictime)

attaquant = Attaquant(parser.get('Attaquant', 'name'), Attacking_Machine=MachineAttaquant)


subnets = [sous_reseau_local, sous_reseau_externe]
