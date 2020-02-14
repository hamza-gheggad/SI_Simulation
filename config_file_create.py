from configparser import ConfigParser

config = ConfigParser()

config['Machine'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['Victim_Machine'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software',
    'vulnerabilities': 'vulnerabilities',
    'defense_actions': 'defense_actions'
}

config['Attacking_Machine'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software',
    'attack_actions': 'attack_actions'
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

config['Web_server'] = {
    'name': 'name',
    'os': 'os',
    'IP_address': 'IP_address',
    'installed_software': 'installed_software'
}

config['Mail_server'] = {
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
    'name': 'name',
    'Victim_Machine': 'Victim_Machine'
}

config['Attaquant'] = {
    'name': 'name',
    'Victim_Machine': 'Victim_Machine'
}

config['Subnet'] = {
    'name': 'name',
    'components': 'components'
}

config['Software'] = {
    'name': 'name',
    'version': 'version'
}

config['File_System'] = {
    'Repositories': 'Repositories',
    'Files': 'Files'
}

config['Router'] = {
    'IP_address': 'IP_address'
}

config['NIDS'] = {
    'name': 'namr'
}

with open('/Users/p/Desktop/CEI/dev.ini', 'w') as f:
    config.write(f)
