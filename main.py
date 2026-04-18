class Kalkulyator:
    def __init__(self):
        self.raqam = 0
        self.ishora = 0

    def son_kirish(self):
        self.raqam = float(input("Son kiriting: "))

    def ishora_kirish(self):
        self.ishora = input("Ishora kiriting (+, -, *, /): ")

    def hisoblash(self):
        if self.ishora == "+":
            return self.raqam + float(input("Son kiriting: "))
        elif self.ishora == "-":
            return self.raqam - float(input("Son kiriting: "))
        elif self.ishora == "*":
            return self.raqam * float(input("Son kiriting: "))
        elif self.ishora == "/":
            if float(input("Son kiriting: ")) != 0:
                return self.raqam / float(input("Son kiriting: "))
            else:
                return "Bo'lishda 0 ga bo'lish qilmaslik kerak!"
        else:
            return "Ishora noto'g'ri!"

    def chiqish(self):
        print("Natija:", self.hisoblash())

kalkulyator = Kalkulyator()
while True:
    print("1. Son kirish")
    print("2. Ishora kirish")
    print("3. Hisoblash")
    print("4. Chiqish")
    print("5. Exit")
    tanlov = int(input("Tanlovni kiriting: "))
    if tanlov == 1:
        kalkulyator.son_kirish()
    elif tanlov == 2:
        kalkulyator.ishora_kirish()
    elif tanlov == 3:
        kalkulyator.chiqish()
    elif tanlov == 4:
        break
    elif tanlov == 5:
        print("Chiqish")
        break
    else:
        print("Notog'ri tanlov!")
