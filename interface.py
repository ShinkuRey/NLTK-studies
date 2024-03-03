import sys
import nltk_studies as ns
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QSplitter, QInputDialog, QLineEdit, QTextEdit, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QGridLayout

import io

from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QIcon, QAction, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NLTK")
        self.setWindowIcon(QIcon("icons/python.ico"))


        main_style = (
            "background-color: #FFFFFF"
        )

        self.setStyleSheet(main_style)
        self.resize(1500, 800)
        self.center()


        self.main_layout = QVBoxLayout(self)
        self.main_content_layout = QHBoxLayout()

        self.left_menu_widget = QWidget()
        self.left_menu_layout = QVBoxLayout(self.left_menu_widget)
        self.left_menu_widget.setMinimumWidth(150)
        self.left_menu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.content = QWidget()
        self.content_layout = QVBoxLayout()
        self.content.setLayout(self.content_layout)

        self.drop_label = QLabel("Drop file here or click to select")
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(self.drop_label)

        self.drop_button = QPushButton("Select File")
        self.drop_button.clicked.connect(self.selectFile)
        self.content_layout.addWidget(self.drop_button)

        self.main_content_layout.addWidget(self.left_menu_widget)
        self.main_content_layout.addWidget(self.content)        

        self.main_content_widget = QWidget()
        self.main_content_widget.setLayout(self.main_content_layout)

        self.splitter = QSplitter()

        splitter_style = (
            "QSplitter::handle {"
                "background-color: #c0c0c0;"
                "border: 1px solid #707070;"
            "}"
        )

        self.splitter.setStyleSheet(splitter_style)

        self.splitter.addWidget(self.left_menu_widget)
        self.splitter.addWidget(self.main_content_widget)

        self.main_layout.addWidget(self.splitter)

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
            for file_path in files:
                file_name = QFileInfo(file_path).fileName()
                file_button = QPushButton(file_name)
                self.left_menu_layout.addWidget(file_button)
                file_button.clicked.connect(lambda _, path=file_path: self.analyze(file_path)) 


    def selectFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file:
            
            file_name = QFileInfo(file).fileName()
            file_button = QPushButton(file_name)
            self.left_menu_layout.addWidget(file_button)
            file_button.clicked.connect(lambda _, path=file_name: self.analyze(file_name)) 


    

    def analyze (self, file_path):
        raw_text, word_tokens, sent_tokens, word_tokens_wsw = ns.read_file(file_path)
            
        max_length, max_length_word = ns.max_length(word_tokens_wsw)
            
        unique_words, unique_words_number = ns.unique_words(word_tokens_wsw)

        word_number = ns.token_number(word_tokens_wsw)
        sent_number = ns.token_number(sent_tokens)
        character_number = ns.token_number(raw_text)

        average_word_length = ns.average_words_length(word_tokens, raw_text)
        average_sent_length = ns.average_sent_length(sent_tokens, raw_text)
        average_words_in_sent = ns.average_words_sent(word_tokens, sent_tokens)
        
        img, words_list = ns.word_cloud(word_tokens_wsw)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        pixmap = QPixmap()
        pixmap.loadFromData(img_byte_array.getvalue())
        
        sorted_collocations = ns.collocations(word_tokens_wsw, num=20)
        
        for i in reversed(range(self.content_layout.count())): 
            self.content_layout.itemAt(i).widget().setParent(None)

        self.analyzed_content = QWidget()
        self.analyzed_content_layout = QHBoxLayout(self.analyzed_content)

        self.left_results = QWidget()
        self.left_results_layout = QVBoxLayout(self.left_results)

        self.center_results = QWidget()
        self.center_results_layout = QVBoxLayout(self.center_results)

        self.right_results = QWidget()
        self.right_results_layout = QVBoxLayout(self.right_results)


        self.left_results_layout.addWidget(QLabel(f"""Самое длинное слово "{max_length_word}" 
        оно состоит из: {max_length} символов"""))
        self.left_results_layout.addWidget(QLabel(f"В корпусе {unique_words_number} уникальных слов"))
        self.left_results_layout.addWidget(QLabel(f"""Всего корпус насчитывает: 
                                                  
        {word_number} слов, 
        {sent_number} предложений, 
        {character_number} знаков"""))
        self.left_results_layout.addWidget(QLabel(f"""Таким образом:
                                                  
        среднее количество знаков на слово {average_word_length}, 
        среднее количество слов в предложении {average_words_in_sent},
        среднее количество знаков в предложении {average_sent_length}"""))



        self.center_results_layout.addWidget(QLabel(f"Самые часто используемые каллокации:"))
        for collocation in sorted_collocations:
            label_text = f"{collocation[0]}: {collocation[1]}"
            label = QLabel(label_text)
            self.center_results_layout.addWidget(label)

        self.word_cloud_label = QLabel()
        self.word_cloud_label.setPixmap(pixmap)
        self.right_results_layout.addWidget(self.word_cloud_label)

        self.words_grid = QWidget()
        self.words_grid_layout = QGridLayout(self.words_grid)

        for index, word in enumerate(words_list):
            label_text = f"{word[0]}: {word[1]}"
            label = QLabel(label_text)
            row = index // 3  
            col = index % 3  
            self.words_grid_layout.addWidget(label, row, col)

        self.right_results_layout.addWidget(self.words_grid)
        
        self.right_results_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.analyzed_content_layout.addWidget(self.left_results)
        self.analyzed_content_layout.addWidget(self.center_results)
        self.analyzed_content_layout.addWidget(self.right_results)


        self.content_layout.addWidget(self.analyzed_content)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()