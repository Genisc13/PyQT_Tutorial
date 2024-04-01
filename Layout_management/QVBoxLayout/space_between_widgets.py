import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QVBoxLayout')

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create buttons
        find_next_btn = QPushButton('Find Next')
        find_all_btn = QPushButton('Find All')
        close_btn = QPushButton('Find All')

        # add the first & second buttons to the layout
        layout.addWidget(find_next_btn)
        layout.addWidget(find_all_btn)

        # add a spacer
        layout.addStretch()

        # add the third button
        layout.addWidget(close_btn)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

