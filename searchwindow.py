from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic, QtGui,QtCore
from data import Db
class SearchWidow(QWidget):
    def __init__(self):
        super().__init__()
        UI_PATH= 'searchwindow.ui'
        uic.loadUi(UI_PATH,self) #تحميل ملف الواجهه
        self.db=Db()
        self.setup_widgets()
    def show_message(self,title:str,message:str):
        QMessageBox.information(self,title,message)
    def setup_widgets(self):
        self.rbtn1.toggled.connect(self.radio_selected)
        self.rbtn2.toggled.connect(self.radio_selected)
        self.rbtn3.toggled.connect(self.radio_selected)
        self.searchbutton.clicked.connect(self.search_button)
    def radio_selected(self,checked):
        if checked: # True or Flase
            self.lineEdit.clear() # حذف المدخلات
            sender= self.sender()  # الزر ال ارسل الاشارة
            self.searchbutton.setDescription(f'By {sender.text()}')
            self.lineEdit.setPlaceholderText(f'Type the {sender.text()}')
            self.lineEdit.setFocus() #عمل تركيز ع الخانة
            if sender.text() == "Member ID":
                validator=QtGui.QIntValidator()  # جعل المدخل رقم فقط
            else:
                regex = QtCore.QRegularExpression("^[a-zA-Z\s]+$")  # حروف ومسافات
                validator = QtGui.QRegularExpressionValidator(regex)
            self.lineEdit.setValidator(validator)
    def search_button(self):
        """
        general search function
        """
        self.listWidget.clear() # لتجنب عدم تكرار البحث
        mode=self.get_search_mode()
        text= self.lineEdit.text().strip().lower()
        text=text.replace(' ','')
        # التحقق من اختيار مود البحث والنص
        if not mode:
            return self.show_message('Warning', 'Please select a search method.')
        elif not text:
             return self.show_message('Warning', 'Please type a search value.')
        else:
            results=self.search_fun(mode,text)
            if results: 
                self.display_results(results)
            else:
                self.show_message('Info', 'This member is not found')
    def search_fun(self,mode,value):
        result=[]
        for row in self.db.fetch():
            if mode =='name': # بحث بالاسم
                full_name= f'{row[1]}{row[2]}'
                if value in full_name.lower():
                    result.append(row)
            elif mode =='member id':
                member_id=row[3]
                if value == member_id:
                    result.append(row)  
            else:
                member_status=row[4]
                if value == member_status.lower():
                    result.append(row)
        return result                
    def get_search_mode(self):
        if self.rbtn1.isChecked():
            return 'name'
        elif self.rbtn2.isChecked():
            return 'member id'
        elif self.rbtn3.isChecked():
            return 'status'
        return None
    def display_results(self,results):
         for row in results:
            self.listWidget.addItem(f"Name: {row[1]} {row[2]}, ID: {row[3]}, Status: {row[4]}")
