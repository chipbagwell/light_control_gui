from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
import subprocess


# pins
RED_PIN = '12'
BLU_PIN = '13'
GRN_PIN = '14'
STAIR_RED_PIN = '9'
STAIR_BLU_PIN = '8'
STAIR_GRN_PIN = '7'

ALL_PINS = [RED_PIN, BLU_PIN, GRN_PIN, STAIR_RED_PIN, STAIR_BLU_PIN, STAIR_GRN_PIN]

# nodes
nodes = '31b325'

# commands
cmd_preamble =  ['toolbelt', '-p', 'S1', 'rpc', 's', 'dm', '-d', '50', nodes]
init_pin = lambda pin : cmd_preamble + ['setPinDir', pin, 'True']
color_on = lambda pin : cmd_preamble + ['writePin', pin, 'False']
color_off = lambda pin : cmd_preamble + ['writePin', pin, 'True']

#constants
BUTTON_HEIGHT = 80

def init_leds_clicked():
    print("initing leds")
    for p in ALL_PINS:
        retval = subprocess.run(init_pin(p), capture_output=True, text=True)
        print(retval.stdout)
        retval = subprocess.run(color_on(p), capture_output=True, text=True)
        print(retval.stdout)
        
def red_clicked():
    print("red clicked")
    retval = subprocess.run(color_on(RED_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_on(STAIR_RED_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(GRN_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(STAIR_GRN_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(BLU_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(STAIR_BLU_PIN), capture_output=True, text=True)
    

    print(retval.stdout)

def gold_clicked():
    print("gold_clicked")
    retval = subprocess.run(color_on(RED_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_on(STAIR_RED_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_on(GRN_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_on(STAIR_GRN_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(BLU_PIN), capture_output=True, text=True)
    retval = subprocess.run(color_off(STAIR_BLU_PIN), capture_output=True, text=True)
    print(retval.stdout)

def white_clicked():
    print("white_clicked")
    for p in ALL_PINS:
        retval = subprocess.run(color_on(p), capture_output=True, text=True)
        print(retval.stdout)

def off_clicked():
    print("off_clicked")
    for p in ALL_PINS:
        retval = subprocess.run(color_off(p), capture_output=True, text=True)
        print(retval.stdout)

def exit_clicked():
    exit()

app = QApplication([])
bigger_font = QFont()
bigger_font.setPointSize(32)

screenGeometry = app.desktop().screenGeometry()
x = int((screenGeometry.width() - 800) / 2)
y = int((screenGeometry.height() - 600) / 2)
window = QWidget()
window.setFixedSize(800,600)
window.move(x, y)

init_button = QPushButton('Init LEDs')
init_button.setFixedHeight(BUTTON_HEIGHT)
init_button.setFont(bigger_font)
init_button.setStyleSheet("background-color: gray")
init_button.clicked.connect(init_leds_clicked)

red_button = QPushButton('Red')
red_button.setFixedHeight(BUTTON_HEIGHT)
red_button.setFont(bigger_font)
red_button.setStyleSheet("background-color: red; color: black")
red_button.clicked.connect(red_clicked)

gold_button = QPushButton('Gold')
gold_button.setFixedHeight(BUTTON_HEIGHT)
gold_button.setFont(bigger_font)
gold_button.setStyleSheet("background-color: gold; color: black")
gold_button.clicked.connect(gold_clicked)

white_button = QPushButton('White')
white_button.setFixedHeight(BUTTON_HEIGHT)
white_button.setFont(bigger_font)
white_button.setStyleSheet("background-color: white; color: black")
white_button.clicked.connect(white_clicked)

off_button = QPushButton('Off')
off_button.setFixedHeight(BUTTON_HEIGHT)
off_button.setFont(bigger_font)
off_button.clicked.connect(off_clicked)

exit_button = QPushButton('Quit')
exit_button.setFixedHeight(BUTTON_HEIGHT)
exit_button.setFont(bigger_font)
exit_button.clicked.connect(exit_clicked)

layout = QVBoxLayout()

layout.addWidget(init_button)
layout.addWidget(red_button)
layout.addWidget(gold_button)
layout.addWidget(white_button)
layout.addWidget(off_button)
layout.addWidget(exit_button)


window.setLayout(layout)
window.show()
app.exec()

