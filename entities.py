from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog)


class Entry():
    def __init__(self, wscope, wname):
        self.widget_scope = wscope
        self.widget_name = wname

    def get_data(self):
        pass


class Function():
    def __init__(self, layout, wtype, wscope, wfield, wargv):

        self.layout = layout
        self.widget_type = wtype
        self.widget_scope = wscope
        self.widget_name = wfield
        self.widget_argv = wargv

        #self.widget_argc = wargc
        #self.widget_argc.valueChanged.connect(self.change_args)
        self.last_widget = None

        self.type = ''
        self.scope = ''
        self.name = ''
        self.argc = 0
        self.argv = '(hello)'

    def get_data(self):
        self.type = self.widget_type.currentText()
        self.scope = self.widget_scope.currentText()
        self.name = self.widget_name.text()

        self.argv = self.widget_argv.text()
        if self.argv.startswith('('):
            self.argv = self.argv[1:]

        if self.argv.endswith(')'):
            self.argv = self.argv[:-1]

    # improve later
    def change_args(self):

        '''
        if self.argc < self.widget_argc.value():  # argument increase

            self.vars_layout.addWidget(var_type, self.x, self.y)
            self.vars_layout.addWidget(var_name, self.x, self.y + 1, 1, 10)
            self.x, self.y = (self.y + 11) // 22, (self.y + 11) % 22

            self.vars_group.setLayout(self.vars_layout)
            self.layout.addWidget(self.vars_group)

            print('Argument increased')

        else:  # argument decrease
            print('Argument decreased')

        '''
        #self.argc = self.widget_argc.value()  #update variable
        vars_group = QGroupBox('Variables')
        vars_layout = QGridLayout()

        if self.last_widget is not None:
            self.layout.removeWidget(self.last_widget)

        for j in range(0, (self.argc // 4) + 1):
            for i in range(0, (self.argc % 4) + 1, 2):
                var_type = QComboBox(vars_group)
                var_type.addItems(['int', 'char *', 'bool', 'uint8_t'])
                var_name = QLineEdit(vars_group)

                vars_layout.addWidget(var_type, i, j)
                vars_layout.addWidget(var_name, i, j + 1)

        vars_group.setLayout(vars_layout)
        self.layout.addWidget(vars_group)
        self.last_widget = vars_group

    def __str__(self):
        return 'Type: ' + self.type + ', Scope: ' + self.scope + ', Name: ' + self.name + ', argv: ' + self.argv


class Variable():
    def __init__(self, wscope, wtype, wname, wval = None):
        self.widget_scope = wscope
        self.widget_type = wtype
        self.widget_name = wname
        self.widget_val = wval

        self.scope = ''
        self.type = ''
        self.name = ''
        self.val = 0

    def get_data(self):
        self.scope = self.widget_scope.currentText()
        self.type = self.widget_type.currentText()
        self.name = self.widget_name.text()
        self.val = self.widget_val.value()


class Macro():
    def __init__(self, wscope, wname, wval=None):
        self.widget_scope = wscope
        self.widget_name = wname
        self.widget_val = wval

        self.scope = ''
        self.name = ''
        self.val = ''

    def get_data(self):
        self.scope = self.widget_scope.currentText()
        self.name = self.widget_name.text()
        self.val = self.widget_val.text()


class Configuration():
    def __init__(self, wauthor, wdir, wlibname):
        self.widget_author = wauthor
        self.widget_dir = wdir
        self.widget_module = wlibname

        self.author = ''
        self.work_dir = ''
        self.module_name = ''

    def get_data(self):
        self.author = self.widget_author.text()
        self.work_dir = self.widget_dir.text()
        self.module_name = self.widget_module.text()

        if self.module_name.endswith('.c') or self.module_name.endswith('.h'):
            self.module_name = self.module_name[:-2]