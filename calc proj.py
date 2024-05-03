import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

     
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

       
        self.sum_button = QPushButton("Sum")
        self.multiplication_button = QPushButton("Multiplication")
        self.subtraction_button = QPushButton("Subtraction")
        self.division_button = QPushButton("Division")

       
        self.result_label = QLabel()

       
        self.sum_button.clicked.connect(self.calculate_sum)
        self.multiplication_button.clicked.connect(self.calculate_multiplication)
        self.subtraction_button.clicked.connect(self.calculate_subtraction)
        self.division_button.clicked.connect(self.calculate_division)

       
        self.layout.addWidget(self.input1)
        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.sum_button)
        self.layout.addWidget(self.multiplication_button)
        self.layout.addWidget(self.subtraction_button)
        self.layout.addWidget(self.division_button)
        self.layout.addWidget(self.result_label)

    def calculate_sum(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 + num2
            self.show_result(result)
        except ValueError:
            self.show_result("Error: Invalid input")

    def calculate_multiplication(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 * num2
            self.show_result(result)
        except ValueError:
            self.show_result("Error: Invalid input")

    def calculate_subtraction(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            result = num1 - num2
            self.show_result(result)
        except ValueError:
            self.show_result("Error: Invalid input")

    def calculate_division(self):
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            if num2 == 0:
                self.show_result("Error: Division by zero")
            else:
                result = num1 / num2
                self.show_result(result)
        except ValueError:
            self.show_result("Error: Invalid input")

    def show_result(self, result):
        self.result_label.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
