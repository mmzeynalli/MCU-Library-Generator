from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog, QMainWindow)

import os
from entities import Function, Variable, Configuration
import generator

class LibGeneratorUI(QDialog):

    num_of_funcs = 0

    def __init__(self, parent=None):
        super(LibGeneratorUI, self).__init__(parent)

        self.layout = QGridLayout(self)
        self.workspace = os.path.dirname(os.path.realpath(__file__))  # current working folder

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(1000, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, 'Function')
        self.tabs.addTab(self.tab2, 'Defines and variables')

        self.tab1_layout = QVBoxLayout()
        self.tab1_layout.setSpacing(10)

        # Create first tab
        self.functions_list = []

        self.create_functions_tab()
        #self.createDefinesTab()

        # Add tabs to widget
        self.tab1.setLayout(self.tab1_layout)

        self.layout.addWidget(self.tabs)
        self.addGenerateButton()

        self.setLayout(self.layout)
        self.setGeometry(700, 400, 400, 50)
        self.setWindowTitle('MCU Library Generator v1.0.0')
        self.setStyle('Fusion')

    def setStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(QApplication.palette())

    def create_functions_tab(self):

        self.conf_box = QGroupBox('Configurations')
        self.confs_layout = QGridLayout()
        self.createConfBox()


        self.functions_box = QGroupBox('Functions')
        self.functions_layout = QGridLayout()

        add_func_button = QPushButton('Add function')
        add_func_button.setIcon(QtGui.QIcon('img/add.jpg'))
        add_func_button.clicked.connect(self.addFunction)
        self.functions_layout.addWidget(add_func_button, 0, 0)

        self.addFunction()

        self.tab1_layout.addWidget(self.conf_box)
        self.tab1_layout.addWidget(self.functions_box)

    def createConfBox(self):

        lbl_username = QLabel('Creators Full Name')
        txt_username = QLineEdit()

        lbl_dir = QLabel('Project Directory')

        bt_dir = QPushButton("...")
        bt_dir.setFixedSize(30, 20)
        bt_dir.clicked.connect(self.get_work_dir)

        # to use in get_work_dir function
        self.txt_dir = QLineEdit()
        self.txt_dir.setText(self.workspace)
        self.txt_dir.setCursorPosition(0)

        ######################################

        lbl_file_name = QLabel('Module (Library) name: ')
        txt_file_name = QLineEdit()
        txt_file_name.setText('sim800')

        self.config = Configuration(txt_username, self.txt_dir, txt_file_name)

        self.confs_layout.addWidget(lbl_username, 0, 0)
        self.confs_layout.addWidget(txt_username, 0, 1, 1, 20)
        self.confs_layout.addWidget(lbl_dir, 1, 0)
        self.confs_layout.addWidget(self.txt_dir, 1, 1, 1, 20)
        self.confs_layout.addWidget(bt_dir, 1, 21)
        self.confs_layout.addWidget(lbl_file_name, 2, 0)
        self.confs_layout.addWidget(txt_file_name, 2, 1, 1, 20)

        self.conf_box.setLayout(self.confs_layout)

    def get_work_dir(self):
        self.workspace = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        self.txt_dir.setText(self.workspace)
        self.txt_dir.setCursorPosition(0)

    def addFunction(self):

        lbls = [QLabel('Return Type'), QLabel('Scope'), QLabel('Function Name'), QLabel('Arguments')]

        for lbl in lbls:
            lbl.setAlignment(Qt.AlignCenter)

        type = QComboBox(self.functions_box)
        type.addItems(['void', 'int', 'char *', 'bool', 'uint32_t'])
        type.setEditable(True)

        visibility = QComboBox(self.functions_box)
        visibility.addItems(['private', 'public'])
        visibility.setFixedWidth(100)

        name = QLineEdit()
        #arg_cnt = QSpinBox(self.functions_box)
        argv = QLineEdit()

        self.functions_list.append(Function(self.functions_layout, type, visibility, name, argv))

        self.functions_layout.addWidget(lbls[0], 1, 0)
        self.functions_layout.addWidget(lbls[1], 1, 1)
        self.functions_layout.addWidget(lbls[2], 1, 4)
        self.functions_layout.addWidget(lbls[3], 1, 18)

        self.functions_layout.addWidget(type, 2 + self.num_of_funcs, 0)
        self.functions_layout.addWidget(visibility, 2 + self.num_of_funcs, 1)
        self.functions_layout.addWidget(name, 2 + self.num_of_funcs, 2, 1, 6)
        self.functions_layout.addWidget(argv, 2 + self.num_of_funcs, 8, 1, 20)

        self.num_of_funcs += 1
        self.functions_box.setLayout(self.functions_layout)

    def addGenerateButton(self):
        generateButton = QPushButton(' Generate')
        generateButton.clicked.connect(self.generateCode)
        generateButton.setIcon(QtGui.QIcon('img/generate.jpg'))

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(generateButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.layout.addLayout(vbox, 1, 0)

    def generateCode(self):
        generator.generateModule(self.config, self.functions_list, [], [])

if __name__ == '__main__':

    app = QApplication([])
    interface = LibGeneratorUI()
    interface.show()
    app.exec_()
