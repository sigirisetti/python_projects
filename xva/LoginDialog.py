import sys

import requests
import json

from PyQt5.QtWidgets import (QPushButton, QLineEdit, QApplication, QGridLayout, QLabel, QDialog)
from constants import *


class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.msg_lbl = QLabel("Please login")
        self.password.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton('Login', self)
        self.login_btn.clicked.connect(self.authenticate)
        self.cancel_btn = QPushButton('Cancel', self)
        self.cancel_btn.clicked.connect(self.cancel)
        self.token = None
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.username.setText(OV_USER)
        self.password.setText(OV_PASS)
        grid.addWidget(self.msg_lbl, 1, 1)
        grid.addWidget(QLabel("Username"), 2, 1)
        grid.addWidget(self.username, 2, 2)
        grid.addWidget(QLabel("Password"), 3, 1)
        grid.addWidget(self.password, 3, 2)
        grid.addWidget(self.login_btn, 4, 1)
        grid.addWidget(self.cancel_btn, 4, 2)
        self.setWindowTitle('Login dialog')

    def authenticate(self):
        response = requests.post(LOGIN_URL, json={"loginName": self.username.text(), "password": self.password.text()})
        data = json.loads(response.text)
        if not data['error']:
            self.token = data['token']
            self.close()
        else:
            self.msg_lbl.setText(data['errorMsg'])
            self.msg_lbl.setStyleSheet("QLabel { color : red; }")

    def get_token(self):
        return self.token

    def cancel(self):
        self.close()

    def exec_(self):
        self.msg_lbl.setText("")
        self.msg_lbl.setStyleSheet("")
        super(LoginDialog, self).exec_()
        return self.token


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginDialog()
    sys.exit(app.exec_())