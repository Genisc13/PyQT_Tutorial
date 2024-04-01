import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QCompleter
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLineEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        common_fruits = QCompleter([
            'Apple',
            'Apricot',
            'Banana',
            'Carambola',
            'Olive',
            'Oranges',
            'Papaya',
            'Peach',
            'Pineapple',
            'Pomegranate',
            'Rambutan',
            'Ramphal',
            'Raspberries',
            'Rose apple',
            'Starfruit',
            'Strawberries',
            'Water apple',
        ])
        fruit = QLineEdit(self,
                          placeholderText='Enter some fruit to eat...')
        fruit.setCompleter(common_fruits)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(fruit)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())