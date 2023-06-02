# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QVBoxLayout, QLabel, QDialog
from ui import Ui_MainWindow
from PySide6.QtGui import QValidator, QRegularExpressionValidator
from PySide6.QtCore import Qt, QThread, Signal, Slot

import sys
import socket
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_ip_addr.setFocus()
        self.ui.com_result.setText("유효성 검사를 실시하세요.")

        self.ui.input_ip_addr.textChanged.connect(self.check_input_info)
        self.ui.input_port.textChanged.connect(self.check_input_info)

        self.ui.exit_btn.clicked.connect(self.confirm_exit)

        self.ui.com_check.clicked.connect(lambda : self.connection_test(self.ui.input_ip_addr.text(), int(self.ui.input_port.text())))
        

    # 유효성 검사를 통해 조건이 충족하는 경우에만 연결 유효성 검사 버튼 활성화
    def check_input_info(self) :
        isValid = 0

        regex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(regex)
        self.ui.input_ip_addr.setValidator(validator)
        
        state, _, _ = validator.validate(self.ui.input_ip_addr.text(), 0)

        if state == QRegularExpressionValidator.Acceptable :
            isValid = 1
        else :
            isValid = 0

        if self.ui.input_port.text() and isValid and int(self.ui.input_port.text()) < 65536 :
            self.ui.com_check.setEnabled(True)
        else :
            self.ui.com_check.setEnabled(False)

    # 종료 기능 구현 (종료 버튼을 눌렀을 때 확인창을 띄운 후 종료 결정)
    def confirm_exit(self) :
        reply = QMessageBox.question(self, "프로그램 종료", "프로그램을 정말 종료하시겠습니까?")
        if reply == QMessageBox.Yes :
            QApplication.quit()

    # 소켓 통신 테스트를 통해 유효성 검사 실시
    def connection_test(self, ip, port) :
        self.ui.com_result.setStyleSheet("color : blue; font-weight : bold;")
        self.ui.com_result.setText("유효성 검사 진행 중 ...")

        try :
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))

            self.ui.com_result.setStyleSheet("color : green; font-weight : bold;")
            self.ui.com_result.setWordWrap(True)
            self.ui.com_result.setText("소켓 통신 성공")
            self.ui.run_btn.setEnabled(True)

        except Exception as e :
            self.ui.com_result.setStyleSheet("color : red; font-weight : bold;")
            self.ui.com_result.setWordWrap(True)
            self.ui.com_result.setText(f"소켓 통신 실패\n({str(e)})")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()

    widget.show()

    sys.exit(app.exec())
