import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
   def __init__(self):
         super(Calculator, self).__init__()

         self.vbox = QVBoxLayout(self)#оси выравнивания
         self.hbox_input = QHBoxLayout()
         self.hbox_first = QHBoxLayout()
         self.hbox_second = QHBoxLayout()
         self.hbox_third = QHBoxLayout()
         self.hbox_fourth = QHBoxLayout()
         self.hbox_result = QHBoxLayout()

         self.vbox.addLayout(self.hbox_input)
         self.vbox.addLayout(self.hbox_first)
         self.vbox.addLayout(self.hbox_second)
         self.vbox.addLayout(self.hbox_third)
         self.vbox.addLayout(self.hbox_fourth)
         self.vbox.addLayout(self.hbox_result)

         self.input = QLineEdit(self)# создаю виджеты и привязываю их к соответствующим осям выравнивания
         self.hbox_input.addWidget(self.input)

         self.b_1 = QPushButton("1", self)
         self.hbox_first.addWidget(self.b_1)

         self.b_2 = QPushButton("2", self)
         self.hbox_first.addWidget(self.b_2)

         self.b_3 = QPushButton("3", self)
         self.hbox_first.addWidget(self.b_3)#

         self.b_4 = QPushButton("4", self)
         self.hbox_second.addWidget(self.b_4)

         self.b_5 = QPushButton("5", self)
         self.hbox_second.addWidget(self.b_5)

         self.b_6 = QPushButton("6", self)
         self.hbox_second.addWidget(self.b_6)

         self.b_7 = QPushButton("7", self)
         self.hbox_third.addWidget(self.b_7)

         self.b_8 = QPushButton("8", self)
         self.hbox_third.addWidget(self.b_8)

         self.b_9 = QPushButton("9", self)
         self.hbox_third.addWidget(self.b_9)

         self.b_point = QPushButton(".", self)
         self.hbox_fourth.addWidget(self.b_point)

         self.b_0 = QPushButton("0", self)
         self.hbox_fourth.addWidget(self.b_0)

         self.b_clear = QPushButton("C", self)
         self.hbox_fourth.addWidget(self.b_clear)

         self.b_plus = QPushButton("+", self)
         self.hbox_first.addWidget(self.b_plus)

         self.b_minus = QPushButton("-", self)
         self.hbox_second.addWidget(self.b_minus)

         self.b_multiply = QPushButton("×", self)
         self.hbox_third.addWidget(self.b_multiply)

         self.b_devided = QPushButton("÷", self)
         self.hbox_fourth.addWidget(self.b_devided)

         self.b_delete = QPushButton("<<", self)
         self.hbox_result.addWidget(self.b_delete)

         self.b_result = QPushButton("=", self)
         self.hbox_result.addWidget(self.b_result)

         self.b_plus.clicked.connect(lambda: self._operation("+"))# события, отвечающие за реакции на нажатия по кнопкам
         self.b_minus.clicked.connect(lambda: self._operation("-"))
         self.b_multiply.clicked.connect(lambda: self._operation("*"))
         self.b_devided.clicked.connect(lambda: self._operation("/"))

         self.b_result.clicked.connect(self._result)
         self.b_clear.clicked.connect(self._clear)
         self.b_delete.clicked.connect(self._delete)

         self.b_1.clicked.connect(lambda: self._button("1")) #В connect функцию нельзя передавать аргументы. Для решения этой проблемы используем lambda-функции
         self.b_2.clicked.connect(lambda: self._button("2"))
         self.b_3.clicked.connect(lambda: self._button("3"))
         self.b_4.clicked.connect(lambda: self._button("4"))
         self.b_5.clicked.connect(lambda: self._button("5"))
         self.b_6.clicked.connect(lambda: self._button("6"))
         self.b_7.clicked.connect(lambda: self._button("7"))
         self.b_8.clicked.connect(lambda: self._button("8"))
         self.b_9.clicked.connect(lambda: self._button("9"))
         self.b_0.clicked.connect(lambda: self._button("0"))
         self.b_point.clicked.connect(lambda: self._button("."))

         self.b_result.setEnabled(False)

   def _button(self, param): #для обработки кнопок, отвечающих за ввод цифр в линию ввода текста
         line = self.input.text()
         self.input.setText(line + param)

   def _operation(self, op):
         self.b_result.setEnabled(True)
         self.num_1 = str(self.input.text())
         if self.num_1 == '':
             self.num_1 = '0'
         self.op = op
         print(op)
         self.input.setText("")

   def _clear(self):
         self.input.setText('')

   def _delete(self):
         self.input.setText(str(self.input.text()[:-1]))

   def _result(self):
         self.num2=float(self.input.text())
         if (self.input.text().count('.') > 1) or (self.num_1.count('.') > 1):
             self.input.setText('Невозможное значение! Нажмите (С), чтобы продолжить.')
         elif self.num_1 == '0' and self.op == '' and self.input.text() == '':
             self.input.setText('1111111')
         else:
             self.num_2 = ''
             if self.input.text() == '':
                 self.num_2 = float('0')
             else:
                 self.num_2 = float(self.input.text())
             if self.op == "+":
                 #print(self.num_1)
                 self.input.setText(str(float(self.num_1) + self.num_2))
             if self.op == "-":
                 self.input.setText(str(float(self.num_1) - self.num_2))
             if self.op == "*":
                 self.input.setText(str(float(self.num_1) * self.num_2))
             if self.op == "/":
                 if int(self.num_2) == 0:
                     self.input.setText('ЧЕЛ, ТЫ ЧЕГО) На ноль делить нельзя!')
                 else:
                     self.input.setText(str(float(self.num_1) / self.num_2))

app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())