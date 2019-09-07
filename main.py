from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog, QMainWindow)

import os
from entities import Function, Variable


class LibGenerator(QDialog):

    num_of_funcs = 0

    def __init__(self, parent=None):
        super(LibGenerator, self).__init__(parent)

        self.layout = QGridLayout(self)

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
        self.setLayout(self.layout)

        self.setGeometry(700, 400, 400, 50)
        self.setWindowTitle('MCU Library Generator v1.0.0')
        self.setStyle('Fusion')

    def setStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(QApplication.palette())

    def create_functions_tab(self):

        self.conf_box = QGroupBox('Configurations')
        self.confs = QGridLayout()
        self.createConfBox()


        self.functions_box = QGroupBox('Functions')
        self.functions = QGridLayout()

        add_func_button = QPushButton('Add function')
        add_func_button.setIcon(QtGui.QIcon('img/add.jpg'))
        add_func_button.clicked.connect(self.addFunction)
        self.functions.addWidget(add_func_button, 0, 0)

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
        self.txt_dir.setText(os.path.dirname(os.path.realpath(__file__)))
        self.txt_dir.setCursorPosition(0)

        ######################################

        lbl_file_name = QLabel('Module (Library) name: ')
        txt_file_name = QLineEdit()
        txt_file_name.setText('sim800')

        self.confs.addWidget(lbl_username, 0, 0)
        self.confs.addWidget(txt_username, 0, 1, 1, 20)
        self.confs.addWidget(lbl_dir, 1, 0)
        self.confs.addWidget(self.txt_dir, 1, 1, 1, 20)
        self.confs.addWidget(bt_dir, 1, 21)
        self.confs.addWidget(lbl_file_name, 2, 0)
        self.confs.addWidget(txt_file_name, 2, 1, 1, 20)

        self.conf_box.setLayout(self.confs)

    def get_work_dir(self):
        self.workspace = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.txt_dir.setText(self.workspace)
        self.txt_dir.setCursorPosition(0)

    def addFunction(self):

        lbls = [QLabel('Return Type'), QLabel('Visibility'), QLabel('Function Name'), QLabel('Arguments')]

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

        self.functions_list.append(Function(self.functions, type, visibility, name, argv))

        self.functions.addWidget(lbls[0], 1, 0)
        self.functions.addWidget(lbls[1], 1, 1)
        self.functions.addWidget(lbls[2], 1, 4)
        self.functions.addWidget(lbls[3], 1, 18)


        self.functions.addWidget(type, 2 + self.num_of_funcs, 0)
        self.functions.addWidget(visibility, 2 + self.num_of_funcs, 1)
        self.functions.addWidget(name, 2 + self.num_of_funcs, 2, 1, 6)
        self.functions.addWidget(argv, 2 + self.num_of_funcs, 8, 1, 20)

        self.num_of_funcs += 1
        self.functions_box.setLayout(self.functions)


if __name__ == '__main__':

    app = QApplication([])
    interface = LibGenerator()
    interface.show()
    app.exec_()
