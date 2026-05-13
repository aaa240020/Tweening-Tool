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
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self._mk_tween_slider_ui()

    def _mk_tween_slider_ui(self):
        # Title
        self.title = QtWidgets.QLabel("Tweening Tool")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.title)
        # Slider
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(25)
        self.main_layout.addWidget(self.slider)
        # Intervals
        self.intervals = QtWidgets.QHBoxLayout()

        last = QtWidgets.QLabel("Last")
        last.setAlignment(QtCore.Qt.AlignLeft)
        last.setAlignment(QtCore.Qt.AlignTop)
        self.intervals.addWidget(last)

        fifty = QtWidgets.QLabel("50%")
        fifty.setAlignment(QtCore.Qt.AlignCenter)
        self.intervals.addWidget(fifty)

        next = QtWidgets.QLabel("Next")
        next.setAlignment(QtCore.Qt.AlignHCenter)
        next.setAlignment(QtCore.Qt.AlignRight)
        
        self.intervals.addWidget(next)

        self.main_layout.addLayout(self.intervals)

