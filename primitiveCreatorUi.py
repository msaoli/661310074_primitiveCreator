from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
from . import primitiveCreatorUtil

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))


class PrimitiveCreatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(500, 250)
        self.setWindowTitle('👾Primitive Creator👾')

        self.setStyleSheet("background-color: #040036;")


        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.primitive_listWidget = QtWidgets.QListWidget()
        self.primitive_listWidget.setIconSize(QtCore.QSize(80, 80))
        self.primitive_listWidget.setSpacing(22)
        self.primitive_listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
        self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

        self.main_layout.addWidget(self.primitive_listWidget)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.create_button = QtWidgets.QPushButton('🐲Create')
        self.cancel_button= QtWidgets.QPushButton('❌Cancel')
        self.button_layout.addStretch()

        self.button_layout.addWidget(self.create_button)
        self.create_button.setStyleSheet(
            '''
            QPushButton {
                font-family: 'Caveat';
                font-size: 20px;
                background-color: #B7B7EB;
                color: black;
                font-weight: bold;
                border-radius: 12px;
                border: 2px solid #000000;
            }
            '''
        )

        self.button_layout.addWidget(self.cancel_button)
        self.cancel_button.setStyleSheet(
            '''
            QPushButton {
                font-family: 'Caveat';
                font-size: 20px;
                background-color: #FF7AAB;
                color: white;
                font-weight: bold;
                border-radius: 12px;
                border: 2px solid #000000;
            }
            '''
        )

        self.create_button.setFixedSize(120, 50)
        self.cancel_button.setFixedSize(120, 50)

        self.button_layout.addStretch()

        self.create_button.clicked.connect(self.createObject)
        self.cancel_button.clicked.connect(self.close)

        self.initIconWidgets()
        #self.setWindowOpacity(0.8)


    def initIconWidgets(self):
        prims = ['cone', 'cube', 'sphere', 'torus']
        for prim in prims:
            item = QtWidgets.QListWidgetItem(prim)
            item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
            item.setForeground(QtGui.QBrush(QtGui.QColor("#AEABCC")))
            self.primitive_listWidget.addItem(item)

    def createObject(self):
        current_item = self.primitive_listWidget.currentItem()
        if not current_item:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select an object.")
            return

        prim_type = current_item.text()
        primitiveCreatorUtil.create_primitive(prim_type)


def run():
    global ui

    try:
        ui.close()
    except:
        pass
    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = PrimitiveCreatorDialog(parent=ptr)
    ui.show()
