import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance


def get_maya_main_win():
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)


def tweening(percentage):
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Object not selected. Select an Object.")
    else:
        pass

    current_time = cmds.currectTime(query=True)
    # Previous and Next Frames
    for object in selection:
        keyed_frames = cmds.listAnimatible(object)
        for key in keyed_frames:
            key_frames = cmds.keyframe(key, query=True, timeChange=True)
            if not key_frames:
                return None, None
            
            before_frames = []
            after_frames = []

            for time in key_frames:
                if time < current_time:
                    before_frames.append(time)

            for time in key_frames:
                if time > current_time:
                    after_frames.append(time)
            
            if len(before_frames) > 0:
                previous_frame = before_frames[0]
                for time in before_frames:
                    if time > previous_frame:
                        previous_frame = time
            else:
                previous_frame = None

            if len(after_frames) > 0:
                next_frame = after_frames[0]
                for time in after_frames:
                    if time > next_frame:
                        next_frame = time
            else:
                next_frame = None


class TweeningToolWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_maya_main_win())
        self.setWindowTitle("Tweening Tool")
        self.resize(300, 200)
        self.setMaximumHeight(100)
        self.setMinimumWidth(300)
        self._mk_main_layout()
        self._connect_signals()

    def _mk_main_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
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
        # Reset to 50%
        self.reset = QtWidgets.QPushButton("Reset")
        self.main_layout.addWidget(self.reset)

    def _connect_signals(self):
        self.reset.clicked.connect(self._reset_to_50)

    def _reset_to_50(self):
        self.slider.setValue(50)
