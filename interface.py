from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(0, 0, 600, 600)
    window.setWindowTitle("My project")

    layout = QVBoxLayout()
  
    label = QLabel("Hello")
    button = QPushButton("buuon")
    button.clicked.connect(on_clicked)

    layout.addWidget(label)
    layout.addWidget(button)


    window.setLayout(layout)

    window.show()
    app.exec_()


def on_clicked():
    message = QMessageBox()
    message.setText("clicked")
    message.exec_()


if __name__  == '__main__':
    main()

