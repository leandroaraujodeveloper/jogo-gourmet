import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox, QInputDialog

from utils import NodoArvore
from models import Game
class FormPrato(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FormPrato, self).__init__(parent)
        self.setWindowTitle("Jogo Gourmet")

        self.edit = QLineEdit()
        self.button_ok = QPushButton("OK")
        self.label = QLabel("Pense em um prato que voce gosta.")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_ok)
        
        self.your_game = Game()
        self.raiz = self.your_game.reset_game()

        self.button_ok.clicked.connect(self.game)

    def game(self, prato_atual=None, request=QMessageBox.Ok):
        prato_recente = None
        next_iteration = 0

        if request == QMessageBox.Ok:
            prato_atual = self.your_game.reset_game()

        request = self.show_help(self.your_game.pergunta(prato_atual))
        if request == QMessageBox.No:
            prato_recente = prato_atual
            prato_atual = prato_atual.esquerda

            if prato_atual is None:
                diff =  self.show_edit(self.your_game.pergunta_novo_prato())
                chave = self.show_edit(self.your_game.pergunta_diferenca(prato_recente))
                self.your_game.insertLeft(self.raiz, chave, diff)
                return
            return self.game(prato_atual, next_iteration)
        elif request == QMessageBox.Yes:
            prato_atual = prato_atual.direita
            if prato_atual is None:
                self.show_sucess("Acertei de novo!!")
                return
            return self.game(prato_atual, next_iteration)       

    def show_edit(self, message):
        text, ok = QInputDialog().getText(self, "Complete",
                                     message, QLineEdit.Normal)
        return text

    def show_sucess(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(message)
        msg.setWindowTitle("Jogo Gourmet")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec()
        return retval

    def show_help(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)

        msg.setText(message)
        msg.setWindowTitle("Jogo Gourmet")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec()
        return retval

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = FormPrato()
    widget.resize(200, 100)
    widget.show()   

    sys.exit(app.exec())