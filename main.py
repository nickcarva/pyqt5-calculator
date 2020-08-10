import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(
            QPushButton('+'), 1, 3, 1, 1,
            'background: #555; color: #FFF; font-weight: 300;'
        )
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            'background: #28f21d; font-weight: 700;',
            lambda: self.display.setText('')
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(
            QPushButton('-'), 2, 3, 1, 1,
            'background: #555; color: #FFF; font-weight: 300;'
        )
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            'background: #f52a45; font-weight: 700;',
            lambda: self.display.setText(
                self.display.text()[:-1]
            )
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(
            QPushButton('/'), 3, 3, 1, 1,
            'background: #555; color: #FFF; font-weight: 300;'
        )
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(
            QPushButton('*'), 4, 3, 1, 1,
            'background: #555; color: #FFF; font-weight: 300;'
        )
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            'background: #3fb6f2; font-weight: 700;',
            self.eval_response
        )

        self.setCentralWidget(self.cw)

    def add_btn(
        self, btn, row, col, rowspan, colspan,
        style=None, action=None
    ):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not action:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(action)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )

    def eval_response(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
