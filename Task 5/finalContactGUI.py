"""TASK 5"""

# Contact Book using GUI

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

class Contact_book(QMainWindow):
   
    #here i've predifined few contacts 
   
    contact = {
        "Amit ": {"Phone": "9876543210", "Email": "amit@gmail.com", "Address": "New Delhi"},
        "Dhriti": {"Phone": "9123456789", "Email": "dhri@gmail.com", "Address": "Mumbai"},
        "Rahul ": {"Phone": "9876501234", "Email": "rahul78@gmail.com", "Address": "Bangalore"}
    }  
    
    def __init__(self):
        super(Contact_book, self).__init__()
        loadUi("contact.ui", self)
        self.setWindowTitle("Contacts")
        self.search.setPlaceholderText("Search contact")
        self.show()

        # Buttons:

        self.add_it.clicked.connect(self.add_contact)
        self.update_it.clicked.connect(self.update_contact)
        self.del_it.clicked.connect(self.delete_contact)
        self.search.textChanged.connect(self.search_contact)
        self.display.itemClicked.connect(self.display_contact)

        
        #NOTE:the .keys() func will fetch the keys and update the dict and when the app will open it will show in default nature
        self.display.addItems(self.contact.keys()) # to display predifined contact
        
    def add_contact(self):
        name = self.name_input.text().strip()
        phone = self.phn_input.text().strip()
        email = self.email_input.text().strip()
        address = self.add_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name cannot be empty!")
            return

        if name in self.contact:
            QMessageBox.warning(self, "Error", "Contact already exists!")
        
        else:
            self.contact[name] = {"Phone": phone, "Email": email, "Address": address} #name is the key for the nested dict
            self.display.addItem(name)  
            
            QMessageBox.information(self, "Success", "Contact added successfully!")
            
            self.clear_inputs()

   
    def update_contact(self):
        selected_item = self.display.currentItem()
        
        if not selected_item:
            QMessageBox.warning(self, "Error", "Select a contact to edit!")
            return

    
        old_name = selected_item.text()

        #fetch the new name from the i/p text
        new_name = self.name_input.text().strip()
        
        if not new_name:
            QMessageBox.warning(self, "Error", "Name cannot be empty!")
            return

        # now imp part to check for new and old name
        if old_name != new_name:  #if diffnt name then continue
            if new_name in self.contact:
                QMessageBox.warning(self, "Error", "Contact with this name already exists!")
                return
            
            #NOTE:here pop will execute 1st, then the cnct will be assingned to the new_name i.e now newname will replace the old key to new 
            self.contact[new_name] = self.contact.pop(old_name)
            selected_item.setText(new_name)  #update the item in the display
        
        # Updating other details 
        self.contact[new_name]["Phone"] = self.phn_input.text().strip()
        self.contact[new_name]["Email"] = self.email_input.text().strip()
        self.contact[new_name]["Address"] = self.add_input.text().strip()

        QMessageBox.information(self, "Success", "Contact updated successfully!")
        self.clear_inputs()



    def delete_contact(self):
        selected_item = self.display.currentItem()
        
        if not selected_item:
            QMessageBox.warning(self, "Error", "Select a contact to delete!")
            return

        name = selected_item.text()
        if QMessageBox.question(self, "Confirm Deletion", f"Delete contact '{name}'?", #here breaking is not so imp but for good look ive done that
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            del self.contact[name]
            self.display.takeItem(self.display.row(selected_item)) #here takeitem will fetch the item and row and will del it
            
            QMessageBox.information(self, "Success", f"Contact '{name}' deleted!")
            self.clear_inputs()

    def search_contact(self):
        search_text = self.search.text().strip().lower()
        self.display.clear()

       #checks the contct that are matched from the user_i/p
        for name in self.contact:
            if search_text in name.lower():
                self.display.addItem(name)

    #simply display the details when the name is selected
    def display_contact(self, item):
        name = item.text()
        if name in self.contact:
            self.name_input.setText(name)
            self.phn_input.setText(self.contact[name]["Phone"])
            self.email_input.setText(self.contact[name]["Email"])
            self.add_input.setText(self.contact[name]["Address"])

    def clear_inputs(self):
        self.name_input.clear()
        self.phn_input.clear()
        self.email_input.clear()
        self.add_input.clear()

def main():
    app = QApplication(sys.argv)
    window = Contact_book()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
