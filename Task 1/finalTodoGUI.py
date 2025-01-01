"""TASK 1"""

# TO-DO List using GUI

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

class MyGUI(QMainWindow):
    
    task = [] #create a empty list first
    
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("Todo.ui", self)
        self.setWindowTitle("Todo Application")
        self.input.setPlaceholderText("Enter item to add or update the list...")

        #these are the pushbutton funcs

        self.addit.clicked.connect(self.addtodo)
        self.input.returnPressed.connect(self.addtodo)
        self.delit.clicked.connect(self.deltodo)
        self.updateit.clicked.connect(self.updatetodo)  

    #here add func will do the fetching work line_widget i.e my input

    def addtodo(self):
        text_insert = self.input.text()
        if text_insert.strip():
            self.task.append(text_insert)
            self.input.clear()
        self.refreshtodo()

    #here del func will do the deletion work display_widget 

    def deltodo(self):
        selected_item = self.displayit.currentItem()
        if selected_item:
            task_text = selected_item.text().split(". ", 1)[-1]
            if task_text in self.task:
                self.task.remove(task_text) 
        self.refreshtodo()  

    #NOTE:here what i've done is,the user have to select the particular task from the list to be updated
     
    def updatetodo(self):
        selected_item = self.displayit.currentItem()
        new_text = self.input.text()
        if selected_item and new_text.strip():
            current_index = self.displayit.row(selected_item)
            self.task[current_index] = new_text
            self.input.clear()
        self.refreshtodo()

    #its just a quick refresh func of the updated list

    def refreshtodo(self):
        self.displayit.clear()
        for i, task in enumerate(self.task, start=1):
            self.displayit.addItem(f"{i}. {task}")


def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show() 
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
