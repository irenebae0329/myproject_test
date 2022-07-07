from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys
import postfix_calculator
from caculator_new_ui import Ui_MainWindow
class myWindow(QWidget,Ui_MainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        self.setupUi(self)


    def backspace(self):
        self.linEdit.backspace()

    def ps_bt1(self):
        self.lineEdit.insert('1 ')

    def ps_bt2(self):
        self.lineEdit.insert('2 ')

    def ps_bt3(self):
        self.lineEdit.insert('3 ')

    def ps_bt4(self):
        self.lineEdit.insert('4 ')

    def ps_bt5(self):
        self.lineEdit.insert('5 ')

    def ps_bt6(self):
        self.lineEdit.insert('6 ')

    def ps_bt7(self):
        self.lineEdit.insert('7 ')

    def ps_bt8(self):
        self.lineEdit.insert('8 ')

    def ps_bt9(self):
        self.lineEdit.insert('9 ')

    def ps_bt0(self):
        self.lineEdit.insert('0 ')

    def ps_bt_clean(self):
        self.lineEdit_clear()

    def ps_bt11(self):
        self.lineEdit.insert('+ ')

    def ps_bt12(self):
        self.lineEdit.insert('- ')

    def ps_bt13(self):
        self.lineEdit.insert('* ')
    def ps_bt14(self):
        self.lineEdit.insert('/ ')
    def ps_bt15(self):
        self.lineEdit.insert('( ')
    def ps_bt16(self):
        self.lineEdit.insert(') ')
    def ps_bt_calcu(self):
        text=postfix_calculator.postfix_operator(self.lineEdit.text())
        self.textBrowser.append('%s'%text)
        self.lineEdit_clear()

    def lineEdit_clear(self):
        self.lineEdit.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    w.pushButton_17.clicked.connect(w.backspace)

    w.pushButton.clicked.connect(w.ps_bt1)
    w.pushButton_3.clicked.connect(w.ps_bt2)
    w.pushButton_9.clicked.connect(w.ps_bt3)
    w.pushButton_10.clicked.connect(w.ps_bt4)
    w.pushButton_7.clicked.connect(w.ps_bt11)
    w.pushButton_4.clicked.connect(w.ps_bt6)
    w.pushButton_11.clicked.connect(w.ps_bt7)
    w.pushButton_17.clicked.connect(w.ps_bt8)
    w.pushButton_2.clicked.connect(w.ps_bt9)
    w.pushButton_5.clicked.connect(w.ps_bt0)
    w.pushButton_8.clicked.connect(w.ps_bt12)
    w.pushButton_20.clicked.connect(w.ps_bt13)
    w.pushButton_19.clicked.connect(w.ps_bt14)
    w.pushButton_6.clicked.connect(w.ps_bt5)

    w.pushButton_14.clicked.connect(w.ps_bt_calcu)

    w.pushButton_16.clicked.connect(w.ps_bt_clean)

    w.pushButton_12.clicked.connect(w.ps_bt15)
    w.pushButton_18.clicked.connect(w.ps_bt16)
    w.show()
    sys.exit(app.exec_())


