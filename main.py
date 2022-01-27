import pickle
import time

import account
import admin
from admin import Admin
import os


def main():
    use = Admin(allUser="")
    use.View()

main()


class ATM:
    def __init__(self, allUser):
        self.allUser = allUser

    def View(self):
        pass

    def FunctionView(self):
        pass

    def Kontrollera(self):
        pass

    def Registrera(self):
        pass

    def creatUser(self):
        pass

    def UserInfo(self):
        pass

    def withdrawmoney(self):
        pass

    def putmoneyin(self):
        pass

    def transferMoney(self):
        pass

    def changePassword(self):
        pass

    def låsAnvändare(self):
        pass

    def unLockUser(self):
        pass

    def newCard(self):
        pass

    def avbryta(self):
        pass

    def checkPassword(self, realPasswd):
        pass

    def randomnum(self):
        pass

    def randomCardId(self):
        pass

    def verify(self):
        pass
