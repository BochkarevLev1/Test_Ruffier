from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import(
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout, 
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit,)
from final_win import *
from instr import *
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.set_appear()
        self.initUI()
        self.connects()
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer1Event (self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.test_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.test_timer.setFont(QFont("color: rgb(0,0,0)"))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def test_timer(self):
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)  
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        #создали виджеты для l_line
        self.text_hintname = QLineEdit(txt_hintname)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_hintage =  QLineEdit(txt_hintage)
        self.text_hinttest1 = QLineEdit(txt_hinttest1)
        self.text_hinttest2 = QLineEdit(txt_hinttest2)
        self.text_hinttest3 = QLineEdit(txt_hinttest3)
        self.text_test1 = QLabel(txt_test1)
        self.text_startest1 = QPushButton(txt_starttest1)
        self.text_test2 = QLabel(txt_test2)
        self.text_startest2 = QPushButton(txt_starttest2)
        self.text_test3 = QLabel(txt_test3)
        self.text_startest3 = QPushButton(txt_starttest3)
        self.button = QPushButton(txt_next)
        #добавить виджеты в l_line
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_hintname, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_hintage, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.button, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_hinttest1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_startest1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_startest2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_hinttest2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_hinttest3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_startest3, alignment = Qt.AlignCenter)
        #добавить виджеты в r_line
        self.text_timer = QLabel(txt_timer)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def next_click(self):
        self.hide()
        self.exp = Experiment (int(self.text_hintage.text()), self.text_hinttest1.text(), self.text_hinttest2.text(), self.text_hinttest3.text())
        self.fw = FinalWin(self.exp)
    def connects(self):
        self.button.clicked.connect(self.test_timer)
        self.text_startest1.clicked.connect(self.next_click)
        self.text_startest2.clicked.connect(self.timer_sits)
        self.text_startest3.clicked.connect(self.timer_final)
        
