import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def gitLogin_auth():
    gitUser = 'vyhoang'
    gitToken = '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'
    return gitUser, gitToken
