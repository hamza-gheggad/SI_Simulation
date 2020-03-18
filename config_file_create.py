from configparser import ConfigParser

config = ConfigParser()

config['Machine'] = {
    'name': 'Ordi personnel',
    'os': 'Debian2.0',
    'IP_address': '192.168.56.1',
    'installed_software': '',
    'rights': 'user'
}

config['Victim_Machine'] = {
    'name': 'Ordi-Paul',
    'os': 'Windows 10',
    'IP_address': '192.168.56.2',
    'installed_software': '',
    'rights': 'user',
    'vulnerabilities': '',
    'defense_actions': ''
}

config['Victim_Externe'] = {
    'name': 'admin',
    'os': 'Windows XP',
    'IP_address': '62.212.118.53',
    'installed_software': '',
    'rights': 'user',
    'vulnerabilities': '',
    'defense_actions': ''
}

config['parfeu'] = {
    'name': 'Parfeu-Externe',
    'os': 'Debian2.1',
    'IP_address': '62.212.118.100',
    'installed_software': '',
    'rights': 'user',
    'rules': 'FORWARD -i HTTP ACCEPT,FORWARD -o HTTP ACCEPT,FORWARD -i SSH REJECT,FORWARD -o SSH ACCEPT'
}

config['Attacking_Machine'] = {
    'name': 'Ordi-Anonyme',
    'os': 'Kali2020.1',
    'IP_address': '192.168.56.100',
    'rights': 'user',
    'installed_software': '',
    'attack_actions': ''
}

config['Server'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software',
    'rights': 'user'
}

config['Client'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['web_server'] = {
    'name': 'user',
    'os': 'Fedora31.0',
    'IP_address': '62.212.118.30',
    'installed_software': '',
    'rights': 'user'
}

config['apache2_vuln'] = {
    'name': 'apache2_vuln',
    'software': 'Apache2',
    'trigger': 'memory-attack',
    'action': 'root'
}

config['mail_server'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software',
    'rights': 'user'
}

config['Utilisateur'] = {
    'name': 'name',
    'Machine': ''
}

config['Paul'] = {
    'name': 'Paul',
    'Victim_Machine': ''
}

config['Attaquant'] = {
    'name': 'Anonymous',
    'Attacking_Machine': 'Attacking_Machine'

}

config['local_subnet'] = {
    'name': 'reseau-local',
    'IP_range': '192.168.56.0/24',
    'components': '',
    'router': '',
    'parfeu': ''
}

config['extern_subnet'] = {
    'name': 'reseau-externe',
    'IP_range': '62.212.118.0/24',
    'components': '',
    'router': '',
    'parfeu': ''
}

config['ssh-admin'] = {
    'name': 'SSH5.1',
    'version': '5.1',
    'password': 'admin'
}

config['HIDS1'] = {
    'name': 'HIDS1',
    'version': '10.2',
    'rules': 'DETECT SERVICE SCAN'
}

config['ssh-server'] = {
    'name': 'SSH2.4',
    'version': '2.4',
    'password': 'user'
}

config['apache'] = {
    'name': 'Apache2',
    'version': '2.2',
    'accessRight': 'root'
}


config['wireshark'] = {
    'name': 'Wireshark',
    'version': '3.0.1'
}


config['File_System'] = {
    'Repositories': 'Repositories',
    'Files': 'Files'
}

config['router1'] = {
    'name': 'router1'
}

config['router2'] = {
    'name': 'router2'
}

config['sonde_externe'] = {
    'name': 'sonde_externe',
    'rules': 'DETECT FAST SCAN'
}

with open('/Users/p/Desktop/CEI/dev.ini', 'w') as f:
    config.write(f)
