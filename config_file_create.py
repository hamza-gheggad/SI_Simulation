from configparser import ConfigParser

config = ConfigParser()

config['victime'] = {
    'os': 'os here',
    'name': 'name here'
}

config['attaquant'] = {
    'os': 'os here',
    'name': 'name here',
    'TypeOfAttack': 'pishing'

}

with open('/Users/p/Desktop/CEI/dev.ini', 'w') as f:
    config.write(f)
