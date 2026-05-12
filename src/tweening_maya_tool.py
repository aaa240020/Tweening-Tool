import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance


def get_maya_main_win():
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)


class TweeningToolWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_maya_main_win())
        self.setWindowTitle("Tweening Tool")
        self.resize(300, 200)
        self._mk_main_layout()

    def _mk_main_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self._mk_tween_slider_ui()

    def _mk_tween_slider_ui(self):
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.main_layout.addWidget(self.slider)


