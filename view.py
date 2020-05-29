from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QLabel, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QWidget, QInputDialog, QLineEdit


class View(QWidget):
    cancelSignal = QtCore.pyqtSignal()
    pauseSignal = QtCore.pyqtSignal()
    passSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.top = 180
        self.left = 80
        self.width = 300
        self.height = 200
        self.createWidget()

    def createWidget(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)

        fontDB = QFontDatabase()
        #fontDB.addApplicationFont("C:/Users/claud/PycharmProjects/BloqAlanna/venv/Scripts/fonts/FakeHope.ttf")
        fontDB.addApplicationFont("./venv/Scripts/fonts/FakeHope.ttf")

        ### ******* imprime todas as fontes ****** #
        # for varriavel in fontDB.families():
        #     print(varriavel)
        ### ************************************** ###
        self.groupBox = QGroupBox("Escolha as Opções")

        self.groupBox.setFixedHeight(90)
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom)

        self.contLabel = QLabel("00:00:00", self)
        self.contLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contLabel.setStyleSheet("QLabel {"
                                     "border-radius:20px;"
                                     "color: black;background-color: #ffd9b3;" #ffcccc , ffd9b3
                                     "font:45pt 'Fake Hope'}")

        hboxL = QHBoxLayout()
        self.pauseButton = QPushButton('&Pause', parent=self)
        self.pauseButton.setStyleSheet('QPushButton {background-color:"salmon";border-radius:15px}')
        self.pauseButton.setFixedHeight(40)
        self.pauseButton.clicked.connect(self.pauseSignal)

        self.cancelButton = QPushButton("&Close", parent=self)
        self.cancelButton.setStyleSheet('QPushButton {background-color:#e6e600;border-radius:15px}')
        self.cancelButton.setFixedHeight(40)
        self.cancelButton.clicked.connect(self.cancelSignal)

        self.senhaButton = QPushButton("&Senha", self)
        self.senhaButton.setStyleSheet('QPushButton {background-color:"pink";border-radius:15px}')
        self.senhaButton.setFixedHeight(40)
        self.senhaButton.clicked.connect(self.passSignal)

        hboxL.addWidget(self.pauseButton)
        hboxL.addWidget(self.cancelButton)
        hboxL.addWidget(self.senhaButton)
        self.groupBox.setLayout(hboxL)

        vbox = QVBoxLayout()
        vbox.addWidget(self.contLabel)
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def mudaBack(self):
        self.contLabel.setStyleSheet("QLabel {"
                                     "border-radius:20px;"
                                     "color: black;background-color: #ff4d4d;"  # ffcccc , ffd9b3
                                     "font:34pt 'Fake Hope'}")

    def getText(self):
        self.text,self.okPress = QInputDialog.getText(self, "Get text", "Your name:", QLineEdit.Password, "")
        return self.text

    def showMessage(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText("Senha correta\n Bem-Vindo")
        messageBox.exec_()

    def showError(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText("Senha errada\nTente denovo...")
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.exec_()

    def QatualizaLabel(self, cont):
        self.contLabel.setText(str(cont))
