import sys
# Importa os conponentes para a
#  construção das janelas
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
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
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#a65505}")


        # Label da direita
        self.label_coluna_direita =QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#FFFFFF}")

        #----  cria o conteúdo da coluna da Esquerda ----
        self.v_layout_esquerda = QVBoxLayout()
        # Vamos criar uma label para adicionar uma nogo da nossa 
        # loja
        self.log_label = QLabel()
        self.log_label.setPixmap(QPixmap("C:/Users/kayque.fssa/Documents/JanelaCaixa/.venv/logo.png"))
        self.log_label.setFixedHeight(200)
        self.log_label.setFixedWidth(200)
        # Ajustar a label com a image para ficar do tamanho
        # ideal
        self.log_label.setScaledContents(True)
        # adicionar a label com a imagem na tela
        self.v_layout_esquerda.addWidget(self.log_label)





        # vamos criar as labels e as linesEdits que ficarão na coluda
        # da esquerda, dentro do layout vertical da esquerda

        # Codigo do Produto

        self.codigo_produto_label =QLabel("Codigo do Produto:")
        self.codigo_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.codig_produto_edit = QLineEdit()
        self.codig_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codig_produto_edit)

        # Nome do Produto

        self.nome_produto_label = QLabel("Nome do Produto:")
        self.nome_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.nome_produto_edit = QLineEdit()
        self.nome_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        # Discrição do Produto

        self.discricao_produto_label = QLabel("Discrição do Produto:")
        self.discricao_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.discricao_produto_edit = QLineEdit()
        self.discricao_produto_edit.setStyleSheet("QLineEdit{padding:25px}")
        self.v_layout_esquerda.addWidget(self.discricao_produto_label)
        self.v_layout_esquerda.addWidget(self.discricao_produto_edit)

        # Quantidade do Produto

        self.quantidade_pruduto_label = QLabel("Quantidade do produto:")
        self.quantidade_pruduto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.quantidade_produto_edit = QLineEdit()
        self.quantidade_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.quantidade_pruduto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        # Preço Unitário do Produto

        self.preco_unitario_produto_label = QLabel("Preço Unitário do Produto:")
        self.preco_unitario_produto_label.setStyleSheet("QLabel{font-size:15pt}")
        self.preco_unitario_produto_edit = QLineEdit()
        self.preco_unitario_produto_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_edit)

        # Sub Total

        self.sub_total_label = QLabel("Sub Total:")
        self.sub_total_label.setStyleSheet("QLabel{font-size:15pt}")
        self.sub_total_edit = QLineEdit()
        self.sub_total_edit.setStyleSheet("QLineEdit{padding:5px}")
        self.v_layout_esquerda.addWidget(self.sub_total_label)
        self.v_layout_esquerda.addWidget(self.sub_total_edit)

        #  Adicionar o layout da vertical da esquerda
        #  com todos os controles :label e loneEdit dento
        #  da coluna da esquerda (label_coluna_esquerda)
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)



        # ---------- controles da coluna da direita --------------------
        self.v_layout_direita = QVBoxLayout()
        # criar uma tabela e adicionar na coluna da direita
        # esta tabela terá os nomes dos campos estão ao lado esquerdo
        # colunas da tabela
        colunas =["cod.produto","Nome do Produto","Descrição","Quantidade","Preço Unitário", "Sub Total"]
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)
        
        self.total_pagar_label = QLabel("Total a Pagar")
        self.total_parar_edit = QLineEdit()
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_parar_edit)
        
        #  Adicionar o layout da vertical da esquerda
        #  com todos os controles :label e loneEdit dento
        #  da coluna da esquerda (label_coluna_esquerda)
        self.label_coluna_direita.setLayout(self.v_layout_direita)





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