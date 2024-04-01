import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # create a checkbox
        checkbox = QCheckBox('I agree', self)
        checkbox.stateChanged.connect(self.on_checkbox_changed)

        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

        # show the window
        self.show()

    def on_checkbox_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())