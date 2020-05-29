from datetime import timedelta, date
import keyboard as key


class Model:

    def __init__(self):
        #self.username = ""
        self.password = ""

        self.add1Hora = timedelta(hours=1, minutes=0, seconds=0)  # variavel add apos senha
        self.bloq = timedelta(hours=0, minutes=0, seconds=1)  # varivel de limite bloqueio
        self.default = timedelta(hours=3, minutes=0, seconds=0)  # variavel de default
        self.notPath = timedelta(hours=0, minutes=0, seconds=10)  # variavel default caso o arquivo tenha sido excluido
        self.now = date.today()
        self.status = True #variavel para bloquear

    def verify_password(self):
        # return self.username == "USER" and self.password == "PASS"
        return self.password == '134'

    def AddUmaHora(self):
        self.default += self.add1Hora
        self.status = True

    def verifPause(self):
        if self.status:
            self.status = False
            self.QBloqueia()
            self.QGrava(2)
        else:
            self.status = True
            key.unhook_all()
            print('desbloqueio')

    def QBloqueia(self):
            key.block_key('w')
            key.block_key('s')
            key.block_key('a')
            key.block_key('d')
            key.block_key('space')
            key.block_key('up')
            key.block_key('down')
            key.block_key('left')
            key.block_key('right')

    def QAtualizaContador(self):
        if self.status and (str(self.default) >= str(self.bloq)):
            self.default -= timedelta(seconds=1)
            return str(self.default)
        else:
            print('esta bloqueado')
            self.status = False
            self.QBloqueia()
            return str(self.default)

    def QGrava(self, ModRecord):
        if ModRecord == 1:
            with open("data.txt", "w") as f:
                f.write(str(self.default))
        if ModRecord == 2:  ## pause ##
            with open("data.txt", "w") as f:
                f.write(str(self.now) + '\n')
                f.write(str(self.default))
                print("gravou")

    def QGoodBye(self):
        with open("data.txt", "w") as f:
            f.write(str(self.default))

    def Qler(self):
        try:
            with open("data.txt", "r") as f:
                self.res = f.read().splitlines()
        except IOError:
            with open("data.txt", "w") as f:
                print('no path')
                f.write(str(self.now) + '\n')
                f.write(str(self.default))
            with open("data.txt", "r") as f:
                self.res = f.read().splitlines()

        fileH = self.res[1]
        self.hh = fileH[0:1]
        self.mm = fileH[2:4]
        self.ss = fileH[5:7]

        if str(self.res[0]) != str(self.now):# compara a data
            self.QGrava(2)
        else:
            self.default = timedelta(hours=float(self.hh), minutes=float(self.mm), seconds=float(self.ss))

