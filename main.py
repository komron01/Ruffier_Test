from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout
from instr import *

app = QApplication([])
main_win =QWidget()
main_win.setWindowTitle(title_txt)
main_win.resize(win_width,win_height)

txt1= QLabel(txt1_txt)
txt2_desc=QLabel(description)
btn1= QPushButton(btn1_txt)

v_line = QVBoxLayout()
v_line.addWidget(txt1)
v_line.addWidget(txt2_desc)
v_line.addWidget(btn1, alignment=Qt.AlignCenter)

main_win.setLayout(v_line)

main_win.show()
app.exec_()