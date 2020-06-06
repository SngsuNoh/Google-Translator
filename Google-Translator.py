#version 0.1 (2020-06-06)
#made by Seoung-su 'HAIL' NOH

import sys
from PyQt5.QtWidgets import *
from googletrans import Translator


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.translator = Translator()
        #googletrans Translator 객체를 생성했다.
        self.initUI()

    def initUI(self):
        #KortoEn
        self.KorEn = QWidget()
        self.lbl1 = QLabel()
        self.lbl1.setText('번역할 텍스트를 입력하세요')
        self.before1 = QTextEdit()
        self.lbl2 = QLabel()
        self.lbl2.setText('번역 결과입니다')
        self.after1 = QTextEdit()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lbl1)
        vbox1.addWidget(self.before1)
        vbox1.addWidget(self.lbl2)
        vbox1.addWidget(self.after1) #텍스트 편집기와 라벨 두 개를 수직 박스 레이아웃으로 정렬했다.
        self.KorEn.setLayout(vbox1)

        self.before1.textChanged.connect(self.translate_kor)
        #사용자가 입력한 텍스트가 바뀔 때 마다 translate_kor 메소드를 호출하여 실시간 번역이 가능하도록 한다.

        #EntoKor
        self.EnKor = QWidget()
        self.lbl3 = QLabel()
        self.lbl3.setText('번역할 텍스트를 입력하세요')
        self.before2 = QTextEdit()
        self.lbl4 = QLabel()
        self.lbl4.setText('번역 결과입니다')
        self.after2 = QTextEdit()

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lbl3)
        vbox2.addWidget(self.before2)
        vbox2.addWidget(self.lbl4)
        vbox2.addWidget(self.after2)
        self.EnKor.setLayout(vbox2)

        self.before2.textChanged.connect(self.translate_en)

        #Tab
        tabs = QTabWidget()
        tabs.addTab(self.KorEn, '한글을 영어로')
        tabs.addTab(self.EnKor, '영어를 한글로')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)

        #WindowSetting
        self.setWindowTitle('Google Translator')
        self.setGeometry(200, 200, 400, 300)
        self.show()

    def translate_kor(self):
        text_kor = self.before1.toPlainText()
        if len(text_kor) != 0: #영한번역에서 텍스트를 입력했다가 지우면 강제종료되는 경우가 있어 예외처리했다.
            text_en = self.translator.translate(text_kor).text
            self.after1.setText(text_en) #번역한 결과를 after 라벨에 표시

    def translate_en(self):
        text_en = self.before2.toPlainText()
        if len(text_en) != 0: #텍스트를 입력했다가 지우면 강제종료되는 경우가 있어 예외처리했다.
            text_kor = self.translator.translate(text_en, src="en", dest="ko").text
            #src="번역 전 언어", dest="번역 후 언어" 로 설정한다.
            self.after2.setText(text_kor)

    def closeEvent(self, event): #closeEvent 이벤트 핸들러를 재구성해 종료 시 확인 창이 나타나도록 했다.
        endMessage = QMessageBox()
        endMessage.setWindowTitle("종료하기")
        endMessage.setText("번역기를 종료하시겠습니까?")
        endMessage.setDetailedText("써주셔서 감사합니다 :D")

        reply = endMessage.question(self, "", endMessage.text(),
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #반환값을 reply에 저장하고 조건문에 진입한다.

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())