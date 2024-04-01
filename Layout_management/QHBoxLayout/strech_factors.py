import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        # create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        # create buttons and add them to the layout
        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        # set the stretch factors
        layout.setStretchFactor(buttons[0], 2)
        layout.setStretchFactor(buttons[1], 2)
        layout.setStretchFactor(buttons[2], 1)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
