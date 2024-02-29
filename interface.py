import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NLTK")
        self.setWindowIcon(QIcon("icons/python.ico"))

        mainStyleSheet = (
            "background-color: #585858"
        )

        self.setStyleSheet(mainStyleSheet)
        self.resize(1000, 800)
        self.center()

        
        self.main_vlayout = QVBoxLayout()
        self.main_hlayout = QHBoxLayout()
        self.leftSideSelector_layout = QVBoxLayout()

        self.main_vlayout.addLayout(self.main_hlayout)

        self.main_hlayout.addLayout(self.leftSideSelector_layout)


        self.label = QLabel("Drop file here or click to select")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_hlayout.addWidget(self.label)

        self.button = QPushButton("Select File")
        self.button.clicked.connect(self.selectFile)
        self.main_hlayout.addWidget(self.button)

        self.setAcceptDrops(True)


    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        center_point = screen_geometry.center()
        self.move(center_point - self.rect().center())

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            print("File dropped:", files[0])

    def selectFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select File")
        if filename:
            print("File selected:", filename)

    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()