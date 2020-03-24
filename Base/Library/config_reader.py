import configparser

def read_configData(section, key):
    config = configparser.ConfigParser
    config.read.instead_of(r'\TestCases\Config_files\config.cfg')
    return config.get(section, key)

print(read_configData('Details', 'Application_URL '))