import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

app = QApplication(sys.argv)

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_irst = QHBoxLayout()
        self.first = QHBoxLayout()
        self.second = QHBoxLayout()
        self.third = QHBoxLayout()
        self.forth = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_irst)
        self.vbox.addLayout(self.first)
        self.vbox.addLayout(self.second)
        self.vbox.addLayout(self.third)
        self.vbox.addLayout(self.forth)


        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.third.addWidget(self.b_9)

        self.b_dot = QPushButton(".", self)
        self.forth.addWidget(self.b_dot)

        self.b_0 = QPushButton("0", self)
        self.forth.addWidget(self.b_0)

        self.b_result = QPushButton("=", self)
        self.forth.addWidget(self.b_result)

        self.b_plus = QPushButton("+", self)
        self.hbox_irst.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_irst.addWidget(self.b_minus)

        self.b_proizvedenie = QPushButton("X", self)
        self.hbox_irst.addWidget(self.b_proizvedenie)

        self.b_delit = QPushButton(":", self)
        self.hbox_irst.addWidget(self.b_delit)


        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_proizvedenie.clicked.connect(lambda: self._operation("*"))
        self.b_delit.clicked.connect(lambda: self._operation("/"))
        self.b_dot.clicked.connect(lambda: self._button("."))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
        except Exception as E:
            print(E)
            self.input.setText("Введите первое число")

    def _result(self):
        try:
            self.num_2 = float(self.input.text())
            try:
                if self.op == "+":
                    self.input.setText(str(self.num_1 + self.num_2))
                if self.op == "-":
                    self.input.setText(str(self.num_1 - self.num_2))
                if self.op == "*":
                    self.input.setText(str(self.num_1 * self.num_2))
                if self.op == "/":
                    try:
                        self.input.setText(str(self.num_1 / self.num_2))
                    except Exception as E:
                        print(E)
                        self.input.setText("Результат не определен")
            except Exception as E:
                print(E)
                self.input.setText("Результат не определен")
        except Exception as E:
            print(E)
            self.input.setText("Результат не определен")


win = Calculator()
win.show()
sys.exit(app.exec_())