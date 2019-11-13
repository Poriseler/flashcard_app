import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QGridLayout, QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit,QFormLayout
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui
from flashcards_dict import saved_dict


class MyAppView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.population=0
        self.setWindowTitle("My flashcards")
        self.setWindowIcon(QtGui.QIcon("logo3.png"))
        self.setFixedSize(450, 200)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.buttons_layout = QGridLayout()
        self.flashcards_base = {}
        self._centralWidget.setLayout(self.generalLayout)
        self._createBar()
        self._createButtons()
        self.update_dict()
        self.range_col = iter([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
                       2, 0, 1, 2])
        self.range_line = iter([3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14])
        self.old_col_range = iter([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1,
                       2, 0, 1, 2])
        self.old_line_range = iter([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14])
        self.old_flashcards()

    def show_text(self, old_content):
        if self.old_button_label.text():
            self.old_button_label.setText("")
        else:
            self.old_button_label.setText(old_content)

    def old_flashcards(self):
        if self.flashcards_base:
            window_flashcards = QDialog(self)
            window_flashcards.setWindowTitle("Saved flashcards")
            oldFlashcardsLayout = QGridLayout()
            self.old_button_label = QLabel("")

            for key in self.flashcards_base:
                old_content = str(self.flashcards_base[key])
                old_button = QPushButton(str(key))
                oldFlashcardsLayout.addWidget(self.old_button_label, 0, 0, 1, 3)
                oldFlashcardsLayout.addWidget(old_button, next(self.old_line_range), next(self.old_col_range))
                old_button.clicked.connect(lambda checked, t=old_content: self.show_text(t))
                window_flashcards.setLayout(oldFlashcardsLayout)

            window_flashcards.show()

    def update_dict(self):
        self.flashcards_base.update(saved_dict)

    def example_text(self):
        if self.msg_label.text():
            self.msg_label.setText("")
        else:
            self.msg_label.setText("It's how flashcards will be displayed.")

    def example_instr(self):
        if self.instr_label.text():
            self.instr_label.setText("")
        else:
            self.instr_label.setText("If You want to add a new flashcards, choose proper option from the bar. Don't forget to save them before You close the program!")

    def example_about(self):
        if self.about_label.text():
            self.about_label.setText("")
        else:
            self.about_label.setText(" Version: 0.1 \n Author: Aleksander Kamiński")

    def show_content(self, content):
        if self.contentLabel.text():
            self.contentLabel.setText("")
        else:
            self.contentLabel.setText(content)
            self.contentLabel.setWordWrap(True)

    def _createButtons(self):
        btn = QPushButton("Example flashcard")
        self.buttons_layout.addWidget(btn,0,0)
        self.msg_label = QLabel("")
        self.msg_label.setWordWrap(True)
        self.msg_label.setAlignment(Qt.AlignTop)
        self.buttons_layout.addWidget(self.msg_label,1,0)
        btn.clicked.connect(self.example_text)

        btn_instru = QPushButton("Instruction")
        self.buttons_layout.addWidget(btn_instru,0,1)
        self.instr_label = QLabel("")
        self.instr_label.setWordWrap(True)
        self.instr_label.setAlignment(Qt.AlignTop)
        self.buttons_layout.addWidget(self.instr_label,1,1)
        btn_instru.clicked.connect(self.example_instr)

        btn_about = QPushButton("About")
        self.buttons_layout.addWidget(btn_about,0,2)
        self.about_label = QLabel("")
        self.about_label.setWordWrap(True)
        self.about_label.setAlignment(Qt.AlignTop)
        self.buttons_layout.addWidget(self.about_label,1,2)
        btn_about.clicked.connect(self.example_about)

        self.generalLayout.addLayout(self.buttons_layout)

    def _createFlash(self):
        local_name = QPushButton(str(self.population))
        self.new_window(local_name)
        self.population += 1


    def new_window(self, local_name):
        mydialog = QDialog(self)
        mydialog.setWindowTitle("New flashcard")
        self.titleTextbox = QLineEdit()
        self.titleTextbox.setMaxLength(30)
        self.titleTextbox.setPlaceholderText("Max 30 characters")
        self.contentTextbox = QTextEdit()
        self.contentTextbox.setPlaceholderText("Don't be ashamed, save Your answer!")
        formLayout = QFormLayout()
        formLayout.addRow('Title:', self.titleTextbox)
        formLayout.addRow('Content:', self.contentTextbox)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        formLayout.addWidget(buttonBox)
        mydialog.setLayout(formLayout)
        buttonBox.accepted.connect(lambda :self.save(mydialog, local_name))
        buttonBox.rejected.connect(mydialog.reject)

        mydialog.show()


    def save(self, mydialog, local_name):
        title = self.titleTextbox.text()
        content = self.contentTextbox.toPlainText()
        self.flashcards_base[title] = content
        self.titleTextbox = title
        self.contentTextbox = content
        local_name.setText(title)

        self.buttons_layout.addWidget(local_name,next(self.range_line), next(self.range_col))
        self.contentLabel = QLabel("")
        self.contentLabel.setWordWrap(True)
        self.contentLabel.setAlignment(Qt.AlignTop)
        self.buttons_layout.addWidget(self.contentLabel,2,0,1,3)
        local_name.clicked.connect(lambda :self.show_content(content))

        mydialog.close()

    def save_session(self):
        base = self.flashcards_base
        myfile = open('flashcards_dict.py', 'w')
        myfile.write('saved_dict = {}'.format(base))
        myfile.close()

    def _createBar(self):
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)
        self.menu.addAction('&Add flashcard', self._createFlash)
        self.menu.addAction('&Save', self.save_session)

def main():

    flashcards = QApplication(sys.argv)
    view = MyAppView()
    view.show()
    sys.exit(flashcards.exec())

if __name__ == '__main__':
    main()