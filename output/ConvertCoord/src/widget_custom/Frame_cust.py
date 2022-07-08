from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

class Button_frame(QFrame):

    clicked = Signal()

    def __init__(self):
        # super(Button_frame, self).__init__(parent)
        QFrame.__init__(self)

    def mousePressEvent(self, event):
        self.clicked.emit()
