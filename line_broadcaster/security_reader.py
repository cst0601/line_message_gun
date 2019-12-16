"""
security_reader.py
Reads application access token and webhook secret.

Created by Chikuma, 2019/12/16
"""

class SecurityReader:
    def __init__(self, path="secret_mix"):
        self.tokenFile = open(path + "token", "r")
        self.webhookFile = open(path + "webhook", "r")

    def getToken(self):
        if self.tokenFile.mode is "r":
            return self.tokenFile.read()
        return ""

    def getWebhookSecret(self):
        if self.webhookFile.mode is "r":
            return self.webhookFile.read()
        return ""

    # Plz remember to close this after reading
    def close(self):
        self.tokenFile.close()
        self.webhookFile.close()
