import configparser # used to read info from config file

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'usermail')
        return username

    @staticmethod
    def getPasword():
        password = config.get('common info', 'password')
        return password
