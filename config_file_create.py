from configparser import ConfigParser

config = ConfigParser()

config['Machine'] = {
    'name': 'Ordi personnel',
    'os': 'Debian2.0',
    'IP_address': '192.168.56.1',
    'installed_software': ''
}

config['Victim_Machine'] = {
    'name': 'Ordi-Paul',
    'os': 'Windows 10',
    'IP_address': '192.168.56.2',
    'installed_software': '',
    'vulnerabilities': 'ssh_weak_password Chrome_exploit',
    'defense_actions': ''
}

config['parfeu'] = {
    'name': 'Parfeu-Paul',
    'os': 'Debian2.1',
    'IP_address': '192.168.56.102',
    'installed_software': '',
    'rules': 'ACCEPT INPUT HTTP,ACCEPT OUTPUT HTTP,ACCEPT INPUT SSH,ACCEPT OUTPUT SSH'
}

config['Attacking_Machine'] = {
    'name': 'Ordi-Anonyme',
    'os': 'Kali2020.1',
    'IP_address': '192.168.56.100',
    'installed_software': '',
    'attack_actions': 'attack1 attack2'
}

config['Server'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['Client'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['web_server'] = {
    'name': 'serveur web ALPHA',
    'os': 'Fedora31.0',
    'IP_address': '204.17.5.100',
    'installed_software': 'apache2 SSH5.1'
}

config['apache2_vuln']={
    'name': 'apache2_vuln',
    'action':'buffer_overflow',
    'trigger':'version_2.2'
}

config['mail_server'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['Utilisateur'] = {
    'name': 'name',
    'Machine': 'Machine'
}

config['Victime'] = {
    'name': 'Paul',
    'Victim_Machine': 'Victim_Machine'
}

config['Attaquant'] = {
    'name': 'Anonymous',
    'Attacking_Machine': 'Attacking_Machine'

}

config['subnet'] = {
    'name': 'réseau local',
    'components': 'components'
}

config['ssh-new'] = {
    'name': 'SSH5.1',
    'version': '5.1'
}

config['ssh-old'] = {
    'name': 'SSH2.4',
    'version': '2.4'
}

config['apache'] = {
    'name': 'Apache2',
    'version': '2.2'
}

config['metasploit'] = {
    'name': 'Metasploit',
    'version': '4.17'
}

config['wireshark'] = {
    'name': 'Wireshark',
    'version': '3.0.1'
}

config['chrome'] = {
    'name': 'Chrome',
    'version': '81.0'
}

config['File_System'] = {
    'Repositories': 'Repositories',
    'Files': 'Files'
}

config['Router'] = {
    'IP_address': 'IP_address'
}

config['NIDS'] = {
    'name': 'name'
}

with open('/Users/p/Desktop/CEI/dev.ini', 'w') as f:
    config.write(f)
