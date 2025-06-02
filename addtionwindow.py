from PyQt6 import QtWidgets, QtGui
from data import Db
class AddWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db=Db()
        self.setGeometry(500, 200, 300, 150)
        #انشاء التخطيط
        self.layout=QtWidgets.QFormLayout(self)
        self.connect_buttons()
    def connect_buttons(self):
        #انشاء الحقول
        self.first_name_input=QtWidgets.QLineEdit()
        self.first_name_input.setPlaceholderText("Type your first name")
        self.last_name_input= QtWidgets.QLineEdit()
        self.last_name_input.setPlaceholderText("Type your last name")
        self.id_input= QtWidgets.QLineEdit()
        validator=QtGui.QIntValidator()
        self.id_input.setValidator(validator)
        self.id_input.setPlaceholderText("Type your ID")
        self.active_radio=QtWidgets.QRadioButton()
        self.inactive_radio=QtWidgets.QRadioButton()
        self.active_radio.setText("Active")
        self.inactive_radio.setText("Inactive")
        #يجمع أزرار الـ radio مع بعض
        # يضمن إن زر واحد فقط يكون مفعّل في وقت واحد (Exclusive behavior)
        self.status_group=QtWidgets.QButtonGroup()
        self.status_group.addButton(self.active_radio)
        self.status_group.addButton(self.inactive_radio)
        # اضافة الحقول الي التخطيط
        self.layout.addRow('First name: ',self.first_name_input)
        self.layout.addRow('last name: ',self.last_name_input)
        self.layout.addRow('ID: ',self.id_input)
        self.layout.addRow('Status: ',self.active_radio)
        self.layout.addRow('',self.inactive_radio)
        #زر الإرسال
        submit_btn=QtWidgets.QPushButton('Add')
        self.layout.addRow(submit_btn)
        submit_btn.clicked.connect(self.submit)
    def show_message(self,title,message):
        QtWidgets.QMessageBox.critical(self, title, message)
    def check_id(self,member_id):
        for row in self.db.fetch():
            if member_id in row:
                return True
        return False
    def reset_form(self):
            self.first_name_input.clear()
            self.last_name_input.clear()
            self.id_input.clear()
            sender=self.status_group.checkedButton()
            self.status_group.setExclusive(False)# تعطيل الحصر داخل الجروب
            sender.setChecked(False)
            self.status_group.setExclusive(True)
    def submit(self):
        #التحقق من حالة العضو
        if self.active_radio.isChecked():
            status='active'
        elif self.inactive_radio.isChecked():
            status='inactive'
        else:
            self.show_message('wrong','please select status.')
            return  #"ارجع فورًا واخرج من الدالة".

        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        member_id = self.id_input.text()
        # التحقق من الخانات
        if not first_name or not last_name or not member_id:
            self.show_message('Wrong','Please, fill in all fields.')
            return
        # التحقق من الID
        if self.check_id(member_id):
            self.show_message('Wrong', 'ID already exists.')
            return
        #ارسال البيانات
        self.db.insert_data(first_name, last_name, member_id, status)
        # تنظيف النموذج
        self.reset_form()
        QtWidgets.QMessageBox.information(self,'Saved',"member added successfully.")
        self.close() #اغلاق النافذة