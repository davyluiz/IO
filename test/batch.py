import os


def inicialize():
    get_directory()


def get_directory():
    SYSTEM_DRIVE = os.environ['SYSTEMDRIVE']
    PC_NAME = os.environ['COMPUTERNAME']
    USER_PATH = os.path.expanduser('~')
    CURRENT_PATH = os.getcwd()

    print(f"Letra do disco do sistema: {SYSTEM_DRIVE}")
    print(f"Nome da máquina: {PC_NAME}")
    print(f"Diretório do usuário: {USER_PATH}")
    print(f"Diretório atual: {CURRENT_PATH}")


# if __name__ == '__main__':
#     pass
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide2.QtGui import QPixmap, QPainter, QBrush, QPen, QColor, QImage, QPainterPath
from PySide2.QtCore import Qt, QEvent


def destruir_sessao():
    app.quit()


def enter_handler_event(event):
    if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
        fazer_login()


def fazer_login():
    username = username_input.text()
    password = password_input.text()

    if username == "usuario" and password == "senha":
        status_label.setText("Login realizado com sucesso!")
    else:
        status_label.setText("Credenciais inválidas. Tente novamente.")


app = QApplication([])
window = QWidget()
window.setMinimumSize(500, 500)
window.setMaximumSize(500, 500)
window.setWindowTitle("Formulário de Login")

layout = QVBoxLayout()
layout.setSpacing(0)  # Define o espaçamento entre os widgets

# Carregar imagem do usuário
image_label = QLabel()
image_pixmap = QPixmap("../assets/img/agent.png").scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)

# Criar uma imagem redonda
rounded_image = QImage(150, 150, QImage.Format_ARGB32)
rounded_image.fill(Qt.transparent)

painter = QPainter(rounded_image)
painter.setRenderHint(QPainter.Antialiasing)

path = QPainterPath()
path.addEllipse(0, 0, 150, 150)
painter.setClipPath(path)

painter.drawPixmap(0, 0, image_pixmap)
painter.setPen(QPen(QColor("black"), 2))
painter.setBrush(QBrush(Qt.transparent))
painter.drawEllipse(0, 0, 150, 150)

painter.end()

rounded_pixmap = QPixmap.fromImage(rounded_image)
image_label.setPixmap(rounded_pixmap)
image_label.setAlignment(Qt.AlignCenter)
layout.addWidget(image_label)

username_label = QLabel("Usuário:")
username_label.setContentsMargins(0, 0, 0, 0)  # Reduzir espaçamento interno
layout.addWidget(username_label, alignment=Qt.AlignCenter)  # Alinhar label ao centro

username_input = QLineEdit()
username_input.setContentsMargins(0, 0, 0, 0)  # Reduzir espaçamento interno
layout.addWidget(username_input, alignment=Qt.AlignCenter)  # Alinhar campo ao centro

password_label = QLabel("Senha:")
password_label.setContentsMargins(0, 0, 0, 0)  # Reduzir espaçamento interno
layout.addWidget(password_label, alignment=Qt.AlignCenter)  # Alinhar label ao centro

password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.Password)
password_input.setContentsMargins(0, 0, 0, 0)  # Reduzir espaçamento interno
layout.addWidget(password_input, alignment=Qt.AlignCenter)  # Alinhar campo ao centro

login_button = QPushButton("Login")
login_button.clicked.connect(fazer_login)
layout.addWidget(login_button, alignment=Qt.AlignCenter)  # Alinhar botão ao centro

encerrar_button = QPushButton("Encerrar")
encerrar_button.clicked.connect(destruir_sessao)
layout.addWidget(login_button, alignment=Qt.AlignCenter)


status_label = QLabel()
layout.addWidget(status_label, alignment=Qt.AlignCenter)  # Alinhar rótulo ao centro

window.setLayout(layout)
window.show()
app.exec_()
