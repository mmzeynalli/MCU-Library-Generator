from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog)

import sys
import os



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

        # Create first tab
        self.createFunctionsTab()
        # self.createDefinesTab

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.setGeometry(600, 600, 400, 50)
        self.setWindowTitle('MCU Library Generator v1.0')
        self.setStyle('Fusion')

    def setStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(QApplication.palette())

    def createFunctionsTab(self):

        self.tab1_layout = QGridLayout()
        self.tab1_layout.setSpacing(10)
        self.tab1_layout.setColumnStretch(1, 4)
        self.tab1_layout.setColumnStretch(2, 4)

        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        ####################################

        lbl_username = QLabel('Creators Full Name')
        txt_username = QLineEdit()

        ####################################

        lbl_dir = QLabel('Project Directory')

        bt_dir = QPushButton("...")
        bt_dir.setFixedSize(30, 20)

        txt_dir = QLineEdit()
        txt_dir.setText(os.path.dirname(os.path.realpath(__file__)))
        txt_dir.setCursorPosition(0)

        self.functions_box = QGroupBox('Functions')
        self.functions = QGridLayout()
        self.createFunction()
        self.createFunction()

        #txt_field_dir.setFixedWidth(100)

        lbl_file_name = QLabel('Module (Library) name: ')
        txt_file_name = QLineEdit()
        txt_file_name.setText('Hello')
        #txt_file_name.setFixedWidth(80)

        self.tab1_layout.addWidget(lbl_username, 0, 0)
        self.tab1_layout.addWidget(txt_username, 0, 1, 1, 20)
        self.tab1_layout.addWidget(lbl_dir, 1, 0)
        self.tab1_layout.addWidget(txt_dir, 1, 1, 1, 20)
        self.tab1_layout.addWidget(bt_dir, 1, 21)
        self.tab1_layout.addWidget(lbl_file_name, 2, 0)
        self.tab1_layout.addWidget(txt_file_name, 2, 1, 1, 20)
        #self.tab1_layout.addWidget(self.functions_box, 3, 0)

        self.tab1.setLayout(self.tab1_layout)


    def createFunction(self):

        type = QComboBox(self.functions_box)
        type.addItems(['void', 'int', 'char *', 'bool', 'uint8_t', 'Other'])

        visibility = QComboBox(self.functions_box)
        visibility.addItems(['private', 'public'])
        visibility.setFixedWidth(100)

        self.functions.addWidget(visibility, 4 + self.num_of_funcs, 0)
        self.functions.addWidget(type, 4 + self.num_of_funcs, 1)
        self.num_of_funcs += 1

        self.functions_box.setLayout(self.functions)


    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)


if __name__ == '__main__':

    app = QApplication([])
    interface = LibGenerator()
    interface.show()
    app.exec_()
