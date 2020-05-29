import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from model import Model
from view import View


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = View()
        self.init()
        self._model.Qler()

        self.ctimer = QTimer()
        self.ctimer.timeout.connect(self.atualizaContador)
        self.ctimer.start(1110)

        self._contadorStart = 0 # contador variavel para gravar no txt
        self.contadorEnd = 600 # contante variavel para gravar no txt


    # signal passado dos button """
    def init(self):
        #self._view.cancelSignal.connect(partial(self._model.verifPause, 'cancel'))# passar argumento p/funcao
        #self._view.pauseSignal.connect(partial(self._model.verifPause, True))# passar argumento p/funcao
        #self._view.senhaSignal.connect(partial(self._model.verifPause, 'senha'))# passar argumento p/funcao

        self._view.cancelSignal.connect(self.closeApp)
        self._view.pauseSignal.connect(self._model.verifPause)
        self._view.passSignal.connect(self.verify_credentials)

    def closeApp(self):
         
        self._model.QGoodBye
        self._model.password = self._view.getText()
        if self._model.verify_password():
            self._model.QGrava(2)
            self._view.close()
        else:
            self._view.showError()

    def atualizaContador(self):
        self.t = self._model.QAtualizaContador()
        self._view.QatualizaLabel(self.t)

        if self._contadorStart == self.contadorEnd:
            self._model.QGrava(2)
            self._contadorStart = 0

        self._contadorStart += 1

    def verify_credentials(self):

        #self._model.username = self._view.username
        self._model.password = self._view.getText()

        if  self._model.verify_password():
            self._view.showMessage()
            self._model.AddUmaHora()
            self._model.QGrava(2)

        else:
            self._view.showError()

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == '__main__':

    c = Controller()
    sys.exit(c.run())

