import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance


def get_maya_main_win():
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)


class BookshelfWindow(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_maya_main_win())
        #self.bookShelf = Bookshelf()
        self.setWindowTitle("Bookshelf Generator")
        self.resize(300, 200)
        self._mk_main_layout()
        self._connect_signals()

    def _connect_signals(self):
        self.cancel_btn.clicked.connect(self.close)
        self.build_btn.clicked.connect(self.build_bookshelf)

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
        self.main_layout = QtWidgets.QVBoxLayout()
        self._mk_frame_options_ui()
        self._mk_book_options_ui()
        self._mk_buttons_layout()
        self.setLayout(self.main_layout)

    def _mk_frame_options_ui(self):
        # Shelf Height
        self.frame_options_layout = QtWidgets.QHBoxLayout()
        self.shelf_height_lbl = QtWidgets.QLabel("Shelf Height")
        self.shelf_height_dspnx = QtWidgets.QDoubleSpinBox()
        self.shelf_height_dspnx.setMinimumWidth(50)
        self.shelf_height_dspnx.setValue(2.0)
        self.shelf_height_dspnx.setSingleStep(0.1)
        self.frame_options_layout.addWidget(self.shelf_height_lbl)
        self.frame_options_layout.addWidget(self.shelf_height_dspnx)
        self.main_layout.addLayout(self.frame_options_layout)
        # Shelf Width
        self.shelf_width_lbl = QtWidgets.QLabel("Shelf Width")
        self.shelf_width_dspnx = QtWidgets.QDoubleSpinBox()
        self.shelf_width_dspnx.setMinimumWidth(50)
        self.shelf_width_dspnx.setValue(1.0)
        self.shelf_width_dspnx.setSingleStep(0.1)
        self.frame_options_layout.addWidget(self.shelf_width_lbl)
        self.frame_options_layout.addWidget(self.shelf_width_dspnx)
        self.main_layout.addLayout(self.frame_options_layout)
        # Shelf Depth
        self.shelf_depth_lbl = QtWidgets.QLabel("Shelf Depth")
        self.shelf_depth_dspnx = QtWidgets.QDoubleSpinBox()
        self.shelf_depth_dspnx.setMinimumWidth(50)
        self.shelf_depth_dspnx.setValue(0.3)
        self.shelf_depth_dspnx.setSingleStep(0.05)
        self.frame_options_layout.addWidget(self.shelf_depth_lbl)
        self.frame_options_layout.addWidget(self.shelf_depth_dspnx)
        self.main_layout.addLayout(self.frame_options_layout)

    def _mk_book_options_ui(self):
        # Shelf Levels
        self.book_options_layout = QtWidgets.QHBoxLayout()
        self.book_levels_lbl = QtWidgets.QLabel("Shelf Levels")
        self.shelf_levels_spnx = QtWidgets.QSpinBox()
        self.shelf_levels_spnx.setMinimumWidth(50)
        self.shelf_levels_spnx.setValue(6)
        self.book_options_layout.addWidget(self.book_levels_lbl)
        self.book_options_layout.addWidget(self.shelf_levels_spnx)
        self.main_layout.addLayout(self.book_options_layout)
        # Book Offset
        self.books_offset_lbl = QtWidgets.QLabel("Book Offset")
        self.books_offset_dspnx = QtWidgets.QDoubleSpinBox()
        self.books_offset_dspnx.setDecimals(4)
        self.books_offset_dspnx.setMinimumWidth(50)
        self.books_offset_dspnx.setValue(0)
        self.books_offset_dspnx.setSingleStep(0.0005)
        self.book_options_layout.addWidget(self.books_offset_lbl)
        self.book_options_layout.addWidget(self.books_offset_dspnx)
        self.main_layout.addLayout(self.book_options_layout)

    def _mk_buttons_layout(self):
        self.build_btn = QtWidgets.QPushButton("Build")
        self.main_layout.addWidget(self.build_btn)

        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.main_layout.addWidget(self.cancel_btn)
