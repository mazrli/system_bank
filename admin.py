from card import Card
from account import Account
import random
import time


class Admin:
    usernew = Account(username="", FristName="", LastName="", personnummer="", card="", )
    usercard = Card(CardId="", CardPassword="", CardMoney="")
    res_id = 1001

    def View(self):
        print("Välkommen till Bank System\n ")
        print("--------------------------------------------\n")
        print("Var snäll och välja ")
        print("1. logga in\n")
        print("2. Registrera dig\n")
        print("3. Avsluta \n")
        print("Skriva in ditt val \n")

        input_val = int(input())

        if input_val == 1:
            return True, self.Kontrollera()
        if input_val == 2:
            return True, self.Registrera()
        else:
            return False

    def FunctionView(self):
        print("Hej och välkommen till oss\n")
        print("--------------------------------------------\n")
        print("Vad roligt att du blir vara en av oss\n ")
        print("Nu kan du välje: \n")
        print("1. söker efter user info:\n")
        print("2. ta ut pengar: \n")
        print("3. lägg till pengar till ditt konto:\n")
        print("4.Överföra pengar: \n")
        print("5. Ändra Password:\n")
        print("6. Lås användare:\n")
        print("7. lås upp användare:\n")
        print("8. Avbryta konto:\n")
        print("0. laggat ut:\n")

        while True:
            val = input("välja ditt val: \n")
            if val == "1":
                print(self.UserInfo())
            elif val == "2":
                self.withdrawmoney()
            elif val == "3":
                self.putmoneyin()
            elif val == "4":
                self.transferMoney()
            elif val == "5":
                self.changePassword()
            elif val == "6":
                self.låsAnvändare()
            elif val == "7":
                self.unLockUser()
            elif val == "8":
                self.avbryta()
            elif val == "0":
                if self.verify(self):
                    print("Du har laggat ut")
                    return False
            else:
                print("Du har laggat ut")
                return False


    def Kontrollera(self):
        while True:
            input_username = input("Skriv in ditt Admin user name\n")
            if self.__class__.usernew.username != input_username:
                print("No such user")
                return False
            input_password = input("var snäll och skriva in ditt Password\n")
            if self.__class__.usercard.CardPassword != input_password:
                print("Incorrect password")
                return False


            print("Du lyckas att komma fram vanligt vänta\n")
            time.sleep(1)
            return True, print(self.FunctionView())


    def Registrera(self):
        print("Hej och välkommen till oss\n")
        print("Vad roligt att du vill vara en av oss\n ")
        print("Innan du kan reigsterar dig här vill vi att frågra några frågor\n")
        print("Hur gammal är du? ?\n")
        print("Skriv din ålder\n")
        older_input = int(input())
        if older_input >= 18:
            print("Du är välkommen att skffa ett konto hos oss. \n")
            print("för att kunna skffa ett nytt konto\n")
            print("vänta en studn\n")
            time.sleep(1)
            return True, print(self.creatUser())

        if older_input <= 17:
            print("Du kan tyvärr inte reigsterar dig hos oss, \n")
            print("Du är minder än 18 och det är därför kan du inte skffa ett konto hos oss. \n")
            time.sleep(1)
            print("Du kommer att gå till baka efter 3 sekunder")
            time.sleep(3)

            return False, self.View()

    def printSysFunctionView1(self):
        interface = int(input("Du kan välja en\n 1. logga in \n 2. skaffa ett konto \n"))
        print(interface)
        if interface == 1:
            print(self.Kontrollera())
            if not self.Kontrollera():
                return False
        if interface == 2:
            print(self.creatUser())

    def printSysFunctionView2(self):
        print("Nu logga in på det info som du sparade innan \n ")
        interface = "Så skriv in ditt ifo nu \n"
        print(interface)
        print(self.Kontrollera())
        if not self.Kontrollera():
            return False

    def __init__(self, allUser):
        self.allUser = allUser
        self.userlisd = [Account]
        self.usercard = [Card]
        self.Account = Account

    def creatUser(self):
        print("Du är välkommen att skffa ett konto hos oss. \n")
        print("-----------------------------------------------\n")
        self.__class__.usernew.username = input("Skriv in ditt username \n")

        self.__class__.usernew.FristName = input("Skriv in ditt First name \n")
        self.__class__.usernew.LastName = input("Skriv in ditt last name\n")
        print("Ditt personnummer skriv bara siffror")
        self.__class__.usernew.personnummer = int(input("Skriv in ditt personnummer\n"))
        cardnum = 10001 + random.randint(1, 99) + 1
        self.__class__.usernew.card =  cardnum
        print(self.__class__.usernew.card)
        ise = 100 + random.randint(1, 99) + 1
        self.__class__.usercard.CardId = ise
        print(self.__class__.usercard.CardId)
        print("För att kunna skaffa ett konto du måste sätt in pengar ")
        self.__class__.usercard.CardMoney = float(input("Skriv in hur mycket pengar vill du sätt in\n"))
        if self.__class__.usercard.CardMoney < 0:
            print("Du kan inte öpnna ett konto för utan sätta in pengar\n")
            return False
        self.__class__.usercard.CardPassword = input("Skriv in ditt password \n")

        time.sleep(1)
        self.__class__.usercard.CardId = self.randomCardId()
        data = open("user.txt", "a")
        tb = (self.__class__.usernew.username,self.__class__.usernew.FristName,self.__class__.usernew.LastName,self.__class__.usernew.personnummer,self.__class__.usernew.card, self.__class__.usercard.CardId,  self.__class__.usercard.CardMoney, self.__class__.usercard.CardPassword)
        data.write(str(tb))
        print("Du lyckas att komma in i vår system")

        return True, print(self.Kontrollera())

    def UserInfo(self):
        info = self.verify("Söker efter user")
        if info:
            print("Då du har ", self.__class__.usercard.CardMoney, "\n")
            print("Ditt Card id är  ", self.__class__.usercard.CardId, " \n")
            print("Ditt password är ", self.__class__.usercard.CardPassword, " \n", " \n")
            print("Ditt username ", self.__class__.usernew.username, " \n")
            print("Ditt personnummer ", self.__class__.usernew.personnummer, " \n")
            print("Ditt id är ", self.__class__.usernew.card, " \n")
        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True

    def withdrawmoney(self):
        info = self.verify("dra ut pengar")
        if info:
            money = float(input("Skriv hur mycket vill du dra ut \n"))
            if money > self.__class__.usercard.CardMoney:
                print("Du har inte till räckligt med pengar\n")
                return False

            self.__class__.usercard.CardMoney -= money
            print("DU dra \n", money, "Du har nu i ditt kontot\n", self.__class__.usercard.CardMoney)
        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True

    def putmoneyin(self):
        info = self.verify("sätta in pengar")
        if info:
            money = float(input("Skriv hur mycket vill du sätta in\n"))
            if money <= 0:
                print("Du skrvi ett fel nummer \n")
                return False
            self.__class__.usercard.CardMoney += money
            print("Du har nu ", self.__class__.usercard.CardMoney, " pengar i ditt konto\n")
        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True

    def transferMoney(self):
        pass

    def changePassword(self):
        info = self.verify("Ändra lösenord")
        if info:
            updatePassword = input("Skriv gärna ditt nytt Password\n")
            verifyPassword = input("Var snall och skriva ditt Password igen\n")
            if updatePassword == verifyPassword:
                print("Vi vill att lösenord är bekräftade så vänligt vänta två sekunder\n")
                time.sleep(1)
                self.__class__.usercard.CardPassword = updatePassword
                print("ojjj det lyckas att ändra lösenord du är välkommen att logga in igen \n")
                print("det ta några sekunder till att return till inlogg sida\n")
                time.sleep(1)
                return True
        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True, self.View()

    def låsAnvändare(self):
        info = self.verify("sparr kortet eller konto ")
        if info:
            infoid = input("Skriv gärna ditt kort ID\n")
            if infoid != self.__class__.usercard.CardId:
                print("Du skrive ett fel nummer\n")
                return False
            self.__class__.usercard.CardLock = True
            print("Du lyckas att låsa ditt kort\n")
        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True

    def unLockUser(self):
        cardinfo = input("Skriv in ditt kort ID\n")

        if cardinfo != self.__class__.usercard.CardId:
            print("Du skriv fel ID\n")
            return False
        if cardinfo == self.__class__.usercard.CardId:
            self.__class__.usercard.CardLock = False
            print("Du lyckas att öppna igen ditt konto\n")

        print("Du kommer att gå till baka efter 3 sekunder\n")
        time.sleep(3)
        return True

    def newCard(self):
        pass

    def avbryta(self):
        info = self.verify("avbryta konto")
        if info:
            self.__class__.usernew.card = input("Skriv ditt id \n")
            if self.__class__.usernew.card != self.__class__.usernew.card:
                print("Du skrive ett fel nummer\n")
                return False
            del self.__class__.usernew.card
            print("Du lyckas att ta bort ditt konto\n")
            print("Du kommer att gå till baka efter 3 sekunder\n")
            time.sleep(4)
        return True, self.View()



    def randomnum(self):
        random.randint(1, 20) + 1

    def randomCardId(self):
        while True:
            str1 = ""
            for i in range(6):
                ise = 100 + random.randint(1, 99) + 1
                str1 += str(ise)

            return True

    def verify(self, operation):
        self.__class__.usercard.CardId = input("Skriv in sitt kordnummer\n")
        if not self.__class__.usercard.CardId:
            return False
        return True
