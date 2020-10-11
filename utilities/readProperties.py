import configparser

config = configparser.RawConfigParser()

config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getBrowser():
        browser = config.get('common info','browser')
        return browser

