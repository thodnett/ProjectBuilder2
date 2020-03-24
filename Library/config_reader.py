import configparser

def read_configData(section, key):
    config = configparser.ConfigParser
    config.read('\\TestCases\\Config_files\\config.cfg', utf-8)
    return config.get(section, key)

print(read_configData('Details', 'Application_URL '))