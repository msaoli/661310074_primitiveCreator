from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))


class PrimitiveCreatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(300, 300)
        self.setWindowTitle('PrimitiveCrator🍪')

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.primitive_listWidget = QtWidgets.QListWidget()
        self.primitive_listWidget.setIconSize(QtCore.QSize(40, 40))
        self.primitive_listWidget.setSpacing(5)
        self.primitive_listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
        self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

        self.main_layout.addWidget(self.primitive_listWidget)

        self.name_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.name_layout)

        self.name_label = QtWidgets.QLabel('Name:')
        self.name_lineEdit = QtWidgets.QLineEdit()
        self.name_lineEdit.setStyleSheet('background-color: white; color: #B7B7EB;font-family:Caveat')
        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name_lineEdit)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.create_button = QtWidgets.QPushButton('🐲Create')
        self.cancel_button= QtWidgets.QPushButton('❌Cancel')
        self.button_layout.addStretch()

        self.button_layout.addWidget(self.create_button)
        self.create_button.setStyleSheet(
            '''
            QPushButton {
                background-color: #B7B7EB;
            }
            '''
        )

        self.button_layout.addWidget(self.cancel_button)

        self.initIconWidgets()
        self.setWindowOpacity(0.8)

    def initIconWidgets(self):
        prims = ['cone', 'cube', 'sphere', 'torus']
        for prim in prims:
            item = QtWidgets.QListWidgetItem(prim)
            item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
            self.primitive_listWidget.addItem(item)

def run():
    global ui

    try:
        ui.close()
    except:
        pass
    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = PrimitiveCreatorDialog(parent=ptr)
    ui.show()

