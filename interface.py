# from PyQt5.QtWidgets import * 
# from PyQt5.QtCore import Qt
# import nltk_studies



# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setGeometry(0, 0, 600, 600)
#     window.setWindowTitle("My project")

#     layout = QVBoxLayout()
  
#     label = QLabel("Drag a file or fill in the box")
#     button = QPushButton("button")
#     button.clicked.connect(on_clicked)

#     layout.addWidget(label)
#     layout.addWidget(button)


#     window.setLayout(layout)

#     window.show()
#     app.exec_()


# def on_clicked():
#     message = QMessageBox()
#     message.setText("clicked")
#     message.exec_()


# if __name__  == '__main__':
#     main()
import nltk_studies as ns
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

class FileSelectWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Selector")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Drop file here or click to select")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Select File")
        self.button.clicked.connect(self.selectFile)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_AnalysisWindow(self, filename):
        self.analysis_window = AnalysisWindow(filename)
        self.analysis_window.show()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            self.label.setText(files[0])

    def selectFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select File")
        if filename:
            self.open_AnalysisWindow(filename)
            

    
            

class AnalysisWindow(QWidget):
    def __init__(self, filename):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel(ns.read_file(filename))
        layout.addWidget(self.label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = FileSelectWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()