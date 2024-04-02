import sys

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Media')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('window', window)
    engine.load('media.qml')
    sys.exit(app.exec())
