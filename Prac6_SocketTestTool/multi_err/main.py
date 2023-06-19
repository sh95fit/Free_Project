# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QVBoxLayout, QLabel, QDialog, QSystemTrayIcon, QMenu
from ui import Ui_MainWindow
from PySide6.QtGui import QValidator, QRegularExpressionValidator, QIcon, QPixmap
from PySide6.QtCore import Qt, QThread, Signal, Slot, QTimer
from data_packet import send_data

import sys, os
import socket
import time

# 단일 파일로 작성 시 pyinstaller 코드
# pyinstaller --onefile --add-data "main_favicon.ico;." --icon="main_favicon.ico" --name="RTU_Socket_Client" main.py

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "main_favicon.ico")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_ip_addr.setFocus()
        self.ui.com_result.setText("유효성 검사를 실시하세요.")
        self.radio_buttons = {1:self.ui.select_modem.checkedButton().text(), 2:self.ui.select_type.checkedButton().text(), 3:self.ui.select_mppt.checkedButton().text(), 4:self.ui.select_err.checkedButton().text(), 5:self.ui.select_com.checkedButton().text(), 6:self.ui.select_count.checkedButton().text()}

        for i in range(0,16) :
            self.ui.err_level.addItem(f"{i:02}")

        for i in range(1,17) :
            self.ui.device_num.addItem(f"{i:02}")

        self.count_status = 1

        self.ui.err_level.setCurrentIndex(0)
        self.ui.device_num.setCurrentIndex(0)

        self.run_status = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.do_work)

        self.tray_icon = QSystemTrayIcon(QIcon(image_path), self)
        self.tray_icon.setToolTip("RTU Socket Client")
        self.tray_icon.activated.connect(self.tray_icon_activated)
        self.tray_icon.show()

        self.ui.select_modem.buttonToggled.connect(lambda : self.radio_btn_handler(1, self.ui.select_modem.checkedButton().text()))
        self.ui.select_type.buttonToggled.connect(lambda : self.radio_btn_handler(2, self.ui.select_type.checkedButton().text()))
        self.ui.select_mppt.buttonToggled.connect(lambda : self.radio_btn_handler(3, self.ui.select_mppt.checkedButton().text()))
        self.ui.select_err.buttonToggled.connect(lambda : self.radio_btn_handler(4, self.ui.select_err.checkedButton().text()))
        self.ui.select_com.buttonToggled.connect(lambda : self.radio_btn_handler(5, self.ui.select_com.checkedButton().text()))
        self.ui.select_count.buttonToggled.connect(lambda : self.radio_btn_handler(6, self.ui.select_count.checkedButton().text()))

        self.ui.input_ip_addr.textChanged.connect(self.check_input_info)
        self.ui.input_port.textChanged.connect(self.check_input_info)

        # 스레드 중지 및 종료 처리
        self.ui.exit_btn.clicked.connect(self.confirm_exit)

        self.ui.com_check.clicked.connect(lambda : self.connection_test(self.ui.input_ip_addr.text(), int(self.ui.input_port.text())))

        self.ui.err_level.currentIndexChanged.connect(self.err_level_handler)

        self.ui.run_btn.clicked.connect(self.start_thread)

        # 스레드 관련
        # self.worker_thread = WorkerThread()
        # self.worker_thread.finished.connect(self.on_thread_finished)


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
    @Slot()
    def confirm_exit(self) :
        # if self.worker_thread.isRunning():
        #     self.run_status = 0

        self.ui.com_result.setStyleSheet("font-weight : bold;")
        self.ui.com_result.setWordWrap(True)
        self.ui.com_result.setText("프로그램 중지")

            # self.worker_thread.requestInterruption()
            # self.ui.run_btn.setEnabled(True)
            # self.worker_thread.finished.connect(self.close)
        # else:
            # self.close()
            # pass

        self.ui.run_btn.setEnabled(True)
        self.ui.com_check.setEnabled(True)
        self.timer.stop()

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

    def radio_btn_handler(self, key, new_value):
        # 선택된 라디오 버튼을 확인하고 해당 라디오 버튼의 인덱스 출력
        if key in self.radio_buttons :
            self.radio_buttons[key] = new_value
            if self.radio_buttons[4] == "에러 적용" :
                self.ui.err_level.setEnabled(True)
            else :
                self.ui.err_level.setEnabled(False)
            if self.radio_buttons[6] == "멀티" :
                self.ui.device_num.setEnabled(True)
            else :
                self.ui.device_num.setEnabled(False)
            # print(self.radio_buttons)
        else :
            pass

    def err_level_handler(self) :
        self.select_err = self.ui.err_level.currentText()


    # 비동기 처리를 위한 스레드 처리 관련 함수
    # def exit_program(self):
    #     self.worker_thread.requestInterruption()

    # def on_thread_finished(self):
    #     QApplication.quit()


    @Slot()
    def start_thread(self):
        self.run_status = 1
        self.count_status = 1

        self.ui.com_result.setStyleSheet("color : green; font-weight : bold;")
        self.ui.com_result.setWordWrap(True)
        self.ui.com_result.setText(f"| 모뎀: {self.radio_buttons[1]} | 상 구분: {self.radio_buttons[2]} | MPPT: {self.radio_buttons[3]} | 에러 상태: {self.radio_buttons[4]}({self.ui.err_level.currentText()}) | 통신 상태: {self.radio_buttons[5]} |\n장비 대수 : {self.radio_buttons[6]}({int(self.ui.device_num.currentText())}대)\n프로그램 정상 실행 중...")


        # 실행 시 최소화
        # self.showMinimized()
        # 숨김 처리
        # self.hide()

        self.initial_execution()

        self.ui.run_btn.setEnabled(False)
        self.ui.com_check.setEnabled(False)
        # self.worker_thread.start()

        self.timer.start(60000)

    # @Slot()
    # def on_thread_finished(self):
    #     self.ui.run_btn.setEnabled(True)


    # Timer로 비동기 적용
    def do_work(self):
        # 주기적으로 실행할 작업을 수행
        if self.radio_buttons[6] == "단일" :
            send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
        else :
            if self.count_status <= int(self.ui.device_num.currentText()) :
                send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
                self.count_status += 1
            else :
                self.count_status = 1
                send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
                self.count_status += 1


        # send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5])
        # print("주기적인 작업 실행...")


    def initial_execution(self):
        if self.radio_buttons[6] == "단일" :
            send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
        else :
            if self.count_status <= int(self.ui.device_num.currentText()) :
                send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
                self.count_status += 1
            else :
                self.count_status = 1
                send_data(self.ui.input_ip_addr.text(), self.ui.input_port.text(), self.radio_buttons[1], self.radio_buttons[2], self.radio_buttons[3], self.ui.err_level.currentText(), self.radio_buttons[5], self.count_status)
                self.count_status += 1

        # print("최초 작업 실행...")

# 비동기 형태로 작업 수행
# class WorkerThread(QThread):
#     finished = Signal()

#     def run(self):
#         while not self.isInterruptionRequested():
#             # 여기에 1분마다 수행할 작업을 추가
#             print("작업 실행 중...")
#             time.sleep(60)
#         self.finished.emit()

    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger :
            self.showNormal()


    def closeEvent(self, event) :
        if self.run_status == 1 :
            event.ignore()
            self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)


    widget = MainWindow()

    # widget.setWindowIcon(QIcon("C:/Users/user/Desktop/KIMSEHUN/develop/Free_Project/Prac6_SocketTestTool/main_favicon.ico"))
    # widget.setWindowIcon(QIcon("C:\\Users\\user\\Desktop\\KIMSEHUN\\develop\\Free_Project\\Prac6_SocketTestTool\\main_favicon.ico"))
    widget.setWindowIcon(QIcon(image_path))

    widget.show()

    sys.exit(app.exec())
