import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance


def get_maya_main_win():
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)


class TweeningToolWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__(parent=get_maya_main_win())
        #self.bookShelf = Bookshelf()
        self.setWindowTitle("Tweening Tool")
        self.resize(300, 200)
        self._mk_main_layout()

    def build_bookshelf(self):
        # Frame Options
        self.bookShelf.overall_height = self.shelf_height_dspnx.value()
        self.bookShelf.shelf_width = self.shelf_width_dspnx.value()
        self.bookShelf.shelf_depth = self.shelf_depth_dspnx.value()
        # Book Options
        self.bookShelf.shelf_levels = self.shelf_levels_spnx.value()
        self.bookShelf.books_offset = self.books_offset_dspnx.value()
        self.bookShelf.generate_bookshelf()

    def _mk_main_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self._mk_tween_slider_ui()
        self.setLayout(self.main_layout)

    def _mk_tween_slider_ui(self):
        self.slider = QtWidgets.QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.main_layout.addWidget(self.slider)
