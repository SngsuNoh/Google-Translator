import sys
from PyQt5.QtWidgets import *
from googletrans import Translator


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.lbl1 = QLabel('한국어:', self)
        self.lbl2 = QLabel('영어:', self)
        self.le = QLineEdit(self)
        self.te = QTextEdit(self)
        self.trans_btn = QPushButton('번역', self)
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.le)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.te)
        vbox.addWidget(self.trans_btn)
        self.setLayout(vbox)

        self.trans_btn.clicked.connect(self.translate_kor)
        self.le.editingFinished.connect(self.translate_kor)

        self.setWindowTitle('Google Translator')
        self.setGeometry(200, 200, 400, 300)
        self.show()

    def translate_kor(self):
        text_kor = self.le.text()
        text_en = self.translator.translate(text_kor).text
        self.te.setText(text_en)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())