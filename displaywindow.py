from PyQt6.QtWidgets import(QWidget, QListWidgetItem, QListWidget, QVBoxLayout, QPushButton,QMessageBox )
from data import Db
class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Members")
        self.setGeometry(500,200,500,400)
        self.layout=QVBoxLayout(self)
        self.connect_buttons()
        self.db=Db()
        self.load_members()
    def show_message(self,title:str,message:str):
        QMessageBox.information(self,title,message)
    def connect_buttons(self):
        self.list=QListWidget(self)
        self.list.setStyleSheet("color:gray;font-size:22px")
        self.layout.addWidget(self.list)
        btnrem=QPushButton("Remove")
        self.layout.addWidget(btnrem)
        btnrem.clicked.connect(self.remove_button)
    def remove_button(self):
        #التحقق من وجود عناصر
        if self.list.count() > 0:
            row_index=self.list.currentRow()
            if row_index >= 0: # حدد عنصر
                item= self.list.item(row_index)
                id_item=item.data(256) 
                self.db.remove(id_item)
                self.list.takeItem(row_index) #حذف العنصر من القائمة
            else:
                self.show_message("info",'Please select an item.')
        else:
            self.show_message("info",'List is empty.')
    def load_members(self):
        for row in self.db.fetch():
            f_name=row[1]
            l_name=row[2]
            member_id=row[3]
            member_status=row[4]
            item= QListWidgetItem(f"Name: {f_name} {l_name}, ID: {member_id}, Status: {member_status}") # تغليف النص
            item.setData(256, row[0])
            self.list.addItem(item) #اضافة العنصر الي القائمة