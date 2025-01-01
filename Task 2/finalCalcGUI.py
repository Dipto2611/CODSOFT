"""TASK 2"""

# Simple Calculator using GUI

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class CalculatorApp(QMainWindow):
    #make them empty first
    curnt_exp = ""
    final_res = ""

    def __init__(self):
        super(CalculatorApp, self).__init__()
        loadUi("updatedcal.ui", self)
        self.setWindowTitle("Calculator")
        self.input.setPlaceholderText("Enter current expression")
        self.show()

        #button property:
        
        #NOTE: here "data" will fetch the particular val from the btn like "0"

        self.btn_0.setProperty("data", "0") 
        self.btn_1.setProperty("data", "1")
        self.btn_2.setProperty("data", "2")
        self.btn_3.setProperty("data", "3")
        self.btn_4.setProperty("data", "4")
        self.btn_5.setProperty("data", "5")
        self.btn_6.setProperty("data", "6")
        self.btn_7.setProperty("data", "7")
        self.btn_8.setProperty("data", "8")
        self.btn_9.setProperty("data", "9")
        self.btn_divide.setProperty("data", "/")
        self.btn_equal.setProperty("data", "=")
        self.btn_minus.setProperty("data", "-")
        self.btn_multiply.setProperty("data", "*")
        self.btn_plus.setProperty("data", "+")
     

        #button connection:

        self.btn_0.clicked.connect(self.btn_pressed)
        self.btn_1.clicked.connect(self.btn_pressed)
        self.btn_2.clicked.connect(self.btn_pressed)
        self.btn_3.clicked.connect(self.btn_pressed)
        self.btn_4.clicked.connect(self.btn_pressed)
        self.btn_5.clicked.connect(self.btn_pressed)
        self.btn_6.clicked.connect(self.btn_pressed)
        self.btn_7.clicked.connect(self.btn_pressed)
        self.btn_8.clicked.connect(self.btn_pressed)
        self.btn_9.clicked.connect(self.btn_pressed)
        self.btn_divide.clicked.connect(self.btn_pressed)
        self.btn_equal.clicked.connect(self.calc_result)
        self.btn_minus.clicked.connect(self.btn_pressed)
        self.btn_multiply.clicked.connect(self.btn_pressed)
        self.btn_plus.clicked.connect(self.btn_pressed)
        self.btn_clear.clicked.connect(self.clr_all)
        #self.input.returnPressed.connect(self.calc_result)

    #NOTE:here what we have to do is to simply fetch the value from the I/P box with addtion to symbols and all

    def btn_pressed(self):
        trigger = self.sender() #its and inbuilt func (it identifies which button was clicked) 
        self.curnt_exp = self.input.text().strip()
        self.curnt_exp = self.curnt_exp + trigger.property("data") #{fetches the value stored in the btn data property}
        self.input.setText(self.curnt_exp) #setText is used for the updation of our exp (like 7 then + then 3 like this....) {simple dipslay}

    #NOTE:now evaluate the res and display it in display_widget
    
    def calc_result(self):
        self.final_res = self.input.text().strip()
        if self.final_res:
            try:
                result = eval(self.final_res)
                self.output.setText(str(result))
            except (ValueError, ZeroDivisionError, TypeError):
                self.output.setText("Error")

    #clear the whole screen

    def clr_all(self):
        self.final_res = ""
        self.curnt_exp = ""
        self.input.clear()
        self.output.clear()



def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()





