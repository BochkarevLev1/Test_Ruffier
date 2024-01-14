from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import(
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout, 
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
class FinalWin(QWidget):    
    def __init__(self, exp): 
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            elif self.index < 0.5:
                return txt_res5
        if self.exp.age >= 13 and self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 12.5 and self.index >= 16.4:
                return txt_res2
            elif self.index < 7.5 and self.index >= 12.4:
                return txt_res3
            elif self.index < 2 and self.index >= 7.4:
                return txt_res4
            elif self.index < 1.9:
                return txt_res5
    def initUI(self):
        self.v_line = QVBoxLayout()
        self.text_index = QLabel(txt_index)
        self.text_workheart = QLabel(txt_workheart + self.results())
        self.v_line.addWidget(self.text_index, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.text_workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
            
