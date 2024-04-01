import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from login_form import Ui_login_form


class Login(QWidget, Ui_login_form):
    def __init__(self):
        super().__init__()

        # setup the UI
        self.setupUi(self)

        # authenticate when the login button is clicked
        self.btn_login.clicked.connect(self.authenticate)

        # show the login window
        self.show()

    def authenticate(self):
        email = self.email_line_edit.text()
        password = self.password_line_edit.text()

        if email == 'john@test.com' and password == '123456':
            QMessageBox.information(self, 'Success', "You're logged in!")
        else:
            QMessageBox.critical(self, 'Error', "Invalid email or password.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())