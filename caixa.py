import sys
# Importa os conponentes para a
#  construção das janelas
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout
# construção da classe janela com nome de caixa
class caixa(QWidget):
    #criação do método __init__ que inicia a janela
    # e exibe ela na tela
    def __init__(self):
        super().__init__() 
        # vamos definir a posução e o tamanho da 
        # tela
        self.setGeometry(0,30,1440,830)

        # vamos definir o título da nossa janela
        self.setWindowTitle("Caixa da Loja ")

        # Vamos criar as labels que representam
        # as colunas esquerda e direita

        # Label da esquerda 
        self.label_coluna_esquerda =QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")


        # Label da direita
        self.label_coluna_direita =QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#FFFFFF}")

        # criar o layout horizontal para 
        # as colunas
        self.h_layout =QHBoxLayout()

        # vamos adicionar as colunas
        # esquerda e direita ao layout
        # horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # adicionar o layout na tela
        self.setLayout(self.h_layout)

app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()